print('Домашнее задание по уроку "Try и Except"')
print()
def add_everything_up(a, b):
    try:
        # Предполагаю, что a и b могут быть сложены без проблем
        result = a + b

        # Если сложение прошло успешно, возвращаю результат
        return result

    except TypeError:
        # Если произошло исключение TypeError, значит типы a и b различны
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
