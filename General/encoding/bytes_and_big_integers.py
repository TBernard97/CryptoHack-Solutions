number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

byte_string = number.to_bytes(len(str(number)), 'big')

print(byte_string)