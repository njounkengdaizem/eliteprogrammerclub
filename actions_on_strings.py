#######################################################################
# TASK: Write a program tat takes a string and returns, the string characters
# and their index positions,
# for example if the input string is 'smiles' you program should
# return [ ['s',0],['m',1],['i',2],['l',3],['e',4],['s',5] ]
########################################################################

# Create an empty list to contain the split characters and their index positions
store = []


def split_string(word):
    for i in range(len(word)):
        """loop that splits the string and returns a list with their indexes
        :param len(word)
        """
        car = [word[i], i]
        store.append(car)
    return

def capitalize(word):
    # Capitalize the beginning letters
    capitalized = word.title()
    return capitalized

def search_replace(word, old, new ):
    return word.replace(old, new)


def main():

# Collect string input from the user
    user_input = input("Enter word: ")
    split_string(user_input) #function calling split_string()
    print("The string Characters and Indexes are: {}" .format(store))

#function calling the capitalize()
    capitalized_word = capitalize(user_input)
    print(capitalized_word)
#Ask the user what word to replace
    old_word = input("What word do you want to replace: ")
    new_word = input("What are you replacing it with: ")
    replace = search_replace(user_input, old_word, new_word)
    print (replace)


if __name__=='__main__':
    main()




