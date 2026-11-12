from urllib.parse import quote


def commons_photo(filename, width=800):
    """Посилання на фото з Wikimedia Commons (вільні ліцензії) за назвою файлу."""
    return f'https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}?width={width}'


# Каталог автомобілів для сторінки «Автомобілі» (заповнює учасник 2).
CARS = []
