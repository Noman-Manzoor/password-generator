import random
print("         PASSWORD GENERATOR")
def shuffle(abc):
    templist = list(abc)
    random.shuffle(templist)
    return ''.join(templist)

uppercase_letter1 = chr(random.randint(65,90))
uppercase_letter2 = chr(random.randint(65,90))
lowercase_letter1 = chr(random.randint(97,122))
lowercase_letter2 = chr(random.randint(97,122))
punctuation_1 = chr(random.randint(33,38))
punctuation_2 = chr(random.randint(42,47))
num1 = random.randint(0,9)
num2 = random.randint(0,20)
password = uppercase_letter1+str(num1)+punctuation_1+uppercase_letter2+str(num2)+punctuation_2+lowercase_letter1+lowercase_letter2
final_passw = shuffle(password)
print(final_passw)