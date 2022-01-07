import json

from Cats import Cat

with open('Pet_List.json', encoding='utf8') as f:
    templates = json.load(f)

print(templates)


def find_cat(item, el):
    if item[el]['code'] == 'cat':
        return True


for i in templates['results']:
    for j in i:
        if j == 'species' and find_cat(i, j):
            obj_cat = Cat(i['name'], i['gender']['name'], i['age'])
            print(obj_cat.name)
            print(obj_cat.gender)
            print(obj_cat.age)
        else:
            print(False)
