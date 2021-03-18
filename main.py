from flask import Flask, url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
