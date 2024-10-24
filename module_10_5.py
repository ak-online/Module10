import multiprocessing
import os
import datetime


def read_info(name):
    all_data = []
    with open(name, "r") as f:
        for lines in f:
            lines = f.readlines()
            all_data.append(lines)


if __name__ == '__main__':

    filenames = [f'./file{number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = datetime.datetime.now()
    for name in filenames:
        read_info(name)
    end = datetime.datetime.now()
    print(f'Время выполнения {end - start}')

    # Многопроцессный
    start = datetime.datetime.now()
    # print(os.cpu_count())
    # with multiprocessing.Pool(processes=os.cpu_count()) as pool:
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'Время выполнения {end - start}')
