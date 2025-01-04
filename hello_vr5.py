from collections import Counter

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

def frequency_analysis(text):
    counter = Counter(char for char in text if char.isalpha())
    total_chars = sum(counter.values())
    freq_percentages = {char: (count / total_chars) * 100 for char, count in counter.items()}
    
    print("\nFrequency analysis of encrypted text:")
    for char, freq in sorted(freq_percentages.items(), key=lambda x: -x[1]):
        print(f"{char}: {freq:.2f}%")

def brute_force_caesar(text):
    print("\nBrute-forcing all possible Caesar shifts:")
    for shift in range(26):
        print(f"\nShift by {shift}:")
        print(caesar_decrypt(text, shift))

def generate_key(msg, key):
    key = list(key)
    key_length = len(key)
    key_as_list = []
    msg_index = 0 

    for i in range(len(msg)):
        if msg[i].isalpha():  
            key_as_list.append(key[msg_index % key_length])
            msg_index += 1
        else:
            key_as_list.append(msg[i])  

    return "".join(key_as_list)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    
    return "".join(encrypted_text)

def vigenere_decrypt(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    
    return "".join(decrypted_text)

def main():
    encrypted_text = input("Enter the encrypted text: ")

    frequency_analysis(encrypted_text)

    print("\nDo you want to try Caesar cipher decryption?")
    try_caesar = input("Enter 'yes' to proceed, or 'no' to skip: ").lower()

    if try_caesar == 'yes':
        brute_force_caesar(encrypted_text)
        shift_value = int(input("\nEnter the shift value you think is correct: "))
        decrypted_caesar_text = caesar_decrypt(encrypted_text, shift_value)
        print(f"\nDecrypted text using Caesar cipher (shift by {shift_value}):")
        print(decrypted_caesar_text)
    else:
        print("Skipping Caesar cipher decryption.")

    print("\nDo you want to try Vigenère cipher encryption and decryption?")
    try_vigenere = input("Enter 'yes' to proceed, or 'no' to skip: ").lower()

    if try_vigenere == 'yes':
        key = input("Enter the Vigenère cipher key: ")
        
      
        encrypted_vigenere_text = encrypt_vigenere(encrypted_text, key)
        print(f"\nEncrypted text using Vigenère cipher (key: {key}):")
        print(encrypted_vigenere_text)

       
        decrypted_vigenere_text = vigenere_decrypt(encrypted_vigenere_text, key)  # Use the newly encrypted text
        print(f"\nDecrypted text using Vigenère cipher (key: {key}):")
        print(decrypted_vigenere_text)
    else:
        print("Skipping Vigenère cipher encryption and decryption.")

if __name__ == "__main__":
    main()
