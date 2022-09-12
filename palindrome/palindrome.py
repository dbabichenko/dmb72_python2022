# Word or a phrase that reads the same backwards and forwards
# Things to consider:
# 1: Capitalization: ex: Bob
# 2: Non-alpha characters: ex: Race car

# Algorithm:
# 1. Get user input
# 2. Validate user input
# 3. Convert to lowercase
# 4. Remove non-alpha characters
# 5. Reverse string 
# 6. Compare strings

def clean_user_input(user_input):
    user_input = user_input.lower().strip()
    clean_input = ""
    for letter in user_input:
        if ord(letter) in range(ord('a'), ord('z')+1):
            clean_input += letter
    return clean_input

def validate_input(user_input):
    if user_input != "" and user_input != None:
        return True
    else:
        return False


user_input = input("Please enter a word or a phrase: ")

if validate_input(user_input):
   clean_input = clean_user_input(user_input)
    
reverse_input = clean_input[::-1]

if clean_input == reverse_input:
    print("Palindrome")
else:
    print("Not a palindrome")

   #print(user_input) 


