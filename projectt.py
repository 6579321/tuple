def calculate_product(tpl):
    product = 1
    for num in tpl:
        product *= num
    return product

# Example usage
tuple_of_numbers = (2, 3, 4, 5)
result = calculate_product(tuple_of_numbers)
print(f"The product of all numbers in the tuple is: {result}")
