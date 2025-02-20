
def Palindrome(s):
    return s == s[::-1]

s = "MOM"
ans = Palindrome(s)

if ans:
    print("Yes")
else:
    print("No")