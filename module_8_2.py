def personal_sum(numbers):
    result = 0
    len_ = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:
                result += i
                len_ += 1
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i}')


        return result, incorrect_data, len_
    except TypeError:
        return

def calculate_average(numbers):
    res = 0
    try:
        sum_result, incorrect_data, len_ = personal_sum(numbers)

        try:
            average = sum_result / len_
            return average
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None



# per = personal_sum("1, 2, 3")
# per = personal_sum([1, "Строка", 3, "Ещё Строка"])
# per = personal_sum(567)
# per = personal_sum([42, 15, 36, 13])
# print(per)


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average('42, 15')}')



