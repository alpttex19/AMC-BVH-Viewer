import numpy as np
from scipy.spatial.transform import Rotation
import bvhio

from bvh2asf_config import (
    JOINT_MAPPING,
    JOINT_DOF_INFO,
    AMC_PREFIX,
    ASF_PREFIX,
    ASF_HIERARCHY,
)


class BVHToASFConverter:
    def __init__(self):
        self.bvh_data = None
        self.skeleton_T = {}
        self.asf_bones = []
        self.root_xyz = None
        self.root_rpy = None
        self.start_loading = False
        self.unit_scale = 0.45  # BVH厘米转ASF米
        self.joint_mapping = JOINT_MAPPING  # 从配置文件加载关节映射
        self.dof_info = JOINT_DOF_INFO  # 从配置文件加载DOF信息

    def calcualte_bone_by_bvh_parser(self, filepath):
        """使用bvh_parser解析BVH层级"""
        root = bvhio.readAsHierarchy(filepath)
        # root.printTree()
        # # 设置单位缩放
        root.RestPose.Scale = self.unit_scale
        root.applyRestposeScale(recursive=True, bakeKeyframes=True)
        for joint, index, depth in root.loadRestPose(recursive=True).layout():
            joint_name = joint.Name
            if joint_name == "Hips":
                self.root_xyz = joint.PositionWorld
                self.root_rpy = joint.RotationWorld

            parent_pos = joint.PositionWorld
            if joint.Children:
                for child in joint.Children:
                    child_name = child.Name
                    child_pos = child.PositionWorld
                    parent_name = child.Parent.Name
                    parent_matrix = Rotation.from_quat(
                        child.Parent.RotationWorld.to_list(), scalar_first=True
                    ).as_matrix()
                    child_matrix = Rotation.from_quat(
                        child.RotationWorld.to_list(), scalar_first=True
                    ).as_matrix()
                    M_local = np.linalg.inv(parent_matrix) @ child_matrix
                    asf_joint_name = self.joint_mapping.get(child_name, child_name)
                    self.skeleton_T[asf_joint_name] = M_local
                    direction = child_pos - parent_pos
                    length = np.linalg.norm(direction)
                    direction_norm = direction / length if length != 0 else direction

                    # 存储骨骼数据
                    if child_name in self.joint_mapping.keys():
                        mapped_name = self.joint_mapping[child_name]
                        self.asf_bones.append(
                            {
                                "name": mapped_name,
                                "direction": direction_norm,
                                "length": length * self.unit_scale,
                            }
                        )

    def generate_asf(self, output_path):
        """生成完整的ASF文件"""

        with open(output_path, "w") as f:
            # 写入ASF头部
            f.write(ASF_PREFIX)

            # 写入骨骼属性
            for idx, bone in enumerate(self.asf_bones, 1):

                direction = " ".join(f"{v:.6f}" for v in bone["direction"])
                f.write(
                    f"""  begin
    id {idx}
    name {bone['name']}
    direction {direction}
    length {bone['length']:.6f}
{self.dof_info[bone['name']]}
  end\n"""
                )

            # 写入层级结构
            f.write(ASF_HIERARCHY)

    def calculate_dof_rotation(self, filepath, output_path):
        with open(output_path, "w") as f:
            f.write(AMC_PREFIX)
        """使用bvh_parser解析BVH层级"""
        root = bvhio.readAsHierarchy(filepath)
        print(len(root.Keyframes))
        # 设置单位缩放
        axis_seq = "YXZ"
        for i in range(len(root.Keyframes)):
            amc_data = []
            for joint, index, depth in root.loadPose(i, recursive=True).layout():
                joint_name = joint.Name
                if joint_name == "Hips":
                    root_xyz = joint.PositionWorld.to_list()
                    root_xyz = [
                        root_xyz[0] * self.unit_scale,
                        root_xyz[2] * self.unit_scale,
                        root_xyz[1] * self.unit_scale,
                    ]
                    root_quat = joint.RotationWorld.to_list()
                    root_euler = (
                        Rotation.from_quat(root_quat, scalar_first=True)
                        .as_euler(axis_seq, degrees=True)
                        .tolist()
                    )
                    # root_euler = [
                    #     root_euler[1],
                    #     root_euler[0],
                    #     root_euler[2],
                    # ]
                    root_name = self.joint_mapping.get(joint_name, joint_name)
                    amc_data.append(
                        {
                            "joint_name": root_name,
                            "anim_date": root_xyz + root_euler,
                        }
                    )

                elif joint_name in self.joint_mapping.keys():  # LeftUpLeg
                    # NOTE: 根据amc_parser 54行，计算关节旋转
                    asf_joint_name = self.joint_mapping.get(
                        joint_name, joint_name
                    )  # lhipjoint
                    asf_joint_info = self.dof_info.get(asf_joint_name, None)

                    parent_quat = joint.Parent.RotationWorld.to_list()
                    parent_matrix = Rotation.from_quat(
                        parent_quat, scalar_first=True
                    ).as_matrix()
                    if "dof" in asf_joint_info:
                        joint_xyz = joint.PositionWorld.to_list()
                        joint_xyz = [
                            joint_xyz[0] * self.unit_scale,
                            joint_xyz[2] * self.unit_scale,
                            joint_xyz[1] * self.unit_scale,
                        ]
                        joint_quat = joint.RotationWorld.to_list()
                        joint_matrix = Rotation.from_quat(
                            joint_quat, scalar_first=True
                        ).as_matrix()

                        total_rot = np.linalg.inv(parent_matrix) @ joint_matrix
                        rest_rot = self.skeleton_T[asf_joint_name]
                        euler_rot = np.linalg.inv(rest_rot) @ total_rot
                        joint_euler = (
                            Rotation.from_matrix(euler_rot)
                            .as_euler(axis_seq, degrees=True)
                            .tolist()
                        )
                        # joint_euler = [
                        #     joint_euler[1],
                        #     joint_euler[0],
                        #     joint_euler[2],
                        # ]
                        amc_data.append(
                            {
                                "joint_name": asf_joint_name,
                                "anim_date": joint_euler,
                            }
                        )

            self.generate_amc(output_path, i + 1, amc_data)

    def generate_amc(self, output_path, frame_idx, amc_data):
        """生成AMC文件"""
        with open(output_path, "a") as f:
            f.write(f"{frame_idx}\n")
            for frame_data in amc_data:
                joint_name = frame_data["joint_name"]
                anim_data = frame_data["anim_date"]
                anim_data_str = " ".join(f"{v:.6f}" for v in anim_data)
                f.write(f"{joint_name} {anim_data_str}\n")


if __name__ == "__main__":
    converter = BVHToASFConverter()
    converter.calcualte_bone_by_bvh_parser("animation.bvh")  # 替换为你的BVH文件路径
    converter.generate_asf("animation.asf")  # 指定输出路径
    converter.calculate_dof_rotation("animation.bvh", "animation.amc")
