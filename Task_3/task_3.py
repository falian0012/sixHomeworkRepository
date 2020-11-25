class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        print(f'Full name is : {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income is : {int(self._income["wage"]) + int(self._income["bonus"])}')

pos = Position("Petr", "Ivanov", 'Someone', {"wage": 1000,
                                             "bonus": 2000})

pos.get_full_name()
pos.get_total_income()
