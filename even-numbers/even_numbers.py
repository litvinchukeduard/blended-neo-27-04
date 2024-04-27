

def even_numbers_from_file(file_path: str) -> list[int]:
    even_numbers_list = []
    file = open(file_path, encoding='utf-8')
    for number in file.read().split():
        if int(number) % 2 == 0:
            even_numbers_list.append(number)
    file.close()
    return even_numbers_list

print(even_numbers_from_file('even-numbers/text.txt'))

# map(lambda number: int(number), )

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \n
# 0 9 46 4

my_str = "1aaa2aaa3aaa4"
# print(list(map(lambda number: int(number), my_str.split('aaa'))))
# print(list(filter(lambda number: int(number) % 2 == 0, my_str.split('aaa'))))
# sum = 0
# for number in my_str.split('aaa'):
#     sum += int(number)

# print(sum)