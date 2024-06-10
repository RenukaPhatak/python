# text2numbers.py
#  A program to convert a textual message into a sequence of numbers, utilizing the underlying Unicode encoding
message = input("Please enter the message to encode:")

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")
    
    # Get the message to encode
    message = input("Please enter the message to encode:")
    print("\nHere are the Unicode codes:")

    # Loop through the message and printout the Unicode values
    for ch in message:
        print(ord(ch), end = "")

      # blank line before prompt
main()

s = "hello, I came here for an arguement"
s.capitalize()
s.title()
s.upper()    
s.replace("I", "you")
s.center(30)
s.count("e")  
"".join(["Number","one","the","Larch"])
"spam".join(["Number", "one,","the","Larch"])

