# author NDO 10/14/22
# application of the string method to find the index of the variable
word = 'flibbertigibbet' 
letter = word.find('t')
print(letter)

# After obtaining the index number of "t" we can print the letter after this value which falls between 8 and 9
letter_after_t = word[8:9]
print(letter_after_t)

# Using the string method to upper case a variable 
first_name = 'nickolas' 
uppercase = first_name.upper()
print (uppercase)

#using the split method to create spaces between the comas in the sentence 
sentence = 'I wish, I wish, I was a fish.'
split_sentence = sentence.split(',')
print(split_sentence)