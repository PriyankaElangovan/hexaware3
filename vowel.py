string = list(map(str, input().lower()))
lst = []
for i in range(0, len(string)):
  if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
    lst.append(string[i])
print(len(lst))
