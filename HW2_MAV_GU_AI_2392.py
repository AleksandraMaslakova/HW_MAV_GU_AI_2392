###################################################################################
# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
###################################################################################
list1 = [1, '2', 'three', 4, (5,6,7), 8.9, '10', {11:12}, True, [14, '15']]
for a in list1:
    print(type(a))

###################################################################################
# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().
###################################################################################

input_list = ['a', '1', 'b', '2', 'c', '3', 'd']
new_list = []
for i, value in enumerate(input_list): #i-шаг, value - значение ячейки(????)
    if i % 2 == 0: 
        #print(i) #0,2,4,6
        if i < len(input_list) - 1:
            #print (i) #0, 2, 4
            new_list.append(input_list[i+1])
            #print(input_list[i+1]) #1,2,3
        new_list.append(value)
        #print(value) #a, b, c, d
print(new_list)
#Пыталась разобраться самостоятельно, но все равно не могу понять принцип действия в цикле. Буду рада за помощь в разъяснении...



###################################################################################
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и dict.
###################################################################################

# словарь времен года
month_num = int(input('Введите номер месяца: '))
seasons_dict = { 12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
    9: 'Осень', 10: 'Осень', 11: 'Осень'}
print('По календарю этот месяц: ', seasons_dict.setdefault(month_num))

# лист времен года
num = input('Введите номер месяца: ')
months_str = ['зима' for x in range(2)]+  ['весна' for x in range(3)] + ['лето' for x in range(3)] + ['осень' for x in range(3)]  + ['зима']
for i in range(12):
    (i+1, months_str[i])
    if months_str[i] == num : 
        print(months_str[i])
    else :  
        break
#  Не могу понять как сделать так, чтобы выводилось нужное время года после прогона...

############################################################################################################
#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
#Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
#Если в слово длинное, выводить только первые 10 букв в слове.
############################################################################################################

inputStr = [ word for word in input('Введите слова через пробел: ').split()]
for ind, word in enumerate(inputStr):
    print(ind, word[:10])
    

############################################################################################################
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, 
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
############################################################################################################


my_list = [7, 5, 3, 3, 2]
user_val = int(input('Ведите место в рейтинге: '))
# Проверяем есть ли элемент в списке
if user_val in my_list:
    i = my_list.index(user_val) # индекс со значением ввода
    #print (my_list.index(user_val))
    count = my_list.count(user_val) # количество элементов со значением ввода
    #print (my_list.count(user_val))
    my_list.insert(i + count, user_val) # присваивание значение по индексу, например, 7=индекс 0 и введенное число тоже 7, т.к. 
# количество элементов со значением 7 будет 1, то место в листе присвоится 0+1=>[7,7,5,3,3,2]
else: # если введенное значение отсутствует в листе
    my_list.append(user_val) # помещаем элеммент в конец листа
    my_list.sort(reverse=True) # выполняем сортировку в порядке убывания, если бы стояло reverse=False, то сортировка была бы в порядке возрастания

print(my_list) 

