"""Robert Walczak"""



import array as arr


def sort_array(sorted_array):
    sortedarray = sorted_array.tolist()
    sortedarray.sort()
    sorted_array = arr.array('sortedarray', sortedarray)
    return sorted_array


def search_array(an_array, value):
    try:
        return an_array.index(value)
    except ValueError:
        return -1


if __name__ == '__main__':
    aaray = arr.array('d', [1.2, 6.3, 3.4])
    search_array(aaray, 2.5)
    print(sort_array(a))