
from flask import Blueprint, redirect, render_template, url_for

busket = Blueprint('busket', __name__,
                         url_prefix='/busket')


@busket.route('/')
def index():
    return redirect(url_for('.my_busket'))

@busket.route('/my-busket/')
def my_busket():
    return render_template('busket/my-busket.html')

