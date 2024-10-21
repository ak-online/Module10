import threading
import random
import time
from threading import Lock


class Bank:

    def __init__(self):
        self.balance: int = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            added_funds = random.randrange(50, 500)
            time.sleep(0.01)
            self.balance += added_funds
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {added_funds}. Баланс: {self.balance}' + '\n')

    def take(self):
        for i in range(100):
            withdrawn_funds = random.randrange(50, 500)
            print(f'Запрос на: {withdrawn_funds} ')
            time.sleep(0.01)
            if withdrawn_funds > self.balance:
                print(f'Запрос отклонён, недостаточно средств: {withdrawn_funds}. Баланс: {self.balance}' + '\n')
                self.lock.acquire()
            elif withdrawn_funds <= self.balance:
                self.balance -= withdrawn_funds
                print(f'Снятие: {withdrawn_funds}. Баланс: {self.balance} ' )


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
