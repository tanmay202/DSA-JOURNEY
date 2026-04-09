a=input("Enter a string:").lower().replace(" ", "")
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")