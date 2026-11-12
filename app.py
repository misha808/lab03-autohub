from flask import Flask, render_template, request

from data import CARS

app = Flask(__name__)

# Пункти меню в одному місці: (назва функції-маршруту, текст у меню).
# Меню в base.html будується циклом, тому нова сторінка = один рядок тут.
NAV_ITEMS = [
    ('home', 'Головна'),
    ('shop', 'Автомобілі'),
    ('about', 'Про нас'),
    ('contact', "Зворотний зв'язок"),
]


@app.context_processor
def inject_nav():
    """Робить змінні доступними в усіх шаблонах без передачі в render_template."""
    return {'nav_items': NAV_ITEMS, 'current': request.endpoint}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shop')
def shop():
    return render_template('shop.html', cars=CARS)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # debug=True: автоматичний перезапуск і детальні помилки. Лише для розробки.
    app.run(debug=True)
