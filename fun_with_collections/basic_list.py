"""
Robert Walczak
This program makes a list from user input
:param input - integer input by user

"""


list=[]
def make_list():
    for x in range(3):
        x = int(get_input())
        list.append(x)
    print(list)
    return list

def get_input():
    print('Input a number: ')
    try:
        input_user = int(input(""))
    except:
        print('Non Numeric Data Entered')
    return input_user

if __name__ == '__main__':
    make_list()