""""

! Завдання відсортовано за складністю
1. Порахувати сумму чисел послідовності 
2. Порахувати добуток чисел послідовності 
3. Порахувати кількість чисел у послідовності 
4. Мінімальне та максимальне числа послідовності
5. Індекс (розташування, номер по порядку введення) мінімального та максимального числа послідовності 
6. Кількість максимальних та мінімальних чисел у послідовності

"""
number = None
sum = 0
while number != 0:
    number = int(input("Write an integer(enter 0 to stop): "))
    sum += number

print(f"the sum of all numbers is {sum}") 
