# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT) 
print ("Число загаданное программой :", num)

while count > 0:
    print ("Попытка" , count)
    count -=1
    
    my_num = int (input( "Введите число : "))
    if my_num > num:
        print ("Число загаданное мной меньше")
    if my_num < num:
        print ("Число загаданное мной больше")
    if my_num == num:
        print ("Вы угадали!")
else:
    print ("Все попытки исчерпаны")