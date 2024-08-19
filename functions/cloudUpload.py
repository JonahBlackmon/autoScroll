import cloudinary
import cloudinary.uploader
import os as os
from dotenv import load_dotenv
from functions.pathConfig import get_default
load_dotenv()

default_path = get_default()

cloudinary.config (
    cloud_name = os.getenv('CLOUDINARY_NAME'),
    
    api_key = os.getenv('CLOUDINARY_KEY'),

    api_secret = os.getenv('CLOUDINARY_SECRET'),
    
    secure = True
)





def cloud_upload():
    for files in os.listdir(f'{default_path}/autoScroll/Outputs'):
        responses = []
        file_name = files
        response = cloudinary.uploader.upload(file_name, resource_type="video")
        responses.append(response['secure_url'])
    return responses
