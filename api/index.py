"""WELMS API BACKEND"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def abcrf():
    """--Returns index.html--"""

    return render_template('index6.html')


# @app.route('/about')
# def about():
#     """--Returns About--"""
#     return render_template('about.html')


# @app.route('/partners')
# def partners():
#     """--Returns About--"""
#     return render_template('blog.html')


# @app.route('/blog_single')
# def blog_single():
#     """--Returns About--"""
#     return render_template('single-blog.html')


# @app.route('/single_blog')
# def single_blog():
#     """--Returns About--"""
#     return render_template('single-blog.html')


# @app.route('/team')
# def team():
#     """--Returns Team--"""
#     return render_template('team.html')


# @app.route('/members')
# def members():
#     """--Returns Memebexrs--"""
#     return render_template('team.html')
