# Урок 4. Задание 1
''''
1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.
'''
# Импорт файла data_wage.py

from data_wage import wage

print(f'Зарплата будет составлять {wage()}  с учетом премении 10%')

