#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request
import random
rg = random.Random()


def prime_test_miller_rabin(p):
    if p == 1 or p == 2 or p == 3 or p == 5:
        return True
    if p <= 0 or (p % 2 == 0) or (p % 5 ==0):
        return False
    s = 0
    d = p - 1
    while d % 2 == 0:
        s += 1
        d = d // 2
    for _ in range(10):
        a = rg.randint(2, p - 2)
        x = pow(a, d, p)
        if x == 1 or x == p - 1:
            continue
        stop = False
        for _ in range(s-1):
            x = pow(x, 2, p)
            if x == 1:
                return False
            if x == (p - 1):
                stop = True
                break
        if stop == True:
            continue
        else:
            return False
    return True


app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/prime', methods = ['GET', 'POST'])
def hello_name(func = prime_test_miller_rabin):
    result = ''
    cic = ''
    otvet =''

    if request.method == 'GET':
        name_param=request.args.get('prime')
    elif request.method == 'POST':
        name_param=request.form.get('prime')

    if name_param==None:
        name_param=""

    if name_param != "":
        tmp = int(name_param)
        result = func(tmp)
        if result == False:
            result = "Это составное!"
        elif result == True:
            result = "Это простое!"
        cic = "Что ж, Сумасшедший Жабен не так уж и плох. Пора начать следующий раунд"
        otvet = "Жабен вам отвечает: \"" + result + "\""
    

    return flask.render_template(
        'prime.html',
        prime = result,
        jabprime = otvet,
        ready = cic
    )

@app.route('/krok')
def krok():
    return flask.render_template(
        'krok.html',
    )
@app.route('/mnogo')
def mnogo():
    return flask.render_template(
        'mnogo.html',
    )
@app.route('/ivan')
def ivan():
    return flask.render_template(
        'ivan.html',
    )

@app.route('/evkl', methods = ['GET', 'POST'])  
def evklid():

    tmp = ''
    udar = ''
    itog = ''
    saying = ''

    if request.method == 'GET':
        name_param=request.args.get('great')
    elif request.method == 'POST':
        name_param=request.form.get('great')
    
    a = rg.randint(1,3)
    if a == 1:
        udar = 'Камень'
    elif a == 2:
        udar = 'Ножницы'
    elif a == 3:
        udar = 'Бумага'

    if name_param == udar:
        tmp = "Ничья!"
        itog = tmp + "Вы поставили: " + name_param + ", а ваш соперник:" + udar
        saying = "В любом случае, у вас впереди ещё один раунд, в котором всё решится"
    if (name_param == 'Камень' and udar == 'Ножницы') or (name_param == 'Ножницы' and udar == 'Бумага') or (name_param == 'Бумага' and udar == 'Камень'):
        tmp = "Победа!"
        itog = tmp + "Вы поставили: " + name_param + ", а ваш соперник:" + udar
        saying = "В любом случае, у вас впереди ещё один раунд, в котором всё решится"
    if (name_param == 'Камень' and udar == 'Бумага') or (name_param == 'Ножницы' and udar == 'Камень') or (name_param == 'Бумага' and udar == 'Ножницы'):
        tmp = "Поражение..."
        itog = tmp + "Вы поставили: " + name_param + ", а ваш соперник:" + udar
        saying = "В любом случае, у вас впереди ещё один раунд, в котором всё решится"
    

    return flask.render_template(
        'evkl.html',
        result = tmp,
        yours = name_param,
        bot = udar,
        words = itog,
        nextround = saying
    )

@app.route('/gipos', methods = ['GET', 'POST'])  
def gipos():

    saying = ''
    screen = ''

    if request.method == 'GET':
        name_param=request.args.get('exp')
    elif request.method == 'POST':
        name_param=request.form.get('exp')
    
    if name_param == "Решить квадратное уравнение":
        saying = "Конечно эта жаба решит квадратное уравнение! На это и пятиклассник способен! Вы проиграли! В следующий раз может больше повезет"
    elif name_param == "Доказать, что алгебраические уравнения 5 степени не имеют решения в радикалах":
        saying = "Жабка думала, думала... Но она то знает теорию Галуа. Поэтому она и выиграла, а вы проиграли!"
    elif name_param == "Доказать Гипотезу Пуанкаре":
        saying = "Хоть Сумасшедший Жабен и хорош в математике, но до такого ему ещё рановато. Вы дали задачу с которой он не справился, поэтому вы и занимаете первое место в нашем турнире!"
        screen = "Получить приз!"

    return flask.render_template(
        'gipos.html',
        final = saying,
        screen = screen 
    )



if __name__ == '__main__':
   app.run(debug = True)
