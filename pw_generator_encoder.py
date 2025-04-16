import random

num_uppercase = []
for i in range(65, 91):
    num_uppercase.append(chr(i))

num_lowercase = []
for i in range(97, 123):
    num_lowercase.append(chr(i))

num_symbols = []
for i in range(33, 48):
    num_symbols.append(chr(i))
num_symbols.append(chr(126))

num_numbers = []
for num in range(0, 10):
    num_numbers.append(str(num))

char = num_uppercase + num_lowercase + num_symbols + num_numbers


#========================================================================================
def caesar_cipher(origin_password, num_of_shift, encode_or_decode):
    '''
    This is a password encoder function designed to encrypt or decrypt passwords to a higher level of complexity.
    The decrypted password will be shuffled randomly to avoid password leakage in external environments.
    Users can also use this function to decrypt and remember their previously encrypted password. 
    =============================================================================================================
    Parameters:
    origin_password(str): User password
    num_of_shift(int): Number of intended shifts for the original password characters
    encode_or_decode(str): Instruction to encrypt or decrypt password.
    '''
    output = []
    if encode_or_decode == "decode":
        num_of_shift *= -1
    
    for letter in origin_password:

        if letter not in char:
            output.append(letter)
        else:
            shifted_position = char.index(letter) + num_of_shift
            shifted_position %= len(char)
            output.append(char[shifted_position])
    
    random.shuffle(output)

    password = ""
    for i in output:
        password += i
    
    print(f"Here is the result: {password}")

#======================================================================================== 
def pw_generator(uppercase, lowercase, symbols, numbers):
    '''
    This power generator is designed to help users create strong and complexed passwords.
    =====================================================================================
    Parameters:
    uppercase(str): Uppercase letters
    lowercase(str): Lowercase letters
    symbols(str): Special symbols
    numbers(str): Numerical digits in string format
    '''
    
    password_list = []
    for _ in range(uppercase):
        password_list.append(random.choice(num_uppercase))
        
    for _ in range(lowercase):
        password_list.append(random.choice(num_lowercase))

    for _ in range(symbols):
        password_list.append(random.choice(num_symbols))

    for _ in range(numbers):
        password_list.append(random.choice(num_numbers))

    random.shuffle(password_list)
    password = ""
    for i in password_list:
        password += i

    print(f"Your password is: {password}")
    return password
#========================================================================================
again = True

while again:
    # choose option
    directory = input("What would you like to do today?Enter 1, 2 or 3.\n1. Encode or decode password\n2. Generate strong password\n3. Both\n")
    
    if directory == '1':
        direction = input("Type 'encode' to encrypt your password, 'decode' to decrypt your password:\n")
        code = input("Type your password here:\n")
        shift = int(input("Indicate the number of shifts for your password:\n"))

        caesar_cipher(origin_password=code, num_of_shift=shift, encode_or_decode=direction)

    elif directory == '2':
        print("Looking to find a strong password? We can help with that!")
        nr_uppercase = int(input(f"How many uppercase letters would you like in your password?\n"))
        nr_lowercase = int(input(f"How many lowercase letters would you like?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        pw_generator(uppercase=nr_uppercase, lowercase=nr_lowercase, symbols=nr_symbols, numbers=nr_numbers)
        
    elif directory == '3':
        print("Got it! We'll start with generating a strong password first!")
        nr_uppercase = int(input(f"How many uppercase letters would you like in your password?\n"))
        nr_lowercase = int(input(f"How many lowercase letters would you like?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        word = pw_generator(uppercase=nr_uppercase, lowercase=nr_lowercase, symbols=nr_symbols, numbers=nr_numbers)
        
        print("Let's move on to encoding your password:")
        direction = "encode"
        shifts = int(input("Indicate the number of shifts for your password:\n"))
        
        caesar_cipher(origin_password=word, num_of_shift=shifts, encode_or_decode=direction)
    
    else:
        print("You've chosen an invalid option!")
        break

    restart = input("Would you like to do anything else?Type 'yes' or 'no'")
    if restart == 'no':
        again = False
        print('Have a great day ahead. Goodbye!')
