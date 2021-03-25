from flask import Flask, url_for, request, render_template,\
    redirect

import datetime as dt
import os

from sqlalchemy import or_

from data.jobs import Jobs
from data.users import User
from data import db_session


PROF_LIST = ('Инженер-исследователь',
             'Пилот', 'Строитель', 'Метеоролог',
             'Инженер по жизнеобеспечению',
             'Инженер по радиацинной защите',
             'Врач', 'Экзобиолог')

answer = {}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promote_mission():
    return '''
    Человечество вырастает из детства.
    </br></br>
    Человечеству мала одна планета.
    </br></br>
    Мы сделаем обитаемыми безжизненные пока планеты.
    </br></br>
    И начнем с Марса!
    </br></br>
    Присоединяйся!'''


@app.route('/image_mars')
def show_red_planet():
    return f'''<h1>Жди нас, Марс</h1>
    <img src="{url_for('static', filename='img/mars.png')}" alt="Красивая картинка Марса">
    </br>
    Вот она, красная планета
    '''


@app.route('/promotion_image')
def show_mars_and_promote():
    return render_template('show_mars_and_promote.html', title='Выбирай Марс!')


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def register_unit():
    global answer

    if request.method == 'GET':
        return render_template('register_unit.html', title='Отбор кандидатов')
    elif request.method == 'POST':
        answer = request.form
        return redirect('/answer')


@app.route('/choice/<planet_name>')
def promote_planet(planet_name: str):
    planet_name = planet_name.capitalize()
    planet_data = {
        'марс': ('https://korki.lol/wp-content/uploads/2017/10/mars.jpg',
                 'red',
                 'На марсе просыпаются самые замечательные идеи (все же читали Марсианин)',
                 'Экология Марса — лучшее, что может иметь человек',
                 'На Марсе есть вода!',
                 'Red Planet звучит круто, у любого спроси'),
        'меркурий': (
            'https://korki.lol/wp-content/uploads/2017/10/mercury.jpg',
            '#6E7F80',
            'Самая маленькая планета — самые маленькие проблемы',
            'Спутников нет, значит нет полнолуний. Прощайте, оборотни!',
            'Непредсказуемость орбиты — ежедневные сюрпризы (и не нужно праздников)',
            'Серый — хит сезона!'),
        'нептун': ('https://korki.lol/wp-content/uploads/2017/10/neptun.jpg',
                   '#2E6BB0',
                   'Кольца! О да, все их любят!',
                   'Мы думали, что это уже не планета, но оказалось, что это было про Плутон',
                   'На этой планете вы не постареете на год (он здесь в 164 раза длиннее земного)',
                   'Ветер — 260 м/с. Мы пока не придумали, в чём здесь плюс, но факт впечатляет'),
        'уран': ('https://korki.lol/wp-content/uploads/2017/10/uranus.jpg',
                 '#2E6BB0',
                 'Это же второй Нептун! Получается, мы сможем организовать 2 колонизации Нептуна',
                 'Любителям зимы здесь понравится! Ещё и мороженое можно взять',
                 '27 спутников! После этой колонизации мы выделим вам по спутнику!',
                 '7 планета от Солнца. 7 счастливое число, так что всё пройдёт на ура!'),
        'сатурн': ('https://korki.lol/wp-content/uploads/2017/10/saturn.jpg',
                   '#C7B293',
                   'Нищие координаторы с Нептуна привлекали Вас своими кольцами? ХА!',
                   '27 спутников? ХА! 62 — наше число!',
                   'Планета по составу похожа на Солнце. Никто не хочет подзагореть?',
                   'Все любят бассейны! Здесь почва имеет меньшую плотность, чем вода!')
    }
    if planet_name.lower() in planet_data.keys():
        info = planet_data[planet_name.lower()]
        return render_template('promote_planet.html',
                               title=f'Наш выбор: {planet_name}',
                               info=info)
    else:
        return render_template('promote_planet.html', title='Планета не найдена')


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def show_results(nickname, level, rating):
    return render_template('show_results.html', title='Ваш билет на Марс!',
                           rating=rating, level=level, nickname=nickname)


@app.route('/training/<prof>')
def training_scheme(prof: str):
    return render_template('profession_select.html', title=prof.capitalize(),
                           engineer_work=('инженер' in prof.lower()) or
                                         ('строитель' in prof.lower()))


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    if list_type in ('ul', 'ol'):
        return render_template('list_prof.html', list=list_type,
                               title='Список специальностей',
                               professions=PROF_LIST)
    else:
        return 'Неверный параметр списка'


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    if answer == {}:
        return redirect('/astronaut_selection')
    else:
        return render_template('auto_answer.html', title='Анкета', **answer)


@app.route('/login', methods=['POST', 'GET'])
def emergency_access():
    if request.method == 'GET':
        return render_template('emergency_access.html',
                               title='Аварийный доступ')
    else:
        return redirect('/index')


@app.route('/distribution')
def room_distribute():
    participants_list = ('Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                         'Венката Капур', 'Тедди Сандерс', 'Шон Бин')
    return render_template('room_distribute.html',
                           title='Расселение по каютам',
                           participants_list=participants_list)


@app.route('/')
@app.route('/index')
def work_journal():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)

    return render_template('works_journal.html', jobs=jobs)


def create_user(**kwargs):
    user = User()
    for arg_name in kwargs.keys():
        user.__setattr__(arg_name, kwargs[arg_name])
    return user


def create_job(**kwargs):
    job = Jobs()
    for arg_name in kwargs.keys():
        job.__setattr__(arg_name, kwargs[arg_name])
    return job


def initiate_users(db_sess):
    db_sess.add(create_user(**{'surname': 'Scott',
                               'name': 'Ridley',
                               'age': 21,
                               'position': 'captain',
                               'speciality': 'research engineer',
                               'address': 'module_1',
                               'email': 'scott_chief@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Stiles',
                               'name': 'Richard',
                               'age': 22,
                               'position': 'helper',
                               'speciality': 'general',
                               'address': 'module_3',
                               'email': 'stile_r@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Crowds',
                               'name': 'Scott',
                               'age': 23,
                               'position': 'junior captain',
                               'speciality': 'math',
                               'address': 'module_2',
                               'email': 'scotty_cr1998@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Canon',
                               'name': 'Pictures',
                               'age': 24,
                               'position': 'operator',
                               'speciality': 'cinema',
                               'address': 'module_7',
                               'email': 'canon_pict@mars.org'
                               }))

    db_sess.add(create_user(**{'surname': 'Ronan',
                               'name': 'Warwar',
                               'age': 25,
                               'position': 'warior',
                               'speciality': 'alien killer',
                               'address': 'module_1',
                               'email': 'kill_mars@mars.org'
                               }))


def initiate_jobs(db_sess):
    db_sess.add(create_job(**{'team_leader': 1,
                              'job': 'deployment of residential modules 1 '
                                     'and 2',
                              'work_size': 15,
                              'collaborators': '2, 3',
                              'start_date': dt.date.today(),
                              'is_finished': False
                              }))


def main():
    Jobs.__repr__ = lambda self: f'<Job> {self.job}'

    db_session.global_init(input())

    db_sess = db_session.create_session()

    jobs = map()

    '''initiate_users(db_sess)
    initiate_jobs(db_sess)'''


if __name__ == '__main__':
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
