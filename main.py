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

######################################################################################

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
