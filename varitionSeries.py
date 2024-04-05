# нахождение повторящиюся чисел
def find_most_frequent_number(numbers):
    numbers.sort()
    max_count = 0
    current_count = 1
    most_frequent_numbers = []
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_frequent_numbers = [numbers[i - 1]]
            elif current_count == max_count:
                most_frequent_numbers.append(numbers[i - 1])
            current_count = 1
    if current_count > max_count:
        most_frequent_numbers = [numbers[-1]]
    elif current_count == max_count:
        most_frequent_numbers.append(numbers[-1])

    return most_frequent_numbers


# нахождение медианы
def find_median(sorted_list):
    length = len(sorted_list)
    if length % 2 == 0:
        mid = length // 2
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        mid = length // 2
        median = sorted_list[mid]

    return median

# основная функция
def variationSeries():
    row = input("Введите числа разделяя пробелами: ")
    if tuple(row) == int:
        numbers_list = [int(num) for num in row.split()]
        numbers_list.sort()
        print(f"Варяционный ряд: {numbers_list}")
        middle = sum(numbers_list) / len(numbers_list)
        print(f"Средняя величина: {middle}")
        if numbers_list == find_most_frequent_number(numbers_list):
            print(f"Мода: --")
        else:
            print(f"Мода: {find_most_frequent_number(numbers_list)}")
        print(f"Медиана: {find_median(numbers_list)}")
        max_num = max(numbers_list)
        min_num = min(numbers_list)
        print(f"Размах: {max_num - min_num}")
    elif tuple(row) == float:
        numbers_list_float = [float(num) for num in row.split()]
        numbers_list_float.sort()
        print(f"Варяционный ряд: {numbers_list_float}")
        middle = sum(numbers_list_float) / len(numbers_list_float)
        print(f"Средняя величина: {middle}")
        if numbers_list_float == find_most_frequent_number(numbers_list_float):
            print(f"Мода: --")
        else:
            print(f"Мода: {find_most_frequent_number(numbers_list_float)}")
        print(f"Медиана: {find_median(numbers_list_float)}")
        max_num = max(numbers_list_float)
        min_num = min(numbers_list_float)
        print(f"Размах: {max_num - min_num}")
    else:
        print("Введите пожалуйста положительные натуральные числа или десятичные положительные числа ")

variationSeries()
