from flask import Blueprint, render_template, request
import logging

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
    pass
