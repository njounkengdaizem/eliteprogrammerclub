# write a simple program that takes a sentence as input,
# returns the capitalized for of the sentence.
#############################################################
result = ""     # an empty string to hold the resulting string
word = input("Enter a word: ")                                  # gets inputs from the user
word = word.capitalize()                                        # capitalizes the first letter of the string
word = word.split('.')                                          # splits words depending on where the "." is

for i in word:                                                  # here goes the magic
    result += i[0].upper() + i[1:] + '. '          # converts the first letter of the split string to uppercase
print(result[:])                                   # then concatenates the remaining letters and adds a
                                                   # full stop and empty space between the words.


