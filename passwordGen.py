import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
uppercaseLetter3 = chr(random.randint(65,90))
uppercaseLetter4 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
lowercaseLetter3 = chr(random.randint(97,122))
lowercaseLetter4 = chr(random.randint(97,122))

digit1 = random.randint(0,9)
digit2 = random.randint(0,9)
digit3 = random.randint(0,9)
digit4 = random.randint(0,9)

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 \
+ uppercaseLetter4 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 \
+ lowercaseLetter4 + str(digit1) + str(digit2) + str(digit3) + str(digit4)
password = shuffle(password)

print(password)
