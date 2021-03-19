from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
