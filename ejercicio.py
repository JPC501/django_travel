def isPalindrome(x):
    if x < 0:
        return False

    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False


print(isPalindrome(122))
