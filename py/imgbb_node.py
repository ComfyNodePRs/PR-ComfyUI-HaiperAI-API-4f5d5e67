# Based on https://github.com/revirevy/Comfyui_saveimage_imgbb/blob/main/ImgBBUploader.py
import requests
import base64
from PIL import Image
import io
import numpy as np
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the imgbb key
imgbb_key = os.getenv('IMGBB_KEY')

class ImgBBUpload:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("image_url",)

    FUNCTION = "upload"

    CATEGORY = "image/upload"

    def upload(self, image):
        # Convert image tensor to PIL Image
        img = image[0]
        img = 255.0 * img.cpu().numpy()
        img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))

        # Save PIL Image to buffer
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

        url = f"https://api.imgbb.com/1/upload?key={imgbb_key}"

        payload = {
            "image": base64_image,
        }

        try:
            response = requests.post(url, data=payload)
            result = response.json()

            if result.get("success"):
                return result["data"]["url"], result["data"]["delete_url"]
            else:
                error_message = result.get("error", {}).get("message", "Unknown error")
                raise ValueError(f"Error: {error_message}")
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")


NODE_CLASS_MAPPINGS = {"ImgBBUpload": ImgBBUpload}

NODE_DISPLAY_NAME_MAPPINGS = {"ImgBBUpload": "Upload to ImgBB"}
