# username.py
# Simple string processing program to generate username.

def main():
    print("This program generates computer usernames. \n")
# get users first and last names
first = input("Please enter your first name(all lowercase):")
last = input("Please enter your last name(all lowercase):")

# concatenate first initial with 7 chars of the last name.
username = first[0] + last[:7]

# output the username
print("Your username is:", username)
main()
