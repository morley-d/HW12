from flask import Blueprint, render_template, request
import logging
from config import *
from main.utils import *
from exeptions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='logger.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    logging.info("Открыта главная страница")
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s', '')
    logging.info("Выполняется поиск")
    try:
        all_posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Ошибка открытия файла постов"
    posts = search_posts_by_substring(all_posts, s)
    return render_template('post_list.html', posts=posts, s=s)
