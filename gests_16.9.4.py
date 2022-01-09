class Volonter:
    def __init__(self, name='', city='', tel_number=0):
        self.name = name
        self.city = city
        self.tel_number = tel_number


class Gest(Volonter):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status

    def get_gest(self):
        return f' {self.name}, г. {self.city}, статус {self.status}'


persons = [
    {'name': 'Иван Петров',
     'city': 'Москва',
     'tel_number': 37529856321,
     'position': 'волонтер',
     'status': 'Наставник'
     },
    {'name': 'Андрей Сидоров',
     'city': 'Минск',
     'tel_number': 856235899,
     'position': 'сотрудник',
     'status': 'Ученик'
     },
    {'name': 'Мария Иванова',
     'city': 'Санкт-Петербург',
     'tel_number': 75658969321,
     'position': 'волонтер',
     'status': 'Ментор'}
]

print('Список гостей :')
for person in persons:
    for n in person:
        if n == 'position' and person['position'] == 'волонтер':
            obj_gest = Gest(person['name'], person['city'], person['status'])
            print(obj_gest.get_gest())



