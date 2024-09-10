from flask import Flask, request, render_template
import math

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/home', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            c = int(request.form['c'])
        except ValueError:
            result = "Некорректный ввод данных. Введите целые числа."
            return render_template("base.html", result=result)

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            result = 'У этого уравнения нет корней'
        elif discriminant == 0:
            x = -b / (2 * a)
            result = f'Уравнение имеет один корень: {x}'
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            result = f'Уравнение имеет два корня: {x1} и {x2}'

    return render_template("base.html", result=result)