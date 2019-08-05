ins = input() # input 
list_string =[] # empty list
for i in ins:
  if i not in list_string:  # not present
    list_string.append(i) # appending the values
print(len(list_string)) # length of sub string