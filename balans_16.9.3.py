class Client:
    def __init__(self, name, surname, prihod, rashod):
        self.name = name
        self.surname =surname
        self.prihod = sum(prihod)
        self.rashod = sum(rashod)

    def get_balanse(self):
        return self.prihod - self.rashod

    def __str__(self):
        return f'Клиент - {self.name} {self.surname}, ,баланс - {self.get_balanse()}'


clients = [
              {'name': 'Иван', 'surname': 'Соболев', 'prihod': {50, 20, 35}, 'rashod': {25, 30}},
              {'name': 'Джон','surname': 'Кукушкин', 'prihod': {45, 60, 70}, 'rashod': {100, 10}},
              {'name': 'Александр','surname': 'Гаврилов', 'prihod': {5, 80,}, 'rashod': {45, 10}}
          ]

for client in clients:
    obj_client = Client(client['name'], client['surname'], client['prihod'], client['rashod'])
    print(obj_client)


