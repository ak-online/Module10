from threading import Thread
from random import randint
from time import sleep
from queue import Queue

class Table:
    def __init__(self, number):
        self.number  = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        #self.run()

    def run(self):
        awaiting = randint(3,10)
        sleep(awaiting)
        #print('run -', self.name )

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        free_t = len(self.tables)
        for guest in guests:
            if not free_t:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    guest.join()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            free_t -= 1

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in tables):
            for table in tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    guest.start()
                    guest.join()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
