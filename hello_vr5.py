from collections import Counter
import re
from typing import Tuple, Dict, List

class CipherTool:
    ENGLISH_FREQ = {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 
        'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3
    }

    def __init__(self):
        self.history: List[Tuple[str, str, str]] = []  # [(operation, input, output)]

    @staticmethod
    def caesar_decrypt(text: str, shift: int) -> str:
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            else:
                decrypted_text += char
        return decrypted_text

    @staticmethod
    def caesar_encrypt(text: str, shift: int) -> str:
        return CipherTool.caesar_decrypt(text, -shift)

    def frequency_analysis(self, text: str) -> Dict[str, float]:
        # Count only alphabetic characters
        counter = Counter(char.upper() for char in text if char.isalpha())
        total_chars = sum(counter.values())
        
        if total_chars == 0:
            return {}
            
        freq_percentages = {char: (count / total_chars) * 100 
                          for char, count in counter.items()}
        return dict(sorted(freq_percentages.items(), key=lambda x: -x[1]))

    def suggest_caesar_shift(self, text: str) -> int:
        """Suggest the most likely Caesar shift based on letter frequency analysis."""
        freq = self.frequency_analysis(text)
        if not freq:
            return 0
            
        most_common = max(freq.items(), key=lambda x: x[1])[0]
        # Assume 'E' is the most common letter in English
        suggested_shift = (ord(most_common) - ord('E')) % 26
        return suggested_shift

    @staticmethod
    def generate_vigenere_key(msg: str, key: str) -> str:
        key = list(key.upper())  # Convert key to uppercase
        if not key:
            return msg
            
        key_length = len(key)
        key_as_list = []
        msg_index = 0

        for char in msg:
            if char.isalpha():
                key_as_list.append(key[msg_index % key_length])
                msg_index += 1
            else:
                key_as_list.append(char)

        return "".join(key_as_list)

    def encrypt_vigenere(self, msg: str, key: str) -> str:
        if not key:
            return msg
            
        key = self.generate_vigenere_key(msg, key)
        encrypted_text = []

        for i, char in enumerate(msg):
            if char.isalpha():
                # Determine the case of the original character
                base = 'A' if char.isupper() else 'a'
                # Convert to 0-25 range, perform shift, and convert back
                shift = (ord(char.upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
                encrypted_text.append(chr(shift + ord(base)))
            else:
                encrypted_text.append(char)

        return "".join(encrypted_text)

    def decrypt_vigenere(self, msg: str, key: str) -> str:
        if not key:
            return msg
            
        key = self.generate_vigenere_key(msg, key)
        decrypted_text = []

        for i, char in enumerate(msg):
            if char.isalpha():
                base = 'A' if char.isupper() else 'a'
                shift = (ord(char.upper()) - ord(key[i].upper()) + 26) % 26
                decrypted_text.append(chr(shift + ord(base)))
            else:
                decrypted_text.append(char)

        return "".join(decrypted_text)

    def add_to_history(self, operation: str, input_text: str, output_text: str):
        self.history.append((operation, input_text, output_text))

def main():
    cipher_tool = CipherTool()
    
    while True:
        print("\n=== Cryptography Tool ===")
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. Frequency Analysis")
        print("4. View Operation History")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice == '4':
            print("\n=== Operation History ===")
            for op, input_text, output_text in cipher_tool.history:
                print(f"\nOperation: {op}")
                print(f"Input: {input_text}")
                print(f"Output: {output_text}")
            continue

        text = input("\nEnter the text: ").strip()
        if not text:
            print("Error: Empty text!")
            continue

        if choice == '1':
            print("\n1. Encrypt")
            print("2. Decrypt")
            print("3. Brute Force")
            sub_choice = input("Enter your choice (1-3): ")
            
            if sub_choice in ['1', '2']:
                try:
                    shift = int(input("Enter shift value (0-25): "))
                    if not 0 <= shift <= 25:
                        raise ValueError
                except ValueError:
                    print("Error: Invalid shift value!")
                    continue
                
                if sub_choice == '1':
                    result = cipher_tool.caesar_encrypt(text, shift)
                    cipher_tool.add_to_history(f"Caesar Encryption (shift={shift})", text, result)
                else:
                    result = cipher_tool.caesar_decrypt(text, shift)
                    cipher_tool.add_to_history(f"Caesar Decryption (shift={shift})", text, result)
                print(f"\nResult: {result}")
                
            elif sub_choice == '3':
                suggested_shift = cipher_tool.suggest_caesar_shift(text)
                print(f"\nSuggested shift (based on frequency analysis): {suggested_shift}")
                print("\nAll possible shifts:")
                for shift in range(26):
                    decrypted = cipher_tool.caesar_decrypt(text, shift)
                    print(f"Shift {shift:2d}: {decrypted}")

        elif choice == '2':
            key = input("Enter the key: ").strip()
            if not key:
                print("Error: Empty key!")
                continue
                
            print("\n1. Encrypt")
            print("2. Decrypt")
            sub_choice = input("Enter your choice (1-2): ")
            
            if sub_choice == '1':
                result = cipher_tool.encrypt_vigenere(text, key)
                cipher_tool.add_to_history(f"Vigenère Encryption (key={key})", text, result)
            elif sub_choice == '2':
                result = cipher_tool.decrypt_vigenere(text, key)
                cipher_tool.add_to_history(f"Vigenère Decryption (key={key})", text, result)
            else:
                print("Invalid choice!")
                continue
                
            print(f"\nResult: {result}")

        elif choice == '3':
            frequencies = cipher_tool.frequency_analysis(text)
            print("\nCharacter frequencies:")
            for char, freq in frequencies.items():
                print(f"{char}: {freq:.2f}%")
                
            print("\nExpected frequencies in English:")
            for char, freq in CipherTool.ENGLISH_FREQ.items():
                print(f"{char}: {freq:.2f}%")
            
            cipher_tool.add_to_history("Frequency Analysis", text, 
                                     str(dict(list(frequencies.items())[:10])))

        else:
            print("Invalid choice!")
    print("Hello")
#hello
if __name__ == "__main__":
    main()