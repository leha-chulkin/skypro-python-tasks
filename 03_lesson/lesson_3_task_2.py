# lesson_3_task_2.py

from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S22", "+79876543210"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79265554433"),
    Smartphone("OnePlus", "9 Pro", "+79001234567"),
    Smartphone("Google", "Pixel 6", "+79107987654")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")