import time

# Прочитати числа
def read_numbers(file_path: str) -> set[int]:
    """
    Function to read numbers from file and return them as a set of ints

        - file_path: path to the file
    """
    with open(file_path, encoding='utf-8') as file:
        # print(file.readlines()[0])
        # file_text = file.read()
        # file_text.split('\n')
        numbers_set = set()
        for line in file:
            # print(line.replace('\n', ''))
            # cleaned_line = line.strip()
            # numbers = cleaned_line.split()
            numbers = line.strip().split() # Cleaning line from whitespace
            numbers_set = numbers_set | set(numbers)
        return numbers_set
 
# Посортувати числа
def sort_numbers(numbers_set: set[int]) -> list[int]:
    numbers_list = list(numbers_set)
    numbers_list.sort()
    # print(numbers_list.sort())
    # print(numbers_list)
    # print(sorted(numbers_list))
    return numbers_list

# Прибрати min та max
def remove_min_max_from_list(ordered_numbers: list[int]) -> list[int]:
    return ordered_numbers[1:-1]

def remove_min_max_from_list_unordered(numbers: list[int]) -> list[int]:
    start_time = time.time()
    # numbers.sort() # O(nlogn) # 18
    sorted_numbers = sorted(numbers)
    sorted_numbers[1:-1]
    end_time = time.time()
    print(f'O(nlogn): {(end_time - start_time):.20f}')
    # return ordered_numbers[1:-1] # 9
    # 1 2 3 4 5 6 7 8 9
    start_time = time.time()
    min_number = min(numbers) # 9
    max_number = max(numbers) # 9
    numbers.remove(min_number) # 9
    numbers.remove(max_number) # 8  O(2n)
    end_time = time.time()
    print(f'O(2n): {(end_time - start_time):.20f}')
    return numbers

# записати у інший файл
def write_numbers_to_file(numbers: list[int], file_path: str) -> list[int]:
    numbers_list_str = []
    for number in numbers:
        numbers_list_str.append(str(number))
    with open(file_path, 'w') as file:
        file.write(' '.join(numbers_list_str))

numbers_set_str = read_numbers('numbers-files/text.txt')
numbers_set = set() # {} dict()
for number in numbers_set_str:
    numbers_set.add(int(number))
numbers_list = remove_min_max_from_list(sort_numbers(numbers_set))
write_numbers_to_file(numbers_list, 'numbers-files/out.txt')

# print('        hello           '.strip())
# print(sort_numbers([1, 3, 1, 2]))

# lst = [1, 2, 3, 4, 5]
# print(lst[1:-1])

# print(remove_min_max_from_list_unordered([9, 8, 6, 7, 5, 3, 4, 1, 2]))