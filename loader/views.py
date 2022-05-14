from flask import Blueprint, render_template, request
import logging
import main.utils
from loader.utils import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='logger.log', level=logging.INFO)


@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def page_post_upload():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        logging.info("Отсутствует часть данных")
        return "Данные не загружены"
    posts = main.utils.load_json_data(POST_PATH)
    try:
        post_path = save_image(picture)
    except WrongImageType:
        return "Неверный тип изображения"
    new_post = {'pic': post_path, 'content': content}
    add_post(posts, new_post)

    return render_template('post_uploaded.html', new_post=new_post)
