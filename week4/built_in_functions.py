# Activity 1: ASCII Value

print("built_in_functions.py")
letter = input("Please enter a letter:\n")
value = ord(letter)
if len(letter) == 1:
    print(f"The ASCII code for {letter} is {value}.")
else:
    print("Too many letters!")
print("Program Ended!\n")

########################################
# Activity 2: ASCII character

print("Program started!")
print("Please enter an ASCII code:")
code = abs(int(input()))
character = chr(code)
if code in range(32,127):
    print(f"The character represented by the ASCII code {code} is: {character}")
else:
    print("Wrong value!")
print("Program Ended!")