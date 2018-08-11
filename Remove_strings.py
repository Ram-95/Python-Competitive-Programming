#Removing spaces in a string
def remove_spaces(string):
    string = string.replace(" ","")
    return string



n_inp = int(input())
for item in range(n_inp):
    word = input()
    print(remove_spaces(word))
