#Zadanie 1
cubic = [number * number * number for number in range(1,11)]
for number in cubic:
  if number % 2 != 0:
    print(number)
#Zadanie 2
number_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
zeros_list = [number_list[1:4] + number_list[5:10] + number_list[12:14]]
not_zeros_list = [number_list[0:1] + number_list[4:5] + number_list[10:12]]
print(zeros_list, not_zeros_list)