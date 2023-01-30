#Zadanie 1
name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
name_dictionary = {
  "John": [len(name_list[0])],
  "Michael": [len(name_list[1])],
  "Terry": [len(name_list[2])],
  "Eric": [len(name_list[3])],
  "Graham": [len(name_list[4])]
}
print("Zadanie 1:", name_dictionary)
#Zadanie 2
number_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_number_list = []

for number in number_list:
  if number > 1:
    for i in range (2, number):
      if number % i == 0:
        break
    else:
      prime_number_list.append(number)
print("Zadanie 2:", prime_number_list)
#Zadanie 3
weekdays_list = ["pon", "śro", "pią", "sob"]
weekdays_list.insert(1, "wto")
weekdays_list.insert(3, "czw")
weekdays_list.append("nie")
print("Zadanie 3:", weekdays_list)
#Zadanie 4
making_tea_steps_list = [
  "włącz czajnik", 
  "znajdź opakowanie herbaty", 
  "zalej herbatę", 
  "nalej wody do czajnika", 
  "wyjmij kubek", 
  "włóż herbatę do kubka"
]
making_tea_steps_list[0] = "znajdź opakowanie herbaty"
making_tea_steps_list[1] = "nalej wody do czajnika"
making_tea_steps_list[2] = "włącz czajnik"
making_tea_steps_list[3] = "wyjmij kubek"
making_tea_steps_list[4] = "włóż herbatę do kubka"
making_tea_steps_list[5] = "zalej herbatę"
print("Zadanie 4:", making_tea_steps_list)