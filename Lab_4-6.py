#author NDO 10/18/22
# write a program that asks for the user input for an animal and dish
animal = input('What is the animal?')
dish = input('What dish will he bring?')

#prints a true or false statement based on the first letter of the animal being the same as the first and last letter of the dish 
animal_first_letter = animal[0]
dish_first_letter = dish[0]
dish_last_letter = dish[-1]
if animal_first_letter == dish_first_letter and animal_first_letter == dish_last_letter :
    print('You may bring the dish')
else :
    print('You may not bring the dish')


