#Palindrome Stirng
import sys
def palindrome(string):
    string_rev = string[::-1]
    if string_rev == string:
        return 'Yes'
    else:
        return 'No'

n_inp = int(input())
for item in range(n_inp):
    size = int(input())
    n = input()
    if len(n) > size:
        print("Size Exceeded.")
        sys.exit()
    print(palindrome(n))
