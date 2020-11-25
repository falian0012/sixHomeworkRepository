class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки...'

class Pen(Stationery):

    def __init__(self, title='ручка'):
        super().__init__(title=title)

    def draw(self):
        print(f'{super().draw()} Рисуем {self.title}!')


class Pencil(Stationery):

    def __init__(self, title='карандаш'):
        super().__init__(title=title)

    def draw(self):
        print(f'{super().draw()} Рисуем {self.title}!')


class Handle(Stationery):

    def __init__(self, title='маркер'):
        super().__init__(title=title)

    def draw(self):
        print(f'{super().draw()} Рисуем {self.title}!')


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()