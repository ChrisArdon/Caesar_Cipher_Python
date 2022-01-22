alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#.Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(given_text, shift_amount, direction_needed):
    caesar_text = ""
    for letter in given_text:
        position = alphabet.index(letter)
        if direction_needed == "encode":
            new_position = position + shift_amount
            if new_position >= 25:
                new_position = position - 26 + shift_amount
        if direction_needed == "decode":
            new_position = position - shift_amount
        caesar_text += alphabet[new_position]
    print(f"The {direction_needed}d text is {caesar_text}")

#Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(given_text = text, shift_amount = shift, direction_needed = direction)