def is_palindrome(s: str) -> bool:
    for i in range(int(len(s)/2)):
        if s[i] != s[-1-i]:
            return False
    return True


s = input("Write word:\n")
if is_palindrome(s):
    print("Is Palendrom")
else:
    print("Not palendrom")


