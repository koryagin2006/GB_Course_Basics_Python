# выводим одно слово
print('Hello')
# выводим несколько слов
print('Hello, world')
# выводим  любой набор символов
print('fexegsge $ sfegegw')
# выводим целое число
print(100)
# выводим число с плавающе точкой
print(90.89)
# выводим истину
print(True)
# выводим ложь
print(False)
# выводим None
print(None)

# строка целиком
print('Привет, меня зовут Кеша, мне 2 года')
name = 'Кеша'
age = 2
print(name, age)  # склеивание через пробел
print(name, age, sep='/')  # склеивание данных не через пробел, а через символ, указанный в sep
print(name, end=';')
print(age, end=';')
print('end')  # склеивание данных

# ввод данных
# 1. без параметров
'''
result = input()
print('Пользователь ввел',  result)'''
# 2. с параметром
name = input()
print('Меня зовут: ', name)
age = int(input('Сколько Вам лет?: '))
period = 20
print('Через ', period, 'лет Вам будет ', age + period)
