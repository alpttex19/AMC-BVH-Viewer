# 核心骨骼名称映射规则
JOINT_MAPPING = {
    "Hips": "root",
    "Spine": "lowerback",
    "Spine1": "middleback",
    "Spine2": "upperback",
    "Spine3": "thorax",
    "Neck": "lowerneck",
    "Neck1": "upperneck",
    "Head": "head",
    "RightShoulder": "rclavicle",
    "LeftShoulder": "lclavicle",
    "RightArm": "rhumerus",
    "LeftArm": "lhumerus",
    "RightForeArm": "rradius",
    "LeftForeArm": "lradius",
    "RightHand": "rwrist",
    "LeftHand": "lwrist",
    "RightHandThumb1": "rthumb",
    "LeftHandThumb1": "lthumb",
    "RightHandMiddle1": "rhand",
    "LeftHandMiddle1": "lhand",
    "RightHandMiddle2": "rfingers",
    "LeftHandMiddle2": "lfingers",
    "RightUpLeg": "rhipjoint",
    "LeftUpLeg": "lhipjoint",
    "RightLeg": "rfemur",
    "LeftLeg": "lfemur",
    "RightFoot": "rtibia",
    "LeftFoot": "ltibia",
    "RightToeBase": "rfoot",
    "LeftToeBase": "lfoot",
    "RightToeBaseEnd": "rtoes",
    "LeftToeBaseEnd": "ltoes",
}
JOINT_DOF_INFO = {
    "root": f"""     axis 0 0 0  XYZ""",
    "lhipjoint": f"""     axis 0 0 0  XYZ""",
    "lfemur": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "ltibia": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lfoot": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "ltoes": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rhipjoint": f"""     axis 0 0 0  XYZ""",
    "rfemur": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rtibia": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rfoot": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rtoes": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lowerback": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "middleback": f"""     axis 0 0 0  XYZ
       dof rx ry rz
       limits (-180.0 180.0)
              (-180.0 180.0)
              (-180.0 180.0)""",
    "upperback": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "thorax": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lowerneck": f"""     axis 0 0 0   XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "upperneck": f"""     axis 0 0 0   XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "head": f"""     axis 0 0 0   XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lclavicle": f"""     axis 0 0 0   XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lhumerus": f"""     axis 0 0 0   XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lradius": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lwrist": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lhand": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lfingers": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "lthumb": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rclavicle": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rhumerus": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rradius": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rwrist": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rhand": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rfingers": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
    "rthumb": f"""     axis 0 0 0  XYZ
   dof rx ry rz
   limits (-180.0 180.0)
          (-180.0 180.0)
          (-180.0 180.0)""",
}

ASF_HIERARCHY = f""":hierarchy
  begin
    root lhipjoint rhipjoint lowerback
    lhipjoint lfemur
    lfemur ltibia
    ltibia lfoot
    lfoot ltoes
    rhipjoint rfemur
    rfemur rtibia
    rtibia rfoot
    rfoot rtoes
    lowerback middleback
    middleback upperback
    upperback thorax
    thorax lowerneck lclavicle rclavicle
    lowerneck upperneck
    upperneck head
    lclavicle lhumerus
    lhumerus lradius
    lradius lwrist
    lwrist lhand lthumb
    lhand lfingers
    rclavicle rhumerus
    rhumerus rradius
    rradius rwrist
    rwrist rhand rthumb
    rhand rfingers
  end\n"""

ASF_PREFIX = f"""# ASF skeleton converted from BVH
:version 1.10
:name root
:units
  mass 1.0
  length 0.45
  angle deg
:documentation
   .ast/.asf automatically generated from VICON data using
   VICON BodyBuilder and BodyLanguage model FoxedUp or BRILLIANT.MOD
:root
  order TX TY TZ RX RY RZ
  axis XYZ
  position 0 0 0
  orientation 0 0 0
:bonedata\n"""

AMC_PREFIX = f"""#!OML:ASF H:\Terrain\Patient Classification 1\Walking\liu\liu.ASF
:FULLY-SPECIFIED
:DEGREES\n"""

# JOINT_DOF_INFO = {
#     "root": f"""     axis 0 0 0  XYZ""",
#     "lhipjoint": f"""     axis 0 0 0  XYZ""",
#     "lfemur": f"""     axis 0 0 20  XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "ltibia": f"""     axis 0 0 20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lfoot": f"""     axis -90 0 20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "ltoes": f"""     axis -90 0 20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rhipjoint": f"""     axis 0 0 0  XYZ""",
#     "rfemur": f"""     axis 0 0 -20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rtibia": f"""     axis 0 0 -20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rfoot": f"""     axis -90 0 -20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rtoes": f"""     axis -90 0 -20   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lowerback": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "upperback": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "thorax": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lowerneck": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "upperneck": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "head": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lclavicle": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lhumerus": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lradius": f"""     axis 180 -30 -90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lwrist": f"""     axis 0 90 90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lhand": f"""     axis 0 90 90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lfingers": f"""     axis 0 90 90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "lthumb": f"""     axis -90 45 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rclavicle": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rhumerus": f"""     axis 180 30 90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rradius": f"""     axis 180 30 90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rwrist": f"""     axis 0 -90 -90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rhand": f"""     axis 0 -90 -90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rfingers": f"""     axis 0 -90 -90   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
#     "rthumb": f"""     axis -90 -45 0   XYZ
#    dof rx ry rz
#    limits (-180.0 180.0)
#           (-180.0 180.0)
#           (-180.0 180.0)""",
# }

# JOINT_DOF_INFO = {
#     "lhipjoint": f"""     axis 0 0 0  XYZ""",
#     "lfemur": f"""     axis 0 0 20  XYZ
#    dof rx ry rz
#    limits (-160.0 20.0)
#           (-70.0 70.0)
#           (-60.0 70.0)""",
#     "ltibia": f"""     axis 0 0 20   XYZ
#    dof rx
#    limits (-10.0 170.0)""",
#     "lfoot": f"""     axis -90 0 20   XYZ
#    dof rx rz
#    limits (-45.0 90.0)
#           (-70.0 20.0)""",
#     "ltoes": f"""     axis -90 0 20   XYZ
#    dof rx
#    limits (-90.0 20.0)""",
#     "rhipjoint": f"""     axis 0 0 0  XYZ""",
#     "rfemur": f"""     axis 0 0 -20   XYZ
#    dof rx ry rz
#    limits (-160.0 20.0)
#           (-70.0 70.0)
#           (-70.0 60.0)""",
#     "rtibia": f"""     axis 0 0 -20   XYZ
#    dof rx
#    limits (-10.0 170.0)""",
#     "rfoot": f"""     axis -90 0 -20   XYZ
#    dof rx rz
#    limits (-45.0 90.0)
#           (-20.0 70.0)""",
#     "rtoes": f"""     axis -90 0 -20   XYZ
#    dof rx
#    limits (-90.0 20.0)""",
#     "lowerback": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-20.0 45.0)
#           (-30.0 30.0)
#           (-30.0 30.0)""",
#     "upperback": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-20.0 45.0)
#           (-30.0 30.0)
#           (-30.0 30.0)""",
#     "thorax": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-20.0 45.0)
#           (-30.0 30.0)
#           (-30.0 30.0)""",
#     "lowerneck": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-20.0 45.0)
#           (-30.0 30.0)
#           (-30.0 30.0)""",
#     "upperneck": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-20.0 45.0)
#           (-30.0 30.0)
#           (-30.0 30.0)""",
#     "head": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-20.0 45.0)
#           (-30.0 30.0)
#           (-30.0 30.0)""",
#     "lclavicle": f"""     axis 0 0 0   XYZ
#    dof ry rz
#    limits (-20.0 10.0)
#           (0.0 20.0)""",
#     "lhumerus": f"""     axis 0 0 0   XYZ
#    dof rx ry rz
#    limits (-60.0 90.0)
#           (-90.0 90.0)
#           (-90.0 90.0)""",
#     "lradius": f"""     axis 180 -30 -90   XYZ
#    dof rx
#    limits (-10.0 170.0)""",
#     "lwrist": f"""     axis 0 90 90   XYZ
#    dof ry
#    limits (-180.0 0.0)""",
#     "lhand": f"""     axis 0 90 90   XYZ
#    dof rx rz
#    limits (-90.0 90.0)
#           (-45.0 45.0)""",
#     "lfingers": f"""     axis 0 90 90   XYZ
#    dof rx
#    limits (0.0 90.0)""",
#     "lthumb": f"""     axis -90 45 0   XYZ
#    dof rx rz
#    limits (-45.0 45.0)
#           (-45.0 45.0)""",
#     "rclavicle": f"""     axis 0 0 0   XYZ
#    dof ry rz
#    limits (-10.0 20.0)
#           (-20.0 0.0)""",
#     "rhumerus": f"""     axis 180 30 90   XYZ
#    dof rx ry rz
#    limits (-90.0 60.0)
#           (-90.0 90.0)
#           (-90.0 90.0)""",
#     "rradius": f"""     axis 180 30 90   XYZ
#    dof rx
#    limits (-10.0 170.0)""",
#     "rwrist": f"""     axis 0 -90 -90   XYZ
#    dof ry
#    limits (-180.0 0.0)""",
#     "rhand": f"""     axis 0 -90 -90   XYZ
#    dof rx rz
#    limits (-90.0 90.0)
#           (-45.0 45.0)""",
#     "rfingers": f"""     axis 0 -90 -90   XYZ
#    dof rx
#    limits (0.0 90.0)""",
#     "rthumb": f"""     axis -90 -45 0   XYZ
#    dof rx rz
#    limits (-45.0 45.0)
#           (-45.0 45.0)""",
# }
