#Palindrome 
def checkPalindrome(strParam):
    strParam == strParam.lower()
    if strParam == strParam[::-1]:
       print(True)
    else:
        print(False)

checkPalindrome(input("Enter String"))
