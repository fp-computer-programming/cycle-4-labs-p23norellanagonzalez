#author NDO 10/13/22
#creating inputs that prompt the users input 
fruit_color = input('What is the color of the first fruit?')
fruit_color2 = input('What is the color of the second fruit?')

#creating a statement that compares the answers inputed by the user 
if fruit_color == fruit_color2 :
    print('They are the same color')
if fruit_color < fruit_color2 :
    print('The first fruit comes first')
elif fruit_color > fruit_color2 :
    print('The second fruit comes first')



