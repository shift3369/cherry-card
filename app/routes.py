from flask import Blueprint, render_template, url_for

app = Blueprint('routes', __name__)


@app.route('/')
def index():
    banners = [
        {
            'image': {
                'url': url_for('static', filename='images/banner-1.png')
            },
            'label': '통신사 할인',
            'content': 'SK KT LGU+\n내가 쓰는 통신사 1등 할인카드는?',
        },
        {
            'image': {
                'url': url_for('static', filename='images/banner-2.png')
            },
            'label': '항공 마일리지',
            'content': '실용적인 여행을 계획하는\n당신을 위한 항공마일리지 카드',
        },
        {
            'image': {
                'url': url_for('static', filename='images/banner-3.png')
            },
            'label': '교통 할인',
            'content': '버스, 지하철 대중교통\n매월 최대 600원 정액할인',
        }
    ]
    return render_template('index.html', banners=banners)
