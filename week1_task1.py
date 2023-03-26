input_strng=str(input("enter the string: "));
# defined a fn l2n to return the digit
def l2n(letter):
   S="abcdefghijklmnopqrstuvwxyz";
   return S.index(letter)+1;
output_stng="";
for i in input_strng:
    if i.isalpha():        
      j=i.lower();             #for checking both uppercase and lowercase
      output_stng=output_stng+" "+str(l2n(j));
    else:
      continue
print(str(output_stng));
