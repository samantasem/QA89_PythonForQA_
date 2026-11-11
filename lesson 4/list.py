fruits = ['orange', 'strawberry', 'mango']
fruits.append('orange')
print(fruits)

fruits.insert(1,'banana')
print(fruits)

first_banana_index = fruits.index('banana')
print(f"The banana was added to position {first_banana_index}")

fruits.remove('orange')
print(fruits)

fruits.pop(2)
print(fruits)

numbers = [10,20,30]
deleted = numbers.pop(1)
print(deleted)
print(numbers)

numbers.clear()
print(numbers)
