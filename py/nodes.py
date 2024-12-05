from .haiper_api_node import (
    I2VPipelineNode,
    T2VPipelineNode,
    T2IPipelineNode,
    KFCPipelineNode,
)
from .imgbb_node import ImgBBUpload

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "ImgBBUpload": ImgBBUpload,
    "HaiperImage2Video": I2VPipelineNode,
    "HaiperText2Video": T2VPipelineNode,
    "HaiperText2Image": T2IPipelineNode,
    "HaiperKeyframeConditioning": KFCPipelineNode,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ImgBBUpload": "ImgBB Upload",
    "HaiperImage2Video": "Haiper Image to Video",
    "HaiperText2Video": "Haiper Text to Video",
    "HaiperText2Image": "Haiper Text to Image",
    "HaiperKeyframeConditioning": "Haiper Keyframe Conditioning",
}
