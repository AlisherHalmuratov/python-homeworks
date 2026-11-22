#7
def digit_count_and_sum(word):
    n = 0

    for i in str(word):
        n += int(i)

    print(f"сумма: {n}, кол. цифр: {len(str(word))}")

digit_count_and_sum(52647)

#8
def add_right(a, b):
    print(f"{a}{b}")

#9
def add_left(a, b):
    print(f"{b}{a}")

#10
def work_with_list(a):
    min_num  = min(a)
    
    for i in range(len(a)):
        a[i] = a[i] * min_num
    
    print(a)

work_with_list([6, 5, 4, 4, 5, 6])

#11
sales = {
     "yanvar": 12000,
     "mart": 6000,
     "aprel": 15000,
     "sentabr": 9000,
     "dekabr": 10000,
}

def big_sales(sales):
    max_sales = max(sales, key=sales.get)
    return max_sales

big_sales_noun = big_sales(sales)
print(big_sales_noun)

#12
def min_max(numbers, max_num, min_num):
    if max(numbers) == max_num and min(numbers) == min_num:
        return True
    else:
        return False

print(min_max([5, 1, 5, 1, 5, 1, 5], 2, 6))
print(min_max([5, 1, 3, 4, 3, 2, 5], 5, 1))

#13
products = [
    {
     "name": "Iphone X",
     "price": 600
    },
    {
     "name": "Iphone 12",
     "price": 1500
    },
    {
     "name": "Samsung Note 9",
     "price": 800
    },
    {
     "name": "Samsung S10",
     "price": 1100
    }
]

def expensiveProduct(products):
    f = products[0]
    
    for i in products:
        if i["price"] > f["price"]:
            f = i
            
    print(f["name"])
    
expensiveProduct(products)