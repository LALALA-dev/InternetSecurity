#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

MyInputYes = bytes("Yes",'utf-8') + bytes("\x0d"*13,'utf-8')
#MyInputNo = bytes("No",'utf-8')+ bytes("\x0e"*14,'utf-8')
BobIV = "721290110177fcd873715992acd831d9" #Bob's IV
NextIV = "601534c10177fcd873715992acd831d9" #Next IV


# Convert ascii string to bytearray
#D1 = bytes(MyInputYes, 'utf-8') #"Yes"


# Convert hex string to bytearray
D3 = bytearray.fromhex(BobIV)
D4 = bytearray.fromhex(NextIV)

r1 = xor(MyInputYes, D3)
r2 = xor(r1, D4)
print(r2.hex())
