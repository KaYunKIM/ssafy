# def is_palindrome(word):
#     for i in range(len(word)//2):
#         if word[i] != word[i-1]:
#
#     return word == word[::-1]
#
# print(is_palindrome('ooopppoooo'))

# def palindrome(word):
#     if list(word) == list(reversed(word)):
#         return True
#     return False
# print(palindrome('aaayaaa'))


def palindrome(word):
	if word == word[::-1]:
		return True
	return False

print(palindrome('aaayyaaa'))


# a = input()
# print(a[1:3:-1])
# print(a[0:7:-1])
# print(a[::-1])