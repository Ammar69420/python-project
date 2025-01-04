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


def vigenere_decrypt(text, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) - 65 for i in key.upper()]  # Adjusted to work with 0-25
    key_index = 0  # Track key index only for alphabetic characters

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            text_int = ord(char) - shift_amount
            key_int = key_as_int[key_index % key_length]
            
            value = (text_int - key_int + 26) % 26  # Decryption formula
            decrypted_text.append(chr(value + shift_amount))
            
            key_index += 1  # Increment key index for alphabetic characters
        else:
            decrypted_text.append(char)  # Keep non-alphabetic characters unchanged

    return ''.join(decrypted_text)


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

    print("\nDo you want to try Vigenère cipher decryption?")
    try_vigenere = input("Enter 'yes' to proceed, or 'no' to skip: ").lower()

    if try_vigenere == 'yes':
        key = input("Enter the Vigenère cipher key: ")
        decrypted_vigenere_text = vigenere_decrypt(encrypted_text, key)
        print(f"\nDecrypted text using Vigenère cipher (key: {key}):")
        print(decrypted_vigenere_text)
    else:
        print("Skipping Vigenère cipher decryption.")


if __name__ == "__main__":
    main()
