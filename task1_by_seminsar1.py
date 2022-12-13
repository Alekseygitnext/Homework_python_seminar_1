# Напишите программу, которая принимает на вход цифру, обозначающую день недели
# и проверяет является ли этот день выходным

day = int(input("Введите цифру обозначающую номер дня недели: "))
list_of_working_days = [1,2,3,4,5]
list_of_days_off = [6,7]
if day in list_of_working_days: print("Рабочий день")
elif day in list_of_days_off: print("Выходной день")
else: print("это не день недели")