
def age(a):
    if a == "5-10":
        a = 0
    elif a == "11-17":
        a = 1
    elif a == "18-22":
        a = 2
    elif a == "23-28":
        a = 3
    elif a == "29-35":
        a = 4
    elif a == "36-45":
        a = 5
    elif a == "46-55":
        a = 6
    elif a == "55-older":
        a = 7
    else:
        a = 0
    return a


def sex(b):
    if b == 'male':
        return 0
    elif b == 'female':
        return 1
    elif b == 'unspecified':
        return 2
    else:
        return 0


def eth(c):
    if c == 'American Indian or Alaska Native':
        return 0
    elif c == 'Asian':
        return 1
    elif c == 'Black or African American':
        return 2
    elif c == 'Hispanic or Latino':
        return 3
    elif c == 'Native Hawaiin':
        return 4
    elif c == 'White':
        return 5
    elif c == 'Middle Eastern':
        return 6
    else:
        return 0


def deg(y):
    if y == 'Uneducated':
        return 0
    elif y == 'Secondary':
        return 1
    elif y == 'Diploma':
        return 2
    elif y == 'Bachelor':
        return 3
    elif y == 'Master':
        return 4
    elif y == 'Doctorate':
        return 5
    else:
        return 0


def status(z):
    if z == 'Single':
        return 0
    elif z == 'Married':
        return 1
    elif z == 'Divorced':
        return 2
    elif z == 'Widowed':
        return 3
    else:
        return 0


def job(x):

    if x == 'Business and Financial Occupations':
        return 0
    elif x == 'Computer and Mathematical':
        return 1
    elif x == 'Architecture and Engineering':
        return 2
    elif x == 'Life, Physical and Social Science':
        return 3
    elif x == 'Community and Social Service':
        return 4
    elif x == 'Legal':
        return 5
    elif x == 'Educational Instruction and Library':
        return 6
    elif x == 'Arts, Design, Entertainment, Sports, and Media':
        return 7
    elif x == 'Healthcare Practitioners and Technical':
        return 8
    elif x == 'Food Preparation and Serving Related':
        return 9
    elif x == 'Building and Grounds Cleaning and Maintenance':
        return 10
    elif x == 'Personal Care and Service':
        return 11
    elif x == 'Sales and Related':
        return 12
    elif x == 'Office and Administrative Support':
        return 13
    elif x == 'Farming, Fishing, and Forestry':
        return 14
    elif x == 'Construction and Extraction':
        return 15
    elif x == 'Installation, Maintenance, and Repair':
        return 16
    elif x == 'Transportation and Material Moving':
        return 17
    else:
        return 0
