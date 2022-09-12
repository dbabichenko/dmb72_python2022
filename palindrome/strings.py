s = "Hello world!"

l = [1, 2, 3, 'a', 'b', 'race car', 'bob']

print(l[3:6])
print(l[:4])
print(l[4:])
print(l[-1])
print(l[::-1])

print(s[3])
print(s[-1])
print(s[3:5])
print(s[::-1])


print(sorted(s))

'''
   for(int i = 97; i<=122; i++){

   }
'''

for i in range(0, len(s)):
    print(s[i])

'''
    for(int i: listVariable){

    }
'''

for letter in s:
    print(letter)


[print(letter) for letter in s]