# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_five = []

for i in a:
    if i < 5:
        less_than_five.append(i)
print(less_than_five)


def user_number():
    user_list = []
    number = input('number please')
    for i in a:
        if i < int(number):
           user_list.append(i)
    return user_list

print(user_number())