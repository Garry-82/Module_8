def personal_sum(numbers):
    result = 0
    incoret_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError as TE:
            incoret_data = incoret_data + 1
    return (result, incoret_data)

def calculate_average(numbers):
    if type(numbers) in (list, tuple, set, str):
        for i in numbers:
            if type(i) != int and type(i) != bool:
                print(f'Некорректный тип данных для подсчета суммы - {i}')
        try:
            return personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
        except ZeroDivisionError:
            return 0

    else:
        print('В numbers записан некорректный тип данных')
        return None


print("Проверка 1 (пустой список). Результат: ", calculate_average([]))

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать