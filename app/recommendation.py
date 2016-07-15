from flask import Blueprint, redirect, render_template, request, url_for

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


@recommendation.route('/benefit/select-category/')
def benefit_select_category():
    monthly_total_usage = request.args.get('monthly-total-usage', type=int)
    if not monthly_total_usage:
        return redirect(url_for('.benefit_monthly_total_usage'))
    categories = [
        {
            'name': '교통',
            'image': {
                'url': url_for('static',
                               filename='images/category/transportation.png'),
            }
        },
        {
            'name': '통신사',
            'image': {
                'url': url_for('static',
                               filename='images/category/telecom.png'),
            }
        },
        {
            'name': '음식점',
            'image': {
                'url': url_for('static',
                               filename='images/category/food.png'),
            }
        },
        {
            'name': '커피',
            'image': {
                'url': url_for('static',
                               filename='images/category/coffee.png'),
            }
        },
        {
            'name': '영화',
            'image': {
                'url': url_for('static',
                               filename='images/category/movie.png'),
            }
        },
        {
            'name': '온라인 쇼핑',
            'image': {
                'url': url_for('static',
                               filename='images/category/shopping.png'),
            }
        },
        {
            'name': '백화점',
            'image': {
                'url': url_for(
                    'static', filename='images/category/department_store.png'
                )
            }
        },
        {
            'name': '할인',
            'image': {
                'url': url_for('static',
                               filename='images/category/sale.png'),
            }
        },
        {
            'name': '교육',
            'image': {
                'url': url_for('static',
                               filename='images/category/education.png'),
            }
        },
        {
            'name': '병원 / 약국',
            'image': {
                'url': url_for('static',
                               filename='images/category/hospital.png'),
            }
        },
        {
            'name': '의류',
            'image': {
                'url': url_for('static',
                               filename='images/category/clothing.png'),
            }
        },
        {
            'name': '놀이공원',
            'image': {
                'url': url_for('static',
                               filename='images/category/park.png'),
            }
        },
    ]
    return render_template('recommendation/benefit/select-category.html',
                           monthly_total_usage=monthly_total_usage,
                           categories=categories)


@recommendation.route('/benefit/usage-of-each-category/')
def usage_of_each_category():
    pass


@recommendation.route('/usage-pattern/')
def usage_pattern():
    return ''
