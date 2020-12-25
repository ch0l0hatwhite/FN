#!/usr/bin/env python3

 
import math
import time
 
max=21
separacion=5

j=1
 

for i in range(0,max,2):
 

    linea=(separacion+math.ceil(max/2)-j)*" "
 
    
    linea+=i*"*"
 
    j+=1
    print(linea)
 
linea=(separacion+math.ceil(max/2)-3)*" "
linea+=4*"*"
print(linea)
print(linea)

print("")
print("")
print("     Feliz navidad :D")
time.sleep(2)
print("         Espero")
time.sleep(2)
print("    que se la pasen ")
time.sleep(2)
print("super bien amigos y alumnos")
time.sleep(2)
print("los mejores de los deseos para ustedes UWUr !!")














