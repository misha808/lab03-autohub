from urllib.parse import quote


def commons_photo(filename, width=800):
    """Посилання на фото з Wikimedia Commons (вільні ліцензії) за назвою файлу."""
    return f'https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}?width={width}'


# Каталог автомобілів для сторінки «Автомобілі».
CARS = [
    {'name': 'Toyota Camry', 'photo': commons_photo('2020 Toyota Camry XSE front.jpg'), 'year': 2021, 'fuel': 'Бензин', 'price': 24500, 'tag': 'Седан'},
    {'name': 'Volkswagen Golf', 'photo': commons_photo('Volkswagen Golf VIII IMG 9737.jpg'), 'year': 2020, 'fuel': 'Дизель', 'price': 17900, 'tag': 'Хетчбек'},
    {'name': 'Tesla Model 3', 'photo': commons_photo('Tesla Model 3 (2023) IMG 9488.jpg'), 'year': 2022, 'fuel': 'Електро', 'price': 31900, 'tag': 'Електромобіль'},
    {'name': 'BMW X5', 'photo': commons_photo('BMW X5 (G05) China.jpg'), 'year': 2019, 'fuel': 'Дизель', 'price': 38500, 'tag': 'Позашляховик'},
    {'name': 'Skoda Octavia', 'photo': commons_photo('Skoda Octavia IV liftback.jpg'), 'year': 2021, 'fuel': 'Бензин', 'price': 19800, 'tag': 'Ліфтбек'},
    {'name': 'Ford Transit', 'photo': commons_photo('Ford Transit T8 002.jpg'), 'year': 2018, 'fuel': 'Дизель', 'price': 15700, 'tag': 'Мінівен'},
]
