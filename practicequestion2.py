# favorite_foods = ["pizza", "pasta", "sushi", "tacos", "ice cream"]
# print(favorite_foods)

# foods = ["pizza", "pasta", "sushi", "tacos", "ice cream"]
# print(foods[0])
# print(foods[-1])

# foods = ["pizza", "pasta", "sushi"]
# foods.append("tacos")
# print(foods)

# foods = ["pasta", "sushi"]
# foods.insert(0, "pizza")
# print(foods)

# foods = ["pizza", "pasta", "sushi"]
# foods[1] = "tacos"
# print(foods)

# foods = ["pizza", "pasta", "sushi"]
# foods.remove("pasta")
# print(foods)

# foods = ["pizza", "pasta", "sushi"]
# last_item = foods.pop()
# print(last_item)
# print(foods)

# foods = ["pizza", "pasta", "sushi"]
# print(len(foods))

# foods = ["pizza", "pasta", "sushi"]
# print("pasta" in foods)

# numbers = [1, 2, 2, 3, 2, 4]
# print(numbers.count(2))

# foods = ["pizza", "pasta", "sushi"]
# print(foods.index("pasta"))

# numbers = [5, 2, 8, 1, 3]
# numbers.sort()
# print(numbers)

# names = ["Zara", "Ali", "Maya", "Ben"]
# names.sort()
# print(names)

# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = numbers[::-1]
# print(reversed_numbers)

# numbers = [4, 9, 2, 7, 5]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)

# numbers = [4, 9, 2, 7, 5]
# smallest = numbers[0]
# for number in numbers:
#     if number < smallest:
#         smallest = number
# print(smallest)

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# numbers = [1, 2, 3, 4, 5]
# average = sum(numbers) / len(numbers)
# print(average)

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# words = ["apple", "banana", "grape", "watermelon"]
# long_words = [word for word in words if len(word) > 5]
# print(long_words)

# numbers = [1, 2, 2, 3, 1, 4]
# unique_numbers = list(dict.fromkeys(numbers))
# print(unique_numbers)

# first_list = [1, 2, 3]
# second_list = [4, 5, 6]
# combined_list = first_list + second_list
# print(combined_list)

# first_list = [1, 2, 3, 4]
# second_list = [3, 4, 5, 6]
# common_values = [value for value in first_list if value in second_list]
# print(common_values)

# original = ["red", "green", "blue"]
# copied_list = original.copy()
# copied_list[0] = "yellow"

# print("Original:", original)
# print("Copy:", copied_list)

# squares = [number ** 2 for number in range(1, 11)]
# print(squares)

# cities = ("Mumbai", "Delhi", "Tokyo", "Paris", "Cairo")
# print(cities)

# cities = ("Mumbai", "Delhi", "Tokyo", "Paris", "Cairo")
# print(cities[0])
# print(cities[-1])

# cities = ("Mumbai", "Delhi", "Tokyo", "Paris", "Cairo")
# print(len(cities))

# cities = ("Mumbai", "Delhi", "Tokyo", "Paris", "Cairo")
# print("Tokyo" in cities)

# numbers = (1, 2, 2, 3, 2, 4)
# print(numbers.count(2))

# cities = ("Mumbai", "Delhi", "Tokyo", "Paris", "Cairo")
# print(cities.index("Tokyo"))

# numbers = tuple(range(1, 11))
# print(numbers)

# first = ("red", "green")
# second = ("blue", "yellow")
# combined = first + second
# print(combined)

# colors = ("red", "blue")
# repeated = colors * 3
# print(repeated)

# fruits = ("apple", "banana", "cherry")
# fruit_list = list(fruits)
# fruit_list[1] = "orange"
# fruits = tuple(fruit_list)
# print(fruits)

# person = ("Asha", 25, "Mumbai")
# name, age, city = person
# print(name)
# print(age)
# print(city)

# a = 10
# b = 20
# a, b = b, a
# print(a, b)

# numbers = (8, 3, 12, 5, 1)
# print("Largest:", max(numbers))
# print("Smallest:", min(numbers))

# single_item = ("apple",)
# print(single_item)

# names = ("Asha", "Ravi", "Mina")
# updated_names = names + ("Leo",)
# print(updated_names)

# person = {"name": "Asha","age": 25,"city": "Mumbai"}
# print(person["name"])
# print(person["age"])
# print(person["city"])

# person = {"name": "Asha", "age": 25}
# person["city"] = "Mumbai"
# print(person)

# person = {"name": "Asha", "age": 25}
# person["age"] = 26
# print(person)

# person = {"name": "Asha", "age": 25, "city": "Mumbai"}
# removed_city = person.pop("city")
# print("Removed:", removed_city)
# print(person)

# person = {"name": "Asha", "age": 25}
# print("age" in person)

# person = {"name": "Asha", "age": 25, "city": "Mumbai"}
# print(person.keys())

# person = {"name": "Asha", "age": 25, "city": "Mumbai"}
# print(person.values())

# person = {"name": "Asha", "age": 25, "city": "Mumbai"}
# for key, value in person.items():
#     print(key, ":", value)

# word = "banana"
# letter_counts = {}
# for letter in word:
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1
# print(letter_counts)

# products = {"book": 12,"backpack": 35,"headphones": 50}
# highest_priced_product = max(products, key=products.get)
# print(highest_priced_product, products[highest_priced_product])