def palindromeCheck(input):
    palindrome = True
    for digit in range(0, len(str(input)) // 2):
        if str(input)[digit] != str(input)[len(str(input))-digit-1]:
            palindrome = False
    return palindrome

def largestPalindromeProduct(digits):
    maxNum = 0
    for x in range(0, digits):
        maxNum += ((10**x) *9)
    minNum = 0
    for x in range(0, digits-1):
        minNum += ((10**x) *9)
    num1, num2 = maxNum, maxNum
    maxPalindromeProduct = 0
    while num1 > minNum:
        while num2 > minNum:
            product = num1*num2
            print(str(num1) + "x" + str(num2) + "=" + str(product))
            if palindromeCheck(product):
                if product > maxPalindromeProduct:
                    maxPalindromeProduct = product
            num2 -= 1
        num1 -= 1
        num2 = maxNum
    return maxPalindromeProduct

print(largestPalindromeProduct(3))
