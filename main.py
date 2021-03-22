from flask import Flask, url_for, request, render_template

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
    return f'''
    <head>
        <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
        <link rel="stylesheet"
            href="{url_for('static', filename='css/style.css')}">
        <title>Выбирай Марс!</title>
        
        <style>
            h1 {"{"}
                color: red;
            {"}"}
        </style>
    </head>
    <body>
        <h1>Жди нас, Марс</h1>
        <img src="{url_for('static', filename='img/mars.png')}" alt="Красивая картинка Марса"
            width=200 height=200>
        
        <div class="alert alert-dark" role="alert">
            Человечество вырастает из детства
        </div>
        <div class="alert alert-success" role="alert">
            Человечеству мала планета
        </div>
        <div class="alert alert-dark" role="alert">
             Мы сделаем обитаемыми безжизненные планеты
        </div>
        <div class="alert alert-warning" role="alert">
            И начнём с Марса!
        </div>
        <div class="alert alert-danger" role="alert">
            Присоединяйся!
        </div>
    </body>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def register_unit():
    if request.method == 'GET':
        return f'''	<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
        <link rel="stylesheet" href={url_for('static', filename='css/style.css')}>
        <title>Отбор кандидатов</title>
    </head>
    <body>
    <h1 align="center">Анкета претендента</h1>
    <h3 align="center">на участие в миссии</h3>
    <form class="login_form" method="post" enctype="multipart/form-data">
        <div class="row g-2">
            <div class="col-6">
                <input type="text" class="form-control" placeholder="Фамилия">
            </div>
            <div class="col-6">
                <input type="text" class="form-control" placeholder="Имя">
            </div>
            <div class="col-12">
                <label>Какое у вас образование?</label>
                <select class="form-select">
                    <option>Начальное</option>
                    <option selected>Среднее</option>
                    <option>Высшее</option>
                </select>
            </div>
            <div class="col-12">
                <label>Какими профессиями вы владеете?</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec1" value="Инженер-исследователь"></input>
                <label class="form-check-label" for="spec1">Инженер-исследователь</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec2" value="Пилот"></input>
                <label class="form-check-label" for="spec2">Пилот</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec3" value="Строитель"></input>
                <label class="form-check-label" for="spec3">Строитель</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec4" value="Метеоролог"></input>
                <label class="form-check-label" for="spec4">Метеоролог</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec5" value="Инженер по жизнеобеспечению"></input>
                <label class="form-check-label" for="spec5">Инженер по жизнеобеспечению</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec6" value="Инженер по радиацинной защите"></input>
                <label class="form-check-label" for="spec6">Инженер по радиацинной защите</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec7" value="Врач"></input>
                <label class="form-check-label" for="spec7">Врач</label>
                <br>

                <input class="form-check-input" type="checkbox" name="speciality"
                    id="spec8" value="Экзобиолог"></input>
                <label class="form-check-label" for="spec8">Экзобиолог</label>
                <br>
            </div>
            <div class="col-12">
                <label>Укажите ваш пол</label>
                <br>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="gender" id="male" value="male"></input>
                    <label class="form-check-label" for="male">Мужской</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="gender" id="female" value="female"></input>
                    <label class="form-check-label" for="female">Женский</label>
                </div>
            </div>
            <div class="col-12">
                <label>Почему вы хотите принять участие в миссии?</label>
                <textarea cols=50></textarea>
            </div>
            <div class="col-12">
                <label>Приложите фотографию</label>
                <input type="file" accept="image/*"></input>
            </div>
            <div class="col-12">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="yes" id="areyouready"></input>
                <label class="form-check-label" for="areyouready">Готовы ли остаться на Марсе?</label>
            </div>
            </div> 
            <div class="col-12">
                <button type="submit" class="btn btn-primary">Отправить</button>
            </div>
            </div>
        </form>
    </body>
</html>'''
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
        return f'''<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
    <title>Наш выбор: {planet_name}</title>
</head>
<body>
<div class="row g-2">
    <div class="col-12">
        <h1 style="color: {info[1]};" align="center">Жди нас, {planet_name}!</h1>
    </div>

    <div class="col-7">
    <img src="{info[0]}" alt="Марс"
        style="margin-left: 10%">
    </div>

    <div class="col-5 align-self-center">
    <div class="alert alert-primary" role="alert">
        {info[2]}
    </div>
    <div class="alert alert-success" role="alert">
        {info[3]}
    </div>
    <div class="alert alert-danger" role="alert">
        {info[4]}
    </div>
    <div class="alert alert-dark" role="alert">
        {info[5]}
    </div>
    </div>
</div>
</body>
</html>'''
    else:
        return '''<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
    <title>Планета не найдена</title>
</head>
<body>
    Увы, на эту планету мы переезжать не планируем. 
    <br>
    <a href="/choice/Марс" class="btn btn-outline-danger" role="button">Перейти к Марсу</a>
</body>
</html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def show_results(nickname, level, rating):
    return render_template('show_results.html', title='Ваш билет на Марс!',
                           rating=rating, level=level, nickname=nickname)


@app.route('/training/<prof>')
def training_scheme(prof: str):
    return render_template('profession_select.html', title=prof.capitalize(),
                           engineer_work=('инженер' in prof.lower()) or
                                         ('строитель' in prof.lower()))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
