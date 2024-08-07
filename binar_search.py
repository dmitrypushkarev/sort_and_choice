"""Функция для бинарного поиска"""


def bin_search(lst: list, text: int):
    """Бинарный поиск"""
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == text:
            return lst[mid]
        elif text < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return "Число не найдено!"


def in_out():
    """input - output"""
    import random
    text = int(input("Введите число: "))
    lst = sorted([random.randint(1, 100) for _ in range(100)])

    print(f'Число введено: {bin_search(lst, text)}')


if __name__ == '__main__':
    in_out()
