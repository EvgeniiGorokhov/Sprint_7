class Data:
    LOGIN = 'Igor1'
    PASSWORD = 'Fgtkmcby'
    FIRSTNAME = 'IGOR'
    VALID_COURIER_DATA = {'login': 'Igor1', 'password': 'Fgtkmcby', 'firstName': 'IGOR'}
    COURIER_DATA_WITH_WRONG_PASSWORD = {'login': 'Igor12', 'password': '1233'}


class OrderData:

    ORDER_DATA_GREY_1 = {
        'firstName': 'Геральт',
        'lastName': 'ИзРивии',
        'address': 'Новиградский проспект, 16',
        'metroStation': 8,
        'phone': '+78005553535',
        'rentTime': 3,
        'deliveryDate': '2024-06-26',
        'comment': '— Правда, — сказала пустельга, — это осколок льда.',
        'color': [
            'GREY'
        ]
    }

    ORDER_DATA_BLACK_2 = {
        'firstName': 'Римуру',
        'lastName': 'Темпесуто',
        'address': ' Великий Лес Джуры',
        'metroStation': 8,
        'phone': '+78888888888',
        'rentTime': 3,
        'deliveryDate': '2024-07-12',
        'comment': 'Хм, распогодилось :)',
        'color': [
            'BLACK'
        ]
    }

    ORDER_DATA_TWO_COLORS_3 = {
        'firstName': 'Аврора Суя Рис',
        'lastName': 'Каймин',
        'address': 'Замок демона',
        'metroStation': 15,
        'phone': '+70009991122',
        'rentTime': 1,
        'deliveryDate': '2024-06-30',
        'comment': 'Ужасненько хочется покататься!',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    ORDER_DATA_NO_COLORS_4 = {
        'firstName': 'Лянь',
        'lastName': 'Се',
        'address': 'Государства Сяньлэ',
        'metroStation': 20,
        'phone': '+77777777777',
        'rentTime': 2,
        'deliveryDate': '2024-06-27',
        'comment': 'Сопротивляться судьбе может быть не менее рискованно, чем отдать себя в ее руки',
        'color': []
    }
