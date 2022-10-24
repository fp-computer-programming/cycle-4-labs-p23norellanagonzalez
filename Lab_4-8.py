#author NDO 10/18/22
# prompts the usre to input a 6 letter sequnece of DNA
var_one = input('Please type a sequence of a,c,t,g here:')

var_comp = ''

if var_one[0] == 'a' : 
    var_comp += 't'
elif var_one[0] == 't' : 
    var_comp += 'a'
elif var_one[0] == 'c' : 
    var_comp += 'g'
elif var_one[0] == 'g' : 
    var_comp += 'c'

if var_one[1] == 'a' : 
    var_comp += 't'
elif var_one[1] == 't' : 
    var_comp += 'a'
elif var_one[1] == 'c' : 
    var_comp += 'g'
elif var_one[1] == 'g' : 
    var_comp += 'c'

if var_one[2] == 'a' : 
    var_comp += 't'
elif var_one[2] == 't' : 
    var_comp += 'a'
elif var_one[2] == 'c' : 
    var_comp += 'g'
elif var_one[2] == 'g' : 
    var_comp += 'c'

if var_one[3] == 'a' : 
    var_comp += 't'
elif var_one[3] == 't' : 
    var_comp += 'a'
elif var_one[3] == 'c' : 
    var_comp += 'g'
elif var_one[3] == 'g' : 
    var_comp += 'c'

if var_one[4] == 'a' : 
    var_comp += 't'
elif var_one[4] == 't' : 
    var_comp += 'a'
elif var_one[4] == 'c' : 
    var_comp += 'g'
elif var_one[4] == 'g' : 
    var_comp += 'c'

if var_one[5] == 'a' : 
    var_comp += 't'
elif var_one[5] == 't' : 
    var_comp += 'a'
elif var_one[5] == 'c' : 
    var_comp += 'g'
elif var_one[5] == 'g' : 
    var_comp += 'c'               

# print the complementary strand    
print(var_comp)
