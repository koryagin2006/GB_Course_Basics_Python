# Математические операции
# Средняя продолжительность жизниы в России
ale = 71
age = int(input('Сколько Ва лет?: '))

after20 = age + 20
print('Через 20 лет Вам будет', age + 20)
print('По статистике Ва остальсь жить', ale - age)
print('Общее время жизни всех людей в РФ =', (14 * 10 ** 7) * ale)
print('Часть прожитой жизни', age / ale)  # <class 'float'> деление, тип с точкой
print('Часть прожитой жизни', age // ale)  # деление нацело
print(3 % 2)  # остаток от деления
print(2 ** 10)  # возведение в степень

# Логические операции
print('У вас юбилей', age % 5 == 0)
