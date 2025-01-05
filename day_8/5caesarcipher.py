
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #we have written the alphabets twice because when aur word contain ending letters like "z" haw can it find letter next to "z" for shift

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26   #so that we can get result also when large shifts were typed

    def encrypt(plain_text, shift_amount):
        cipher_text=""  
        for letter in plain_text:
            
            position = alphabet.index(letter)      # to get the rank of letter in the alphabet list

            new_position = position + shift_amount

            new_letter = alphabet[new_position]

            cipher_text += new_letter  

        print(f"The encoded text is {cipher_text}")

    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)    
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
        print(f"the decoded text is {plain_text}")


    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)

    elif direction == "decode":
        decrypt(cipher_text=text, shift_amount=shift)


    result = input(" type yes if you want to go again. Otherwise type no.\n")
    if result == "no":
        should_continue = False