ins = input()
list_string =[]
for i in ins:
  if i not in list_string:
    list_string.append(i)
print(len(list_string))