# def is_even(num):
#     if num == 0:
#         print("Zero")
#     else:
#         if num % 2 == 0:
#             print(f"{num} is an even number")
#         elif num % 2 != 0:
#             print(f"{num} is an odd number")
#         else:
#             print("Zero")

# number = int(input("Enter a number: "))
# is_even(number)

"""calculate the area of a rectangle"""
# area = width * height

def calculate_area_rectangle(width, height):
    area = width * height
    return area

rectangle = calculate_area_rectangle(4, 10)
print(rectangle)