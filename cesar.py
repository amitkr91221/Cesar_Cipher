from art import logo
print(logo)

def cesar_cipher(text, shift, operation):
    cesar = ""
    if operation == "decode":
        shift *= -1
    for letters in text:
        if letters in words:
            pos = words.index(letters)
            new_pos = pos + shift
            cesar += words[new_pos]
        else:
            cesar += letters
    print(f"The {operation}d text is: {cesar}")

con = "yes"
while con == "yes":
    words = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    operation = input("What operation would you like to perform? Encode or Decode....\n").lower()
    text = input("Enter the text\n").lower()
    shift = int(input("Enter the shift enter\n")) % 26
    
    cesar_cipher(text ,shift, operation)
    
    con = input("Do you want to continue? Yes or No\n").lower()
print("Thankyou for using the Cesar Cipher program.....")