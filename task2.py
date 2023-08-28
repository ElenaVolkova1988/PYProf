# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num  = int (input('Введите число: '))
min = 0
max = 100000
if min < num < max:
    if num % 2 ==0:
       print("Число является составным") 
    elif num % num == 0 and num % 1 == 0:
        print("Число является простым")
else :
    print ("Число не входит в данный диапазон")