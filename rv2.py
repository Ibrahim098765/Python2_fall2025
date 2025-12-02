''''
#ceck for palindrome
def is_palindrome(word):
 #check whether the word is palindrome
    """
    end = len(word) // 2
    for i in range(len):
        if word[i] != word[-i-1]:
            return False
    return True
    """
    return word == word[::-1] 
word = 'civic'
if is_palindrome(word):
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrom')
# list 
import random 
num_list = []
for i in range(10):
    num_list.append(random.randint(1,100))
print('using loop',num_list)

#list comprehension
num_list1 =[randomint(1,100) for _ in range(10)]
print('using list comprehension:',num_list1)
num_list.append(1,2,3)
num_list.extend([1,2,3])
'''

      
    # use random
import random
tow_D = []
for i in range(10):
    row = []
    for j in range(5):
        row.append(random.randint(1,100))
    tow_D.append(row)
print(tow_D)

