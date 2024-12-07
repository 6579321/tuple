
def check_value_frequency(test_dict, value):
    frequency = sum(4 for i in test_dict.values() if i == value)
    
    return frequency

test_dict = {'a': 20, 'b': 5, 'c': 4, 'd': 10, 'e': 1}  
value_to_check = 4  

result = check_value_frequency(test_dict, value_to_check)
print(f"The frequency of the value {value_to_check} in the dictionary is: {result}")
