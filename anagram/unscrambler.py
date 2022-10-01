
# Open data file
f = open('words.txt')

# Read data
data = f.readlines()

base = "cardiothorasic"
base_letters = sorted(base)

result = []
for word in data:
    word_letters = sorted(word.strip().lower())
    if len(word.strip()) in range(3, 7):
        if all(elem in base_letters  for elem in word_letters):
            result.append(word.strip())

sorted_result = sorted(result, key=len)

prev_len = 0
for word in sorted_result:
    if prev_len != len(word):
        print("___________________________")
        print("Words with ", len(word), " characters:")
        print("___________________________")
        prev_len = len(word)
    print(word)



