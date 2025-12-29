# lesson_3_task_3.py

from address import Address
from mailing import Mailing

# Создаем адреса отправителя и получателя
to_addr = Address("123456", "Москва", "Ленинский проспект", "10а", "12")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "5", "45")

# Создаем отправление
mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=250, track="AB123456789RU")

# Распечатываем информацию
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
