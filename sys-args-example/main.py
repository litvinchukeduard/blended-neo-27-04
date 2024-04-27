import sys

print()
print(sys.argv)
print()

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    print(f'File name {file_name}')
else:
    print('No arguments')

for argument in sys.argv:
    print(argument)
