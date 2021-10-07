#######################################################################
# TASK: Write a program tat takes a string and returns, the string characters
# and their index positions,
# for example if the input string is 'smiles' you program should
# return [ ['s',0],['m',1],['i',2],['l',3],['e',4],['s',5] ]
########################################################################

# Create an empty list to contain the split characters and their index positions
store = []
# Collect string input from the user
word = input("Enter word: ")

for i in range(len(word)):
    """loop that splits the string and returns a list with their indexes
    :param len(word)
    """
    car = [word[i], i]
    store.append(car)
print("The string Characters and Indexes are: {}" .format(store))
