""" Robert Walczak """



def write_to_file(info_file):
    f = open('student_info.txt', 'a')
    f.write(str(info_file))
    f.close()


def get_student_info(**scores):
    for key, value in scores.items():
        print(value)
    score = 0
    info_file = [scores]
    while score >= 0:
        try:
            score = int(input("Enter your score or enter -99 to quit: "))
        except ValueError:
            print("Entr numbers only for scores.")
        else:
            if score == -99:
                break
            else:
                info_file.append(score)
    write_to_file(info_file)


def read_from_file():
    f = open('student_info.txt', "r")
    line = f.readline()
    print(line)
    f.close()


if __name__ == '__main__':
    get_student_info(name='Robert')
    get_student_info(name='Jessica')
    get_student_info(name='Oliver')
    get_student_info(name='Noah')
    read_from_file()