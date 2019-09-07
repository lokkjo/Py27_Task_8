# Задача 8-1

def form_cook_book():
    with open('recipes.txt', encoding='utf8') as f:
        cook_book = {}
        for line in f:
            cb_key = line.strip()
            ing_num = f.readline().strip()
            counter = int(ing_num)
            dish_list = []
            while counter > 0:
                ing_data = list(f.readline().split(' | '))
                ing_dict = {
                    'ingredient_name': ing_data[0],
                    'quantity': int(ing_data[1]),
                    'measure': ing_data[2].rstrip(),
                }
                dish_list.append(ing_dict)
                counter -= 1
            cook_book[cb_key] = dish_list
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = form_cook_book()
    shop_list = {}
    for course in cook_book:
        if course in dishes:
            for item in cook_book[course]:
                if shop_list.get(item['ingredient_name']) is None:
                    shop_list[item['ingredient_name']] = {
                                    'measure': item['measure'],
                                    'quantity': item['quantity']
                                                *person_count
                    }
                else:
                    shop_list[item['ingredient_name']]['quantity'] = (
                        shop_list[item['ingredient_name']]
                        ['quantity'] + item['quantity']
                        * person_count)
    return shop_list

cook_book = form_cook_book()
shop_list = get_shop_list_by_dishes(['Запеченный картофель',
                                     'Омлет', 'Кофе с молоком',
                                     'Бургер'], 2)

print(f'\nРешение задачи 1: Словарь с рецептами\n\n {cook_book}')
print(f'\nРешение задачи 2: Список покупок\n\n {shop_list}')

# Проверка повторяющихся ингредиентов - по ингредиенту 'Помидор'