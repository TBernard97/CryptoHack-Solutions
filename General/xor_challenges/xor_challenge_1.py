string = "label"

unicode = [ord(c) for c in string]

flag = ""
for i in unicode:
   xor = i ^ 13
   letter = chr(xor)
   flag += letter

print(flag)
   

