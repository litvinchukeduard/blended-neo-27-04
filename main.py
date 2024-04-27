from colorama import Fore, Back, Style
# Додаток, який слідкує за продуктами в супермаркеті
# Має вміти додати товар, видалити товар та вивести увесь товар

# https://pypi.org/project/colorama/
# https://github.com/vinta/awesome-python
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Welcome!

# Ctrl C in terminal to stop application

banner = """


  (`\ .-') /`   ('-.                                  _   .-')       ('-.  ,---. 
   `.( OO ),' _(  OO)                                ( '.( OO )_   _(  OO) |   | 
,--./  .--.  (,------.,--.       .-----.  .-'),-----. ,--.   ,--.)(,------.|   | 
|      |  |   |  .---'|  |.-')  '  .--./ ( OO'  .-.  '|   `.'   |  |  .---'|   | 
|  |   |  |,  |  |    |  | OO ) |  |('-. /   |  | |  ||         |  |  |    |   | 
|  |.'.|  |_)(|  '--. |  |`-' |/_) |OO  )\_) |  |\|  ||  |'.'|  | (|  '--. |  .' 
|         |   |  .--'(|  '---.'||  |`-'|   \ |  | |  ||  |   |  |  |  .--' `--'  
|   ,'.   |   |  `---.|      |(_'  '--'\    `'  '-'  '|  |   |  |  |  `---..--.  
'--'   '--'   `------'`------'   `-----'      `-----' `--'   `--'  `------''--'  


"""

# add-product Yogurt 1
# delete-product Yogurt
# all

# colorama

# pipenv poetry

def main():
    products = dict() # 'Product name' -> quantity 1
    while True:
        user_input = input(">>> ") # add-product Yogurt 1
        command, *args = user_input.strip().split() # ['add-product', 'Yogurt', '1']
        # print(command, args)

        if command == 'add-product':
            product_name, quantity = args
            if product_name in products:
                products[product_name] += int(quantity)
            else:
                products[product_name] = int(quantity)
            print(Fore.GREEN + 'Product added' + Style.RESET_ALL)
        elif command == 'delete-product':
            product_name, = args # ['Yogurt'] product_name = args[0]
            del products[product_name]
            print(f'Product with name {product_name} deleted successfuly')
        elif command == 'all':
            print(products)
        elif command == 'exit':
            print(Fore.BLUE + Back.GREEN + "Have a nice day!" + Style.RESET_ALL)
            break


if __name__ == '__main__':
    print(banner)
    print('App to track supermarket inventory')
    print(Fore.RED + '\t1. Use "add-product" to add a product to inventory' + Style.RESET_ALL)
    print(Fore.GREEN + '\t2. Use "delete-product" to delete product from inventory' + Style.RESET_ALL)
    print(Fore.BLUE + '\t3. Use "all" to view all inventory' + Style.RESET_ALL)
    main()
