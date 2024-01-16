# #list - це мутабєльна колекція, ми можемо змінювати у ній дані.
# import random
#
# numbers = []
# numbers_1 = list()
#
# print(type(numbers))
# print(type(numbers_1))
#
# numbers = [1, 3, 25, 7, 2, 7]
# print(numbers)
# print(numbers[0])
#
# numbers[1] = 11111
# print(numbers)
#
# print(len(numbers)) #це для отримання довжини рідка, скільки цифр у рядку
# print(numbers[-1]) #ми використовуємо від'ємні індекси, щоб отримати якесь значення з кінця списку
#
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
# print()
#
# for number in numbers:
#     print(number, end=" ")
# print()
#
# #
# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3] * 5  #виводить цифри 1 та 3 5 разів підряд, це дублювання списку.
# #ми можемо додавати та помножувати списка, але не можемо їх ділити та віднімати
# print(nums)
#
# #
# numbers = [1, 3, 25, 7, 2, 7] #вчимость працювати зі зрізами у списках
# print(numbers[:]) #виводить цілий список, всі цифри у списку
# print(numbers[1:5]) #виводить індекси зі списку з 1го по 4й, бо 5й індекс не відображується
# print(numbers[1:5:2]) #виводимо кожен другий елемент зі списку з індексів від 1 до 5
# print(numbers[:: -1]) #так ми можемо перевернути список і він буде задом на перед
#
# # розкладання списку\ декомпозиція
#
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)
#
# # import random - створення рандомних списків
#
# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
#
# # робимо цикл, який буде додавати рандомне число кожного разу у кінець списку
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
# print(numbers)
#
# # як працює append(item) - додає елемент item до кінця списку
# numbers.append(2222)
# print(numbers)
#
# #insert(index, item) - додає елемент item до списку за індексом index
# numbers.insert(1, 3333) #ми додали 3333 на місце 1го індексу і списку
# print(numbers)
#
# #extend(items) - додає набір елементів items до кінця списку
# numbers.extend([2, 3, 4])
# print(numbers)
#
# #remove(item) - видаляє елемент item, видаляється лише перше входження елемента
# #якщо елемент не знайдено, то генерується виняток ValueError
# numbers.remove(2222)
# print(numbers)
#
# #clear() - видалення всіх елементів зі списку
# # numbers.clear()
# # print(numbers)
#
# #index(item) - повертає індекс елемента item. якщо елемент не знайдено, то генерує виняток ValueError
# print(numbers.index(2))
#
# #pop([index]) - видаляє та повертає елемент за індексом index; коли треба видалити якесь значення по індексу
# #якщо індекс не передано, то просто видаляє останній елемент
#
# result = numbers.pop(0)
# print(result)
# print(numbers) #ми у прикладі за індексом 0 видалили число 6
#
# #варіація pop, яка видаляє значення з кінця, видаляє останній елемент у списку
# print(numbers.pop())
# print(numbers) #ми у прикладі видалили 4ку, яка була останнім елементом списку

#count(item) - повертає кількість входжень елемента item до сприску
#дозволяэ порахувати, скульки разыв цей елемент зустрычаэться у списку
# print(numbers.count(3))

#функції sort та sorted
# sort([key]) - сортує елементи, за замовченням сортує за зростанням. змінює оригінал списку
# sorted(list, [key]) - повертає відсортований список, вона не зманіює оригінал списку
#вона повертає нам відсортовану копію, а оригінал списка залишиться незмінним

# numbers, sort()
# print(numbers)
#
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)

# #v1.
# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# people.sort()
# print(people)
#
# #v2.
# people.sort(key=str.lower) #тут ми передали параметр key, та привели всі значення до нижнього регыстру lower
# print(people)
#
# #v3. - з функцією sorted, ми зробили копію списка і відсортували її за нижнім регістром
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

#reverse() - функція розставляє всі елементи у списку у зворотньому порядку, зеркалює їх, вона змінює оригінал
# numbers.reverse()
# print(numbers)

# #функція copy() - копіює список, вона робить з нього точну та повністю самостійну копію
# nums_1 = [1, 3, 5]
# nums_copy = nums_1
# print(nums_1)
# nums_copy[1] = 1111  #ми тут замінтили число на 1111
# print(nums_1) #це оригінал списку
# print(nums_copy) #це копія списку (при заміні числа на 1111 змінились і оригінал, і копія)

#вбудовані функціі у списках:
# len(list) #повертає довжину списку
# print(len(numbers))
#
# min(list) #повертає найменший елемент списку
# print(min(numbers))
#
# max(list) #повертаэ найбільший елемент списку
# print(max(numbers))

# #як знайти мінімум та максимум у рядків
# users = ["Vasya", "Sam"]
# print(max(users))
#
# letters = ["ab", "ac"]
# print(max(letters))

############################

#функції split та join
#split - дозволяє роззділити рядок за якимость розділителем.
#по дефолту розділителем є пробіл, але можна задати і свій
#скільки розділителей знайде split, стільки частин він і виведе
# text = "hello world. goodbye, world"
# search_item = ". "
# sentences = text.split(search_item)
# print(sentences)
# result = []

# #зробимо перше слово у реченні з великої букви
# for sentence in sentences:
#     result.append(sentence.capitalize())
# print(result)
# #об'єднаємо обидва речення у один рядок
# result_sentence = search_item.join(result)
# print(result_sentence)

# #створити список з 10 чисел, поміняти місцями min та max значння
#
# nums = [3, 1, 4, 2, 5]
# print(nums)
# min_value = min(nums)
# max_value = max(nums)
# min_value_index = nums.index(min_value)
# max_value_index = nums.index(max_value)
# nums[min_value_index] = max_value
# nums[max_value_index] = min_value

# #або інакше зробити те саме, але через множественное присвоєння
# nums[nums.index(min(nums))], nums[nums.index(max(nums))] = max(nums), min(nums)
# print(nums) #список не змінився відносно оригінала
# #застосуємо для зміни списку nums_copy
# nums = nums.copy()
# nums_copy[nums.index(min(nums))], nums_copy[nums.index(max(nums))] = max(nums), min(nums)
# nums = nums_copy.copy()
# print(nums)


















#Task1
# згерерувати список рандомних цілих чисел, вивести на екран
# порахувати суму негативних чисел, суму парних чисел та суму непарних чисел

#v1.
import random

randomlist = random.sample(range(-10, 30), 5)
print(randomlist)

minNum=-10
maxNum=20
mainlist=[]
list_Odds=[]
list_Evens=[]
list_Neg=[]
sumNeg=0
sum_Odds=0
sum_Evens=0

#Making the 20 random elements list with integers starting from lowNum and upto #HighNum
import random
#Generate 20 random numbers between lowNum and highNum
randomlist = random.sample(range(minNum, maxNum), 10)

print("In range from ", minNum, " to", maxNum, " :")
print("\nThe 10 element random list :")
print(randomlist)

# dividing the main list into negatives, positive odds and positive even
# and calculating their sums separately
for item in randomlist:
    if (item > 0):
        if (item % 2 == 1):
            list_Odds.append(item)
            sum_Odds += item
        else:
            list_Evens.append(item)
            sum_Evens += item
    elif (item < 0):
        list_Neg.append(item)
        sumNeg += item

print("Negative elements in list :")
print(list_Neg)
print("\n Sum of all negative elements in List :", sumNeg)

print("\n Positive even elements in list :")
print(list_Evens)
print("\n Sum of all positive even elements in list :", sum_Evens)

print("\n Positive odd elements in list :")
print(list_Odds)
print("\n Sum of all positive odd elements in list :", sum_Odds)

print()
#порахувати суму елементів між min та max елементом, добуток елементів між min та max елементом;


import random
nums = [random.randint(10, 15) for _ in range(10)]
print(nums)

prod_min_max = 2

min_num = min(nums)

max_num = max(nums)

for num in nums:

   if num > min_num and num < max_num:

       prod_min_max = min_num * max_num
       sum_min_max = min_num + max_num

print('sum_min_max =', sum_min_max)
print('prod_min_max =', prod_min_max)
print()

#порахувати добуток елементів з індексами 3
prod_3 = 1

for i, num in enumerate(nums):

   if i % 3 == 0:

       prod_3 *= num

print('prod_3 =', prod_3)

print()

#Task2
#згенерити рандомний список цілих, на підставі даних цього списку масиву:

#cтворити список цілих, що містить лише парні числа з першого списку;
#cтворити список цілих, що містить лише непарні числа з першого списку;
#cтворити список цілих, що містить лише негативні числа з першого списку;
#cтворити список цілих, що містить лише позитивні числа з першого списку.

def separate_numbers(numbers):
    even = []
    odd = []
    negative = []
    positive = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)
    return even, odd, negative, positive

numbers = random.sample(range(-5, 20), 10)
print(numbers)

even, odd, negative, positive = separate_numbers(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Negative numbers:", negative)
print("Positive numbers:", positive)

#
#

#Task 3
# У списку цілих, заповненому випадковими числами обчислити:
#створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99

#вивести на екран

#вивести суму чисел головної діагоналі матриці

#вивести мінімальне та максимальне значення побічної діагоналі матриці

#ввести з клавіатури порядковий номер стовпця, вивести цифри з
#цього стовпця на екран (аналогічно зробити з рядком)

#ввести з клавіатури порядковий номер одного стовпця і потім
#іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)

print()
import random

randomlist = random.sample(range(1, 10), 8)
print(randomlist)

