"""
Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. 
В результирующем списке
не должно быть дубликатов.
"""  


list_one = [1, 1, 1, 2, 3, 4, 5, 4, 6, 7, 7, 'test', 'test', 'bk', 9, 9]
list_result = []

for i in list_one:
    count = 0
    for j in list_one:
        if i == j:
            count += 1
            if count > 1 and not list_result.count(i):
                list_result.append(i)
                count = 0

print(list_result)

