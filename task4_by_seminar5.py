#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

quarter_number = int(input('Введите номер четверти: '))
if quarter_number == 1: print ('infinity > X > 0 ; infinity > Y > 0')
elif quarter_number == 2: print ('0 > X > - infinity ; infinity > Y > 0')
elif quarter_number == 3: print ('0 > X > - infinity ; 0 > Y > - infinity')
elif quarter_number == 4: print ('infinity > X > 0 ; 0 > Y > - infinity')
else: print ('Нет такого номера четверти')