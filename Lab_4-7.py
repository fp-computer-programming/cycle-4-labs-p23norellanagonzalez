#author NDO 10/18/22
# prompt the user to input 5 numbers 
first_number = int(input('Please type a number here:'))
second_number = int(input('Please type a number here:'))
third_number = int(input('Please type a number here:'))
fourth_number = int(input('Please type a number here:'))
fifth_number = int(input('Please type a number here:'))

#store all numbers as one string 
num_str = first_number, second_number, third_number, fourth_number, fifth_number
print(num_str)

#finds and prints the max and min value of the string and prints the product of them two 
max_number = max(num_str)
print('Is the greatest number', max_number)
min_number = min(num_str)
print('Is the smallest number', min_number)

product_value = max_number * min_number 
print(product_value)


