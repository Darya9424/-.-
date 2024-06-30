from pprint import pprint
cook_book = {}

with open('recepty.txt', encoding='utf-8') as file:

    for row in file:
        ingredients = []
        new_row = row.strip()
        count_ing = file.readline()
#print(count_ing)


        for n in range(int(count_ing)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, weight = recepie
            ingredients.append({'ingredient_name': product, 'quantity': int(quantity), 'measure': weight})
        file.readline()
        cook_book[new_row] = ingredients
#pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                                (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')

    return shop_list

#pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))



with open('1.txt', encoding='utf-8') as f1:
    text1 = f1.read()
with open('2.txt', encoding='utf-8') as f2:
    text2 = f2.read()
with open('3.txt', encoding='utf-8') as f3:
    text3 = f3.read()

def count_line_length(text):
    return len(text.split('\n'))

main_dict = {
    '1':{'file_name': '1.txt', 'text': text1},
    '2':{'file_name': '2.txt', 'text': text2},
    '3':{'file_name': '3.txt', 'text': text3}
            }
lengthes_list = []

for i in main_dict.values():
    (i['length']) = count_line_length(i['text'])
    lengthes_list.append(i['length'])

lengthes_list.sort()

def create_text():
    text_list = []
    position = 0
    for length in lengthes_list:
        for v in main_dict.values():
            if length == v['length']:
                position += 1
                text_list.append(v['file_name'])
                text_list.append(str(position))
                text_list.append(v['text'])
    return '\n'.join(text_list)

full_text = create_text()

with open('result.txt', 'w', encoding='utf-8') as f4:
    f4.write(full_text)


