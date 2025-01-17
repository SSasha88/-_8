print('Задача "Некорректность"')
print()
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
class Car:
    def __init__(self, model, vin_number, car_numbers):
        # Проверка вин-номера
        if not self._is_valid_vin(vin_number):
            raise IncorrectVinNumber(self._get_vin_error_message(vin_number))
        # Проверка регистрационных номеров
        if not self._is_valid_numbers(car_numbers):
            raise IncorrectCarNumbers(self._get_car_numbers_error_message(car_numbers))
        # Если все проверки прошли успешно, сохраняем данные
        self.model = model
        self._vin = vin_number
        self._numbers = car_numbers
    def get_vin(self):
        return self._vin
    def get_numbers(self):
        return self._numbers
    def _is_valid_vin(self, vin_number):
        # Проверка типа данных
        if not isinstance(vin_number, int):
            return False
        # Проверка диапазона значений
        if not (1000000 <= vin_number <= 9999999):
            return False
        return True
    def _is_valid_numbers(self, numbers):
        # Проверка типа данных
        if not isinstance(numbers, str):
            return False
        # Проверка длины строки
        if len(numbers) != 6:
            return False
        return True
    def _get_vin_error_message(self, vin_number):
        return 'Некорректный тип vin номер' if not isinstance(vin_number, int) else 'Неверный диапазон для vin номера'
    def _get_car_numbers_error_message(self, numbers):
        return 'Некорректный тип данных для номеров' if not isinstance(numbers, str) else 'Неверная длина номера'

# Пример выполняемого кода:
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")


try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{second.model} успешно создан")


try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{third.model} успешно создан")