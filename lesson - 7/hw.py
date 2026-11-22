import math

#1
one_num = int(input("input 1 num: "))
two_num = int(input("input 2 num: "))
three_num = int(input("input 3 num: "))

nums = [one_num, two_num, three_num]
result = list(map(lambda x:math.sqrt(x), nums))

print(result)

#2
r_input = float(input("input radius: "))
find_s = lambda r:math.pi*r**2
s = find_s(r_input)
l = 2 * math.pi * r_input

print("площадь (S):", round(s, 2))
print("длина окружности (L):", round(l, 2))

#3
input1 = float(input("input float 1: "))
input2 = float(input("input float 2: "))
input3 = float(input("input float 3: "))
input4 = float(input("input float 4: "))
input5 = float(input("input float 5: "))

all_input = [input1, input2, input3, input4, input5] 

fist_func = list(map(lambda x:math.ceil(x), all_input))
second_func = list(map(lambda x:math.floor(x), all_input))

print(fist_func)
print(second_func)

#4
n  = int(input("input n: "))

total = 0

for i in range(1, n + 1):
    f = 1

    for j in range(1, i + 1):
        f *= j

    total += f

print(f"Sum factorial = {total}")

#5
natural1 = int(input("1 input natural number : "))
natural2 = int(input("2 input natural number : "))
natural3 = int(input("3 input natural number : "))

naturals = [natural1, natural2, natural3]
nods = math.gcd(natural1,natural2,natural3)
k = map(lambda x:x/nods, naturals)
print(list(k))