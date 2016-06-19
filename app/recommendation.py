from flask import Blueprint, redirect, render_template, url_for

recommendation = Blueprint('recommendation', __name__,
                           url_prefix='/recommendation')


@recommendation.route('/')
def index():
    return redirect(url_for('.select_method'))


@recommendation.route('/select-method/')
def select_method():
    return render_template('recommendation/select-method.html')


@recommendation.route('/benefit/')
def benefit():
    return redirect(url_for('.benefit_monthly_total_usage'))


@recommendation.route('/benefit/monthly_total_usage/')
def benefit_monthly_total_usage():
    return render_template('recommendation/benefit/monthly-total-usage.html')


@recommendation.route('/usage-pattern/')
def usage_pattern():
    return ''
