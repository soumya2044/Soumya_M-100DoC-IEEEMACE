a=str(input("enter the string: "));

# defined a fn l2n to do the task

def l2n(letter):
   S="abcdefghijklmnopqrstuvwxyz";
   return S.index(letter)+1;

stng="";

for i in a:
    if i.isalpha():
      j=i.lower();
      stng=stng+" "+str(l2n(j));
    else:
      continue
print(str(stng));