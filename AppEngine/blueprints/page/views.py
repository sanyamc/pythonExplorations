from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
import os

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')

@page.route('/faq')
def faq():
    return render_template('page/faq.html')


# @page.route('/', defaults = {'page': 'home'})
# @page.route('/<page>')
# def pages(page):
#     try:
#         #import os 
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         print('page is -----> {}'.format(page))
#         return render_template('page/{}.html'.format(page))
#     except TemplateNotFound as e:
#         return "Exception: {}".format(dir_path)


# def test():
#     pass
