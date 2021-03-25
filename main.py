from flask import Flask, url_for, request, render_template

PROF_LIST = ('Инженер-исследователь',
             'Пилот', 'Строитель', 'Метеоролог',
             'Инженер по жизнеобеспечению',
             'Инженер по радиацинной защите',
             'Врач', 'Экзобиолог')

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index_default():
    return render_template('base.html', title='MarsOne')


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
    if request.method == 'GET':
        return render_template('register_unit.html', title='Отбор кандидатов')
    elif request.method == 'POST':
        print(request.form['name'])
        return 'Отправлено'


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
