# Урок 4. Задание 1
''''
1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.
'''


from sys import argv

income1, piecework, hours = argv

print("Имя скрипта: ", income1)
print("Ставка в час: ", piecework)
print("Выработка в часах: ", hours)
print(f'Премия 10%: {float(piecework)*float(hours)*0.1}')
print(f'Итого с учетом премии: {float(piecework)*float(hours)*1.1}')