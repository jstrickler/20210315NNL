fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit.upper() + '\n')

nums = [800,80,1000,32,255,400,5,5000]

with open("numbers.txt", "w") as numbers_out:
    for num in nums:
        numbers_out.write(f"{num:05d}\n")

with open('fruits.txt') as fruits_in:  # input data
    with open('with_vowels.txt', 'w') as with_vowels_out:  # output data
        with open('without_vowels.txt', 'w') as without_vowels_out:  # output data
            for fruit in fruits_in:
                if fruit[0].lower() in 'aeiou':
                    with_vowels_out.write(fruit)
                else:
                    without_vowels_out.write(fruit)

#  r  w  a x
#  rb wb ab xb

