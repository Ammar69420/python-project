from collections import Counter

# Function to perform Caesar cipher decryption
def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

# Function to perform frequency analysis of the encrypted text
def frequency_analysis(text):
    counter = Counter(char for char in text if char.isalpha())
    total_chars = sum(counter.values())
    freq_percentages = {char: (count / total_chars) * 100 for char, count in counter.items()}
    
    print("\nFrequency analysis of encrypted text:")
    for char, freq in sorted(freq_percentages.items(), key=lambda x: -x[1]):
        print(f"{char}: {freq:.2f}%")

# Function to brute-force all Caesar cipher shifts
def brute_force_caesar(text):
    print("\nBrute-forcing all possible Caesar shifts:")
    for shift in range(26):
        print(f"\nShift by {shift}:")
        print(caesar_decrypt(text, shift))

# Main function to handle user input and run the analysis
def main():
    # User input
    encrypted_text = input("Enter the encrypted text: ")

    # Perform frequency analysis
    frequency_analysis(encrypted_text)

    # Caesar cipher decryption options
    print("\nDo you want to try Caesar cipher decryption?")
    try_caesar = input("Enter 'yes' to proceed, or 'no' to skip: ").lower()

    if try_caesar == 'yes':
        # Caesar brute-force
        brute_force_caesar(encrypted_text)
        shift_value = int(input("\nEnter the shift value you think is correct: "))
        decrypted_caesar_text = caesar_decrypt(encrypted_text, shift_value)
        print(f"\nDecrypted text using Caesar cipher (shift by {shift_value}):")
        print(decrypted_caesar_text)
    else:
        print("Skipping Caesar cipher decryption.")

    # Placeholder for future Vigenère cipher support
    print("\nVigenère cipher support coming soon!")

# Run the main function
if __name__ == "__main__":
    main()
