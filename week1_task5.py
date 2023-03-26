def sqsum(lst):
  s=0
  for i in lst:
    if type(i)==int:
      s=s+int(i*i);
    else:
      continue;
  return s;
L=eval(input("enter the list: "));
print("The square sum is: ",sqsum(L));
