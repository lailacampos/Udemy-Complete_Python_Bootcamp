from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, direction):
  output_text = ""

  if shift_amount > len(alphabet):
    shift_amount = shift_amount % len(alphabet)

  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)

      if direction == "encode":
        new_position = position + shift_amount

        if new_position > len(alphabet) - 1:
          new_position = new_position - len(alphabet)

      elif direction == "decode":
        new_position = position - shift_amount

      output_text += alphabet[new_position]

    else:
      output_text += letter

  print(f"The {direction}d text is {output_text}")

print(logo)

restart = True

while restart:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction != "encode" and direction != "decode":
    print("\nSorry, invalid input.")
  else:
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))
  
    caesar(text, shift, direction)

  user_choice = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if user_choice == "no":
      restart = False

print("\nGoodbye!\n")