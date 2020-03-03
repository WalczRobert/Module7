"""Robert Walczak
:return: the index of item in list or item not found
:param list: list from user input
:param number: to the search index
"""

def sort_list(list):
    try:
        list.sort()
    except ValueError:
        return -1


def search_list(list, number):
    try:
        index_listing = list.index(number)
    except ValueError:
        return -1
    else:
        return index_listing


if __name__ == '__main__':
    sort_list()
    list = [5, 10, 15, 20, 25]
    sort_list(a_list)
    print(a_list)