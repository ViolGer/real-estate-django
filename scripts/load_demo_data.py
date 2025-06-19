from listings.models import Property
from django.core.files import File
from pathlib import Path

# ⚠️ Убедись, что путь media/property_images/ существует
image_folder = Path("media/property_images")

demo_properties = [
    {
        "title": "Просторный лофт в Барселоне",
        "description": "Уютный лофт с панорамными окнами и видом на город.",
        "price": 480000,
        "currency": "EUR",
        "area": 85,
        "city": "Барселона",
        "country": "Испания",
        "image": "loft_barcelona.jpg"
    },
    {
        "title": "Вилла с бассейном в Тоскане",
        "description": "Роскошная вилла с садом, винным погребом и бассейном.",
        "price": 950000,
        "currency": "EUR",
        "area": 230,
        "city": "Флоренция",
        "country": "Италия",
        "image": "villa_tuscany.jpg"
    },
    {
        "title": "Апартаменты в центре Нью-Йорка",
        "description": "Современные апартаменты с видом на Манхэттен и фитнес-залом.",
        "price": 1200000,
        "currency": "USD",
        "area": 110,
        "city": "Нью-Йорк",
        "country": "США",
        "image": "nyc_apartment.jpg"
    },
    {
        "title": "Дом с панорамными окнами в Цюрихе",
        "description": "Минималистичный дизайн, гараж и камин.",
        "price": 870000,
        "currency": "CHF",
        "area": 150,
        "city": "Цюрих",
        "country": "Швейцария",
        "image": "zurich_home.jpg"
    },
    {
        "title": "Пентхаус с видом на море в Дубае",
        "description": "Интерьер в стиле хай-тек, терраса и джакузи.",
        "price": 2100000,
        "currency": "AED",
        "area": 190,
        "city": "Дубай",
        "country": "ОАЭ",
        "image": "dubai_penthouse.jpg"
    },
    {
        "title": "Таунхаус в Тбилиси",
        "description": "Просторный таунхаус в зелёном районе, с террасой.",
        "price": 320000,
        "currency": "USD",
        "area": 140,
        "city": "Тбилиси",
        "country": "Грузия",
        "image": "tbilisi_townhouse.jpg"
    },
    {
        "title": "Квартира в Бангкоке",
        "description": "Апартаменты в современном жилом комплексе с бассейном.",
        "price": 270000,
        "currency": "THB",
        "area": 95,
        "city": "Бангкок",
        "country": "Таиланд",
        "image": "bangkok_flat.jpg"
    },
    {
        "title": "Шале в Альпах",
        "description": "Аутентичное шале с камином и видом на горы.",
        "price": 750000,
        "currency": "EUR",
        "area": 160,
        "city": "Шамони",
        "country": "Франция",
        "image": "chamonix_chalet.jpg"
    },
    {
        "title": "Скандинавский дом у озера",
        "description": "Экологичный дом с сауной и панорамным остеклением.",
        "price": 540000,
        "currency": "EUR",
        "area": 130,
        "city": "Хельсинки",
        "country": "Финляндия",
        "image": "helsinki_lakehouse.jpg"
    },
    {
        "title": "Мини-дом в Лиссабоне",
        "description": "Компактный домик для сдачи в аренду в историческом центре.",
        "price": 260000,
        "currency": "EUR",
        "area": 50,
        "city": "Лиссабон",
        "country": "Португалия",
        "image": "lisbon_microhome.jpg"
    },
]

for data in demo_properties:
    p = Property(
        title=data["title"],
        description=data["description"],
        price=data["price"],
        currency=data["currency"],
        area=data["area"],
        city=data["city"],
        country=data["country"],
        is_available=True,
    )

    image_path = image_folder / data["image"]
    if image_path.exists():
        with open(image_path, "rb") as img:
            p.image.save(data["image"], File(img), save=False)

    p.save()

print("✅ Готово: добавлены 10 объектов.")
