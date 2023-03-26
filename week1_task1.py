input_str=str(input("enter the string: "));

# defined a fn l2n to do the task

def l2n(letter):
   S="abcdefghijklmnopqrstuvwxyz";
   return S.index(letter)+1;

output_str="";

for i in input_str:
    if i.isalpha():
      j=i.lower();
      ouput_str=output_str+" "+output_str(l2n(j));
    else:
      continue
print(str(output_str));
