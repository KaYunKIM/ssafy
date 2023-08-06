# Day03_WS

### 1. 

```
def palindrome(word):
    if list(word) == list(reversed(word)):
        return True
    return False

print(palindrome('aaayaaa'))
```

```
def palindrome(word):
	if word == word[::-1]:
		return True
	return False

print(palindrome('aaayyaaa'))	
```

