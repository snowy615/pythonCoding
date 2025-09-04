def string_to_list_of_numbers(s):
    return [int(char) for char in s]

# Example usage:
s = "1234567890"
list_of_numbers = string_to_list_of_numbers(s)
print(list_of_numbers)
