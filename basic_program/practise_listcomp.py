create_list = [i for i in range(10, 50)]
print(create_list)

"""
     using if condition in list comprehension
"""

even_number = [i for i in range(11, 41) if i % 4== 0]
print(even_number)
"""
     using if & else condition in list comprehension
"""

even = [i if i % 6== 0 else "odd" for i in range(10, 20)]
print(even)

