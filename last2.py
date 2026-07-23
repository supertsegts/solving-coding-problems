def last2(str):
  count = 0
  str_to_compare = str[-2:]
  a = str[:-1]
  
  for i in range(len(a)-1):
    check = a[i] + a[i+1]
    if check==str_to_compare:
      count+=1
  return count



#def last2(str):
#  count = 0
#  str_to_compare = str[:-2]
#  a = str[-2:]
#  for i in range(len(str)):
#    if a[i]==str_to_compare[i] and a[i+1]==str_to_compare[i+1]:
#      count=count+1
#  return count
