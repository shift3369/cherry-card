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
@recommendation.route('/result/')
def result():
    return redirect(url_for('.recommendation_result'))

@recommendation.route('/result/recommendation_result/')
def recommendation_result():
    recommendation_cards = [
	{
		'image': {
 			'url' :url_for('static', filename='images/bg_maincard.png')},
			'hashtag': '#영화 #편의점 #교통 #커피',
			'name': '삼성카드6 V2',
			'total_benefit': '28500',
			'benefits': [{'benefit': '영화', 'price': '10000'}, 
					{'benefit': '편의점', 'price': '12000'},
					{'benefit': '교통', 'price': '30000'},
					{'benefit': '커피', 'price': '20000'}]
	},
        {
                'image': {
                        'url' :url_for('static', filename='images/bg_nextcard.png')},
                        'hashtag': '#영화 #편의점 #온라인쇼핑 #커피',
                        'name': '삼성카드3',
                        'total_benefit': '31500',
                        'benefits': [{'benefit': '영화', 'price': '10000'}, 
                                        {'benefit': '편의점', 'price': '22000'},
                                        {'benefit': '온라인쇼핑', 'price': '50000'},
                                        {'benefit': '커피', 'price': '20000'}]
        },
        {
                'image': {
                        'url' :url_for('static', filename='images/bg_maincard.png')},
                        'hashtag': '#영화 #항공  #교통 #통신사',
                        'name': '삼성카드5 V3',
                        'total_benefit': '48500',
                        'benefits': [{'benefit': '영화', 'price': '10000'}, 
                                        {'benefit': '항공', 'price': '12000'},
                                        {'benefit': '교통', 'price': '30000'},
                                        {'benefit': '통신사', 'price': '20000'}]
        }]

    return render_template('recommendation/result/recommendation-result2.html', recommendation_cards=recommendation_cards)

@recommendation.route('/result/recommendation-result-detail')
def recommendation_result_detail():
    return render_template('recommendation/result/recommendation-result-detail.html')
