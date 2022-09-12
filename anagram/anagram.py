# Anagrams

# 1. Get user input
# 2. Validate user input
# 3. Open and read the data file (words.txt)
# 4. Check if user input exists it is a valid word, else it is not
# 5. Sort input and each value in lexiographic order and compare

def validate_input(user_input, word_list = None):
    user_input = user_input.strip().lower()

    if user_input != None and user_input != "":
        if word_list != None:
            if user_input in word_list:
                return True
            else:
                print("Your word does not exist!")
                return False
        return True
    else:
        print("Please enter something!")
        return False

def check_word_exists(word, word_list):
    if user_input in word_list:
        return True
    else:
        return False

def is_word_in_base(word, base_letters):
    for letter in word:
        if letter in base_letters:
            base_letters.remove(letter)
        else:
            return False
    return True

# Open data file
f = open('words.txt')

# Read data
data = f.readlines()

# Cleaned backslash \n characters
for i in range(0, len(data)):
    data[i] = data[i].strip().lower()
#print(data[:10])

base = "dictionary"
base_letters = sorted(base)
#print(base_letters)
print("Enter a word that can be composed from letters in the word 'DICTIONARY'")
interrupt = False
while not interrupt:
    # Get user input
    user_input = input("Please enter a word: ")
    if user_input == "q":
        interrupt = True
    else:
        if validate_input(user_input, data):
            '''
            for word in data:
            
                if sorted(user_input) == sorted(word):
                    print(word)
            '''
            if is_word_in_base(user_input, base_letters):
                print("Valid word")
            else:
                print("Invalid word")            

        #print(sorted('elvis')== sorted('lives'))