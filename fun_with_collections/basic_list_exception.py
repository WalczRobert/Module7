"""
Robert Walczak
The purpose of this program is to take the user input then display it in a list.
:return: returns list of user input
"""

number_list = []
def make_list():
    for x in range(3):
        try:
            user_num = int(get_input())
        except ValueError:
            raise ValueError("Please use numbers only.")
        else:
            if user_num < 1 or user_num > 50:
            # if 1 > user_num > 50: this would not work for some reason
                raise ValueError("Only numbers between 1 and 50 can be used.")
            else:
                number_list.insert(len(number_list), user_num)
    return number_list


def get_input():
    user_num = input("Please enter a number: ")
    return user_num


if __name__ == '__main__':
    print(make_list())