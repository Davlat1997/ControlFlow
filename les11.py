
word_1 = input("1-so`zni kiriting: ")

is_palindrome = word_1.lower() == word_1[::-1].lower()


print(is_palindrome)