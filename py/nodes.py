from .haiper_api_node import (
    I2VPipelineNode,
    T2VPipelineNode,
    T2IPipelineNode,
)
from .imgbb_node import ImgBBUpload

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "ImgBBUpload": ImgBBUpload,
    "HaiperImage2Video": I2VPipelineNode,
    "HaiperText2Video": T2VPipelineNode,
    "HaiperText2Image": T2IPipelineNode,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ImgBBUpload": "ImgBB Upload",
    "HaiperImage2Video": "Image to Video",
    "HaiperText2Video": "Text to Video",
    "HaiperText2Image": "Text to Image",
}
