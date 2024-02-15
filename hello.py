letters = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar():
    hello = " "
    cipher = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
    if cipher.lower() == 'encode':
        word = input("Enter word: ")
        y = int(input("Enter the factor: "))
        for letter in word:
            x = letters.index(letter)
            hello = f"{hello}{letters[x+y]}"
        print(hello)
    elif cipher.lower() == 'decode':
        word = input("Enter encrypted word: ")
        y = int(input("Enter the factor: "))
        for letter in word:
            x = letters.index(letter)
            hello = f"{hello}{letters[x-y]}"
        print(hello)
    else:
        print("Invalid input!")
caesar()
              