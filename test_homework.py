import math
import random


def test_greeting():
    name = "Анна"
    age = 25

    # Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Выводим результат на экран
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20

    # Расчет периметра
    perimeter = 2 * (a + b)

    assert perimeter == 60

    # Расчет площади
    area = a * b

    assert area == 200


def test_circle():
    r = 23

    # Расчёт площади круга
    area = math.pi * r ** 2

    # Расчёт длины окружности
    length = 2 * math.pi * r
    print("Площадь круга:", area)
    print("Длина окружности:", length)


def test_random_list():
    # Создаем список из 10 случайных чисел от 1 до 100
    l = [random.randint(1, 100) for _ in range(10)]

    # Сортируем список по возрастанию
    l.sort()

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
