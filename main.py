# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
from conf import robot_cleaner

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}


# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
    # Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )


# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if user_id != 'AFCB03FF9199C0E7CDDBEFF530E40CBD0C23F62F16F6BE7523D346A533AE4647':
        res['response']['text'] = 'Тебе сюда вход закрыт'
        return

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        sessionStorage[user_id] = {
            'suggests': [
                "Стоп",
                "Останови",
                "Старт",
                "Поехали",
                "На зарядку",
                "На подзярядку",
                "Домой",
                "Найти",
                "Где пылесос",
            ]
        }

        res['response']['text'] = 'Привет! Давай начнем управлять пылесосом, что будем делать?'
        res['response']['buttons'] = get_suggests(user_id)
        robot_cleaner.status()
        return

    # Обрабатываем ответ пользователя.
    if req['request']['original_utterance'].lower() in [
        'стоп',
        'останови',
    ]:
        # Пользователь дал команду.
        res['response']['text'] = 'Стоп пылесоса!'
        # todo  не работает остановка пылесоса
        robot_cleaner.pause()
        # return
    elif req['request']['original_utterance'].lower() in [
        'старт',
        'поехали',
    ]:
        # Пользователь дал команду.
        res['response']['text'] = 'Старт пылесоса!'
        robot_cleaner.start()
        # return
    elif req['request']['original_utterance'].lower() in [
        'на зарядку',
        'на подзарядку',
        'домой',
    ]:
        # Пользователь дал команду.
        res['response']['text'] = 'Пылесос домой!'
        robot_cleaner.home()
        # return
    elif req['request']['original_utterance'].lower() in [
        'найти',
        'где пылесос',
    ]:
        # Пользователь дал команду.
        res['response']['text'] = 'Найти пылесос!'
        robot_cleaner.find()
        # return
    else:
        # Показать что не знает выбранной команды!
        res['response']['text'] = 'Прости я не знаю команды "%s", выбери среди [старт, стоп, домой, найти]!' % (
            req['request']['original_utterance']
        )
    res['response']['buttons'] = get_suggests(user_id)


# Функция возвращает две подсказки для ответа.
def get_suggests(user_id):
    session = sessionStorage[user_id]

    # Выбираем две первые подсказки из массива.
    suggests = [
        {'title': suggest, 'hide': True}
        # for suggest in session['suggests'][:2]
        for suggest in session['suggests']
    ]

    # # Убираем первую подсказку, чтобы подсказки менялись каждый раз.
    # session['suggests'] = session['suggests'][1:]
    # sessionStorage[user_id] = session
    #
    # # Если осталась только одна подсказка, предлагаем подсказку
    # # со ссылкой на Яндекс.Маркет.
    # if len(suggests) < 2:
    #     suggests.append({
    #         "title": "Ладно",
    #         "url": "https://market.yandex.ru/search?text=слон",
    #         "hide": True
    #     })

    return suggests


app.run()
