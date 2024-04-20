a = input("Enter a text: ")
b = int(input("Enter a shift value: "))

def encrypt():
    encrypted_text = ""
    for i in a:
        if i.isalpha():
            s = ord(i)
            if i.islower():
                d = (s - ord('a') + b) % 26 + ord('a')
            elif i.isupper():
                d = (s - ord('A') + b) % 26 + ord('A')
            encrypted_text += chr(d)
        else:
            encrypted_text += i
    return encrypted_text   

def decrypt(en):
    decrypted_text = ""
    for i in en:
        if i.isalpha():
            s = ord(i)
            if i.islower():
                d = (s - ord('a') - b) % 26 + ord('a')
            elif i.isupper():
                d = (s - ord('A') - b) % 26 + ord('A')
            decrypted_text += chr(d)
        else:
            decrypted_text += i
    return decrypted_text

encrypted_text = encrypt()
decrypted_text = decrypt(encrypted_text)

print("Encrypted text:", encrypted_text)         
print("Decrypted text:", decrypted_text)
