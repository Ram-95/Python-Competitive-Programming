#Leap Year
def leap_year(year):
    if (year%4 ==0 and year%100 != 0) or (year%400 == 0):
        return 'Yes'
    else:
        return 'No'


n_inp = int(input())
for item in range(0,n_inp):
    n = int(input())
    print(leap_year(n))
