"""
Создайте словарь со списком 
вещей для похода в качестве ключа 
и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак 
передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. 
"""


def find_items_for_backpack(max_weight):
    items = {
        'спальник': 2,
        'палатка': 4,
        'еда': 1,
        'вода': 3,
        'фонарик': 0.5,
        'топор': 1.5
    }

    backpack_items = {}

    for item, weight in items.items():
        if weight <= max_weight:
            backpack_items[item] = weight
            max_weight -= weight

        if max_weight == 0:
            break

    return backpack_items

max_weight = 7
backpack_items = find_items_for_backpack(max_weight)
print(backpack_items)

