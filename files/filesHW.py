import os
from pprint import pprint

def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ingr_list = []
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ingr_list.append(ingrs)
            cook_book[dish_name] = ingr_list
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingrs in cook_book[dish_name]:
                if ingrs['ingredient_name'] not in result_dict:
                    result_dict[ingrs['ingredient_name']] = {'measure': ingrs['measure'], 'quantity': ingrs['quantity'] * person_count}
                else:
                    result_dict[ingrs['ingredient_name']]['quantity'] += ingrs['quantity'] * person_count
        else:
            print(f'Блюдо {dish_name} отсутствует в списке блюд.')
    return result_dict

if __name__ == '__main__':
    cook_book = read_cookbook()
    print(cook_book)
    pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Окрошка'], 5))