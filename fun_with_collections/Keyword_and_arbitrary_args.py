

def average_scores(*args, **kwargs):
    firstname = kwargs.get('first_name')
    lastname = kwargs.get('last_name')
    major = kwargs.get('major')
    var_count = 0
    total_val = 0
    for i in args:
        var_count +=1
        total_val += i
    gpa = str(total_val/var_count)
    print ('Result: Name ' + str(firstname) + ' '+ str(lastname) + ' ' + 'course = ' + str(major) + ' ' + 'with current average ' + gpa)

if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
