def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            # Shift uppercase letters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep spaces and special characters as they are
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            # Reverse shift uppercase letters
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            # Reverse shift lowercase letters
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Keep spaces and special characters as they are
            result += char
    return result

# Main Program
text_input = input("Enter the message: ")
shift_key = int(input("Enter shift key: "))

# Running Encryption
encrypted_text = encrypt(text_input, shift_key)
print("Encrypted message:", encrypted_text)

# Running Decryption
decrypted_text = decrypt(encrypted_text, shift_key)
print("Decrypted message:", decrypted_text)
