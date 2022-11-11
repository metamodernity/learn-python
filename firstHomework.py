#1) Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
#2) Выведите все нечетные элементы списка, используя функцию range().
#2) Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, не функцию range!
#3) Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента. Можно вывести их пару, главное обозначить вывод.
#4) Дан список чисел. Если в нем есть два соседних элемента одного знака (положительные или отрицательные), выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
#5) Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
#6) Программа получает на вход список, затем число k. Удалить данный элемент с индексом k из списка. Затем удалите последний элемент из списка. Можно использовать встроенные функции, которые есть у списка.
#7) Программа получает на вход список, затем число k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k. НЕ ИСПОЛЬЗУЯ ВСТРОЕННЫЕ ФУНКЦИИ СПИСКА.
#8) Сгенерируйте список, состоящий из 25 элементов и выведите каждый элемент отдельно на экран.
#9) Сгенерируйте список, состоящий из 1000 элементов и выведите на экран его длину.
#10) Сгенерируйте список, состоящий из 10000 элементов и выведите на экран сумму всех чисел и его длину с помощью функции len()
import random
flag = 1
def taskOne():
    print('#1')
    a = []
    b = []
    for i in range(10):
        a.append(random.randint(1, 10))
        if i % 2 == 0:
            b.append(f'A[{i}]:{a[i]}')
    print('Изначальный список:', a)
    print('элементы списка с четными индексами:', b)
def taskTwo_One(): #Честно не понял как использовать range в этой задаче
    print('#2.1')
    a = []
    for i in range(10):
        a.append(random.randint(1, 10))
    print('Изначальный список:', a)
    b = []
    for i in a:
        if i % 2 == 1:
            b.append(i)
    print('Все нечётные элементы списка:', b)
def taskTwo_Two():
    print('#2.2')
    a = []
    for i in range(10):
        a.append(random.randint(1, 10))
    print('Изначальный список:', a)
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    print('Все чётные элементы списка:', b)
def taskThree():
    print('#3')
    a = []
    b = []
    for i in range(10):
        a.append(random.randint(1, 10))
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            b.append(a[i + 1])
    print(a)
    print(b)
def taskFour():
    a = []
    b = []
    for i in range(10):
        a.append(random.randint(-10, 10))
    for i in range(len(a) - 1):
        if (a[i] > 0 and a[i + 1] > 0) or (a[i] < 0 and a[i + 1] < 0):
            b.append([a[i], a[i + 1]])
    print('Изначальный список:', a)
    print('Пары элементов одного знака', b)
def taskFive():
    print('#5')
    a = []
    for i in range(10):
        a.append(random.randint(1, 10))
    max_number = max(a)
    index = a.index(max(a))
    print(a)
    print("Наибольшее число в списке:", max_number, '\nЕго индекс:', index)
def taskSix():
    print('#6')
    a = []
    b = []
    num = int(input('Введите длину списка: '))
    while num > 0:
        element = int(input('Введите элемент списка: '))
        a.append(element)
        num -= 1
    k = int(input('Введите число k: '))
    for i in a:
        if i != a[k]:
            b.append(i)
    b = b[:-1]
    print(a)
    print(b)
def taskSeven():
    print('#7')
    a = []
    b = []
    num = int(input('Введите длину списка: '))
    while num > 0:
        element = int(input('Введите элемент списка: '))
        a.append(element)
        num -= 1
    k = int(input('Введите число k: '))
    for i in a:
        if i != a[k]:
            b.append(i)
    print(a)
    print(b)
def taskEight():
    print('#8')
    a = []
    count = 0
    while count < 25:
        a.append(random.randint(1, 10))
        count += 1
    for i in a:
        print(i)
    print('Список: ', a)
    print('Длина списка: ', len(a))
def taskNine():
    print('#9')
    a = []
    count = 0
    while count < 1000:
        a.append(random.randint(1, 10))
        count += 1
    print('Длина списка: ', len(a))
def taskTen():
    print('#10')
    a = []
    sum = 0
    for i in range(10000):
        a.append(random.randint(1, 10))
    for i in a:
        sum += i
    print('Сумма всех элементов списка:',sum, '\n' 'Длина списка:', len(a))
if __name__ == '__main__':
    while flag == 1:
        answer = int(input('Введите номер задачи: '))
        if answer == 1:
            taskOne()
        if answer == 2:
            specialAnswer = int(input('Какую из двух (1 или 2): '))
            if specialAnswer == 1:
                taskTwo_One()
            if specialAnswer == 2:
                taskTwo_Two()
        if answer == 3:
            taskThree()
        if answer == 4:
            taskFour()
        if answer == 5:
            taskFive()
        if answer == 6:
            taskSix()
        if answer == 7:
            taskSeven()
        if answer == 8:
            taskEight()
        if answer == 9:
            taskNine()
        if answer == 10:
            taskTen()
