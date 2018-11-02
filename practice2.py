
str = "Mahmoud"

def factorial(n):
    if n > 1 :
        return n * factorial(n-1)
    else:
        return 1

def fact(n):
    x = 1
    for i in range(1,n+1):
        x = i * x
    return x

def volmn(s):
    for i in range(0,len(s)):
        if(s[i] == "a" | s[i] == "e" | s[i] == "u" | s[i] == "o" | s[i] == "i"):
            print(s[i])
    return
def vowel(word):
    for i in word:
        if i in ("a","e","i","o","u"):
            print(i)
    return

def isPalindrome(word):
    left = 0
    right = len(word)-1
    while(right >= left):
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome("aza"))