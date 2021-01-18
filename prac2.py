#q2) WAP to take a word from user and check if it is a palindrome
word = input("Enter a word :")
if word.lower() == word[::-1].lower():
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
