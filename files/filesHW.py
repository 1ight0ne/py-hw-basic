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

def concat_files(files_count, *files):
    if len(files) == files_count and files_count > 1:
        if not os.path.exists(os.getcwd() + '\\sorted'):
            return 'Ошибка! папка sorted не существует'
        os.chdir('sorted')
        files = list(map(lambda f: os.path.join(os.getcwd(), f), files))
        output_file = os.path.join(os.getcwd(), 'out_sorted.txt')
        files_to_dict = []
        for file in files:
            if not os.path.exists(file):
                return f'Ошибка! файл {file} не существует'
            with open(file, 'r', encoding='utf-8') as f:
                content = f.readlines()
            files_to_dict.append({'filename': os.path.basename(file), 'content': content, 'lines_count':len(content)})
        files_to_dict.sort(key=lambda e: e['lines_count'])
        with open(output_file, 'w', encoding='utf-8') as f:
            for file in files_to_dict:
                f.write(file['filename'] + '\n')
                f.write(str(file['lines_count']) + '\n')
                f.writelines(file['content'] )
        return 'Успех!'
    else:
        return f'Ошибка! указано неверное количество фалов'

if __name__ == '__main__':
    cook_book = read_cookbook()
    print(cook_book)
    pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Окрошка'], 5))
    print(concat_files(3,'1.txt', '2.txt', '3.txt'))