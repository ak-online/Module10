import time
from datetime import datetime
from threading import Thread


count = 0

def write_file(file_name, text):
    file = open(file_name, 'a', encoding='utf-8')
    file.write(f'{text}\n')
    file.closed

def write_words(word_count, file_name):
    global count
    count +=1
    write_str = "Python " * word_count + "№"+str(count)
    write_file(file_name, write_str)
    time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')

time_start = datetime.now()

thr_first = Thread(target=write_words(10, 'example5.txt'))
thr_second = Thread(target=write_words(30, 'example6.txt'))
thr_third = Thread(target=write_words(200, 'example7.txt'))
thr_fourth = Thread(target=write_words(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')
