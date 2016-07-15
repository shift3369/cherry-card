# -*- coding: utf-8 -*-
import re

from flask import url_for
from xlsx import Workbook


def parse(path):


    categories = ['education', 'shopping', 'name', 'beauty', 'restaurant',
                  'culture', 'movie', 'medical', 'gas', 'descript', 'cvs',
                  'reisure', 'phone', 'transport', 'financial', 'cafe',
                  'annualfee']

    category_map = {
        '식비': {
            '커피/음료': 'cafe',
            '기타': 'restaurant',
        },
        '주거/통신': {
            '기타': 'financial',
        },
        '생활용품': {
            '기타': 'shopping',
        },
        '의복/미용': {
            '헤어/뷰티': 'beauty',
            '세탁수선비': 'beauty',
            '기타': 'shopping',
        },
        '건강/문화': {
            '운동/레저': 'reisure',
            '문화생활': 'culture',
            '여행': 'reisure',
            '병원비': 'medical',
            '기타': 'culture',
            '보장성보험': 'medical',
        },
        '교육/육아': {
            '육아용품': 'shopping',
            '기타': 'education',
        },
        '교통/차량': {
            '기타': 'transport',
        },
        '경조사/회비': {
            '데이트': 'culture',
            '기타': 'shopping',
        },
        '세금/이자': {
            '기타': 'financial',
        },
        '용돈/기타': {
            '기타': 'financial',
        },
        '저축/보험': {
            '기타': 'financial',
        },
    }

    cards = [
        {'name': '신한 러브카드', 'descript': '똑똑한소비, 외식/카페 최대30%할인 백화점부터 온라인쇼핑까지 거침없는할인',
         'annualfee': '내전용 8천원, 해외겸용 1만원', 'movie': 7000, 'restaurant': 0.3,
         'shopping': 0.05, 'gas': 0.04,'image':{'url':'c1.jpg'}},
        {'name': '신한카드 YOLOⓘ', 'descript': 'you only live once!할인율과 디자인을 내 마음대로!!',
         'annualfee': '국내전용 1만5천원, 해외겸용 1만8천원', 'movie': 50000, 'cafe': 50000,
         'transport': 50000, 'shopping': 50000, 'cvs': 50000,'image':{'url':'c2.jpg'}},
        {'name': '현대카드 ZERO', 'descript': '2~6월 C카드비교사이트 인기차트1위 무조건 할인카드의 대표, 현대카드',
         'annualfee': '국내전용 5천원, 해외겸용 1만원', 'movie': 0.07, 'restaurant': 0.12,
         'phone': 0.7, 'transport': 0.12, 'shopping': 0.07, 'cvs': 0.05,
         'culture': 0.15, 'gas': 0.07, 'education': 0.15, 'beauty': 0.15,
         'medical': 0.15, 'financial': 0.12,'image':{'url':'c3.png'}},
        {'name': '현대카드X3 Edition2모바일',
         'descript': '시즌스페셜 할인처에서 5%/10%할인 영화,커피,주차할인 등 플래티넘서비스',
         'annualfee': '국내전용 6만5천원, 해외겸용 6만5천원',
         'movie': 3000, 'restaurant': 0.05,
         'phone': 0.05, 'cafe': 0.05,
         'reisure': 0.05, 'transport': 0.05,
         'shopping': 0.05, 'cvs': 0.05,
         'gas': 0.05, 'education': 0.05,
         'beauty': 0.05, 'medical': 0.05,
         'financial': 0.05,'image':{'url':'c4.jpg'}},
        {'name': '삼성카드 2 V2',
         'descript': '교통·통신 10%, 커피전문점 5% CGV·롯데시네마 3천원·6천원 할인',
         'annualfee': '국내전용 1만8천원, 해외겸용 1만8천원', 'movie': 3000, 'phone': 0.1,
         'cafe': 0.05, 'transport': 0.1,'image':{'url':'c5.png'}},
        {'name': '삼성카드 4', 'descript': '모든 가맹점 할인, 무이자할부!영화관2,500원할인, 주야간발급',
         'annualfee': '국내전용 5천원, 해외겸용 1만원', 'movie': 2500, 'restaurant': 0.07,
         'phone': 0.07, 'cafe': 0.07, 'shopping': 0.07, 'cvs': 0.7, 'culture': 0.07,
         'gas': 0.07, 'education': 0.07, 'beauty': 0.07, 'medical': 0.07,
         'financial': 0.07,'image':{'url':'c6.jpg'}}, {'name': 'KB국민 FINETECH카드',
                              'descript': '스타벅스 50%, 교통 20% 할인, CGV, 통신비 5천원 할인까지',
                              'annualfee': '국내전용 1만2천원, 해외겸용 1만7천원', 'movie': 3000,
                              'phone': 5000, 'cafe': 0.3, 'transport': 0.2,
                              'culture': 0.1,'image':{'url':'c7.jpg'}}, {'name': 'KB국민 굿데이카드모바일',
                                                 'descript': '대중교통, 통신, 주유 업종 청구할인,음식, 편의점, 학원 업종 청구할인',
                                                 'annualfee': '국내전용 5천원, 해외겸용 1만원',
                                                 'phone': 0.1, 'transport': 0.1,
                                                 'cvs': 0.1, 'gas': 0.25,
                                                 'education': 0.1,'image':{'url':'c8.png'}},
        {'name': '롯데 아이행복 카드', 'descript': '어린이집, 학원비, 학습지 10%할인,오늘 신청, 내일 수령!',
         'annualfee': '국내전용 무료, 해외겸용 무료', 'movie': 1500, 'restaurant': 0.1,
         'phone': 2000, 'cafe': 0.1, 'transport': 0.1, 'shopping': 0.05, 'cvs': 0.1,
         'education': 0.05, 'medical': 0.05,'image':{'url':'c9.jpg'}}, {'name': '트래블패스 시그니처 카드',
                                              'descript': '1,500원당 최고 2플라이어마일적립, 국내선 동반자 무료 항공권 서비스',
                                              'annualfee': '해외겸용 12만원',
                                              'movie': 1500, 'cafe': 0.1,
                                              'reisure': 0.2, 'shopping': 0.3,
                                              'beauty': 0.15,'image':{'url':'c10.png'}},
        {'name': '하나POP(팝) 카드',
         'descript': 'GS25, GS수퍼 10% 청구할인, 커피, 영화, 서점, 화장품 5%할인',
         'annualfee': '국내전용 8천원, 해외겸용 1만원', 'movie': 0.05, 'cafe': 0.05, 'cvs': 0.1,
         'culture': 0.05, 'beauty': 0.05,'image':{'url':'c11.png'}}, {'name': '하나2X α (투엑스알파)',
                                             'descript': '인터넷쇼핑, 커피, 편의점 등 할인, 오래쓰면 할인율 2배+할인한도 2배!',
                                             'annualfee': '국내전용 9천원, 해외겸용 1만원',
                                             'movie': 2000, 'restaurant': 0.1,
                                             'phone': 0.1, 'cafe': 0.25,
                                             'transport': 0.07, 'shopping': 0.1,
                                             'cvs': 0.1, 'gas': 0.25,'image':{'url':'c12.jpg'}},
        {'name': '우리V카드 Tiara(티아라)',
         'descript': 'Enjoy the lady style, 백화점,택시 10% 커피 25% 할인',
         'annualfee': '국내전용 2천원, 해외겸용 5천원', 'movie': 6000, 'restaurant': 0.25,
         'cafe': 0.25, 'reisure': 0.5, 'transport': 0.1, 'shopping': 0.1,'image':{'url':'c13.png'}},
        {'name': '우리 다모아 할인카드', 'descript': '카드사용 전월실적에 따라, 레스토랑 20%, 영화관 3천원 할인',
         'annualfee': '국내전용 5천원, 해외겸용 1만원', 'movie': 3000, 'restaurant': 0.2,
         'cafe': 0.2, 'reisure': 0.5,'image':{'url':'c14.jpg'}}]
    workbook = Workbook(path)
    sheet = next(iter(workbook))
    grouped = {}
    for row, cells in sheet.rowsIter():
        date = re.match('^(\d{4})년0?(\d+)월0?(\d+)일$', cells[0].value)
        if not date:
            continue
        price = int(cells[3].value.replace(',', ''))
        category, item = cells[7].value.split('>')
        if category == '이체/대체':
            continue
        items = category_map[category]
        card_category = items[item if item in items else '기타']
        grouped.setdefault(card_category, []).append(price)
    for card in cards:
        money = 0
        for category, price in grouped.items():
            benefit = card.get(category)
            if benefit:
                if benefit <= 1:
                    money += int(sum(price) * benefit)
                else:
                    money += min(benefit, sum(price))
        card['money'] = money

    for i, card in enumerate(cards, 1):
        card['image'] = {'url': url_for('static', filename='images/' + card['image']['url'])}
    cards.sort(key=lambda x: x['money'], reverse=True)
    return cards
