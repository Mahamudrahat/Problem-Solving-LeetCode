# import the re module
import re

# initializing string
test_string ="  hello world  "
stack=[]
# printing original string
print("The original string : " + str(test_string))

# Using re.split() to split the string including spaces
res = re.split(r'(\s)', test_string)

# Removing empty strings from the list
res = [x for x in res if x != '']

if res[0]==' ':
    res.pop();
if res[-1]==' ':
    res.pop();
print(res)
for i in range(len(res)-1,0,-1):
    if(res[i] != res[i-1]):
              stack.append(res[i])

stack.append(res[0])


if stack[0]==' ':
    stack.pop();
if stack[-1]==' ':
    stack.pop();
result_string = ''.join(stack)
print("The list without omitting spaces : " + result_string)
