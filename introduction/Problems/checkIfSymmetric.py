'''
Goal: To create a program which check if the word is palindrome or symmetric or both or none

khokho is a symmetrical
reviver is a palindrome
amaama is symmetrical and also palindrome

example output:
>> word is symmetric
>> word is palindrome


'''

def checkPalindrome(word):
    newWord = ''
    for i in range(len(word)):
        newWord += word[-i + -1]
        
    print(newWord)
    
    return word == newWord
        
while True:
    print(checkPalindrome(input('Check if palindrome: ')))