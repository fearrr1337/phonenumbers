import phonenumbers
from phonenumbers import  geocoder, carrier, timezone

ru_number = '+79025645649'

ready_number = ru_number

parsed_number = phonenumbers.parse(ready_number, None)
print(f'Валидный ли номер: {phonenumbers.is_valid_number(parsed_number)}')
print(f'Cтрана: {geocoder.description_for_number(parsed_number, 'ru')}')
print(f'Часовой пояс: {timezone.time_zones_for_number(parsed_number)}')
print(f'Опреатор: {carrier.name_for_number(parsed_number, 'ru')}')