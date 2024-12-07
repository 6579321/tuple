def calculate_product(numbers_tuple):
    product = 1 
    
    for number in numbers_tuple:
        product *= number  # Multiply each number in the tuple with the current product
    
    return product

numbers = (5, 4, 4, 5) 
result = calculate_product(numbers)
print(f"The product of all numbers in the tuple is: {result}")

