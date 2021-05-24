def encrypt(text,key):
   result = ""
 
   for i in range(len(text)):
      char = text[i]
      #print (text[i])
      #result += chr((ord(char) + key - 65) % 26 + 65)

      #ord() returns an integer representing the Unicode character
      result += chr((ord(char) + key - 97) % 26 + 97)

   return result

#xly td detww esp xzde pieclzcotylcj nzxafepc zq lww
#hml qgmj xmlmjw af yggv zsfvk qgmj gof 
##############################

def decrypt(cipher,key):
   result = ""
 
   for i in range(len(cipher)):
      char = cipher[i]
      result += chr((ord(char) - key - 97) % 26 + 97)

   return result

##############################

abc = 'abcdefghijklmnopqrstuvwxyz'
x = int(input("Enter 1 to Encrypt, 2 to Decrypt: "))

if(x == 1):
    text = input("Enter Text in Lowercase: ")
    key = int(input("Enter Key: "))

    print ("Cipher: " + encrypt(text,key))

###############################

elif(x == 2):
    cipher = input("Enter Cipher in Lowercase: ")
    y = int(input("Do you have the key? Enter 1 for YES, 0 for NO: "))


    if(y == 1):
        key = int(input("Enter Key: "))
        print ("Cipher: " + decrypt(cipher,key))


    elif(y == 0):
        print("Brute Force will commence now...")

        for key in range(len(abc)):
            result = ''
            for z in cipher:
                if z in abc:
                    num = abc.find(z) #get position number
                    num -= key
                    
                    if num < 0:
                        num += len(abc) #add 26 if its -ve
                    
                    result += abc[num]
                    
                else:
                     result += z
                     print("Decryption Failed")
                     
            print('Hacking key #%s: %s' % (key, result))


    else:
        print("You had one job, to enter 1 or 0")


else:
    print("You entered a wrong number")

