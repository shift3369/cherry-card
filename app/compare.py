from flask import Blueprint, redirect, render_template, url_for

compare = Blueprint('compare', __name__,
                         url_prefix='/compare')


@compare.route('/')
def index():
    return redirect(url_for('.card_compare'))

@compare.route('/card-compare/')
def card_compare():
    return render_template('compare/card-compare.html')
