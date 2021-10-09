# write a simple program that takes a sentence as input,
# returns the capitalized for of the sentence.
#############################################################
result = ""     # an empty string to hold the resulting string
sentence = input("Enter a word: ")                                  # gets inputs from the user
sentence = sentence.capitalize()
sentence_list = sentence.split('.')
list = []

for word in sentence_list:
    list.append(word.strip())                               # takes out every whitespace between splited sentence
sentence = list

for word in sentence:                                    # here goes the magic
    result += word[0].upper() + word[1:] + '. '          # converts the first letter of the split string to uppercase
print(result[:])                                   # then concatenates the remaining letters and adds a
                                                   # full stop and empty space between the words.
