import json
from config import *
from exeptions import *


def save_image(picture):
    allowed_type = ["jpg", "jpeg", "png", "img", "gif"]
    picture_type = picture.filename.split('.')[-1]
    if picture_type not in allowed_type:
        raise WrongImageType("Неверный формат файла")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(post_list, file)
