#author NDO 10/17/22

# prompts user 1 and 2 to type their name seperately 
user1_name = input('User 1 please enter your name here')
user2_name = input('User 2 please enter your name here')

# creates a statement that displays the sentence 
fs = 'Hello, {0}. My name is {1}.'.format(user1_name, user2_name)
print(fs)


