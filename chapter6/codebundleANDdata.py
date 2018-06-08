#function to filter the list
def sanitize(data):
    if '-' in data:
        splitter = '-'
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (min , sec) = data.split(splitter)
    return (min + '.' + sec)

# to open and split the file
def get_coach_data(filename):
    try:
        with open(filename) as fname:
            data = fname.readline().strip().split(',')
            data_dict = dict()
            data_dict['Name'] = data.pop(0)
            data_dict['dob'] = data.pop(0)
            data_dict['timings'] = str(sorted(set(sanitize(t) for t in data))[0:3])
            return data_dict
    except IOError:
        print("File Error")
        return (None)

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
# sarah_data = dict()
# sarah_data['Name'] = sarah.pop(0)
# sarah_data['dob'] = sarah.pop(0)
# sarah_data['timings'] = sorted(set([sanitize(t) for t in sarah]))
print(james['Name'] + " born on : " + james['dob'] + " have fastest 03 running time as : "+ james['timings'])
print(julie['Name'] + " born on : " + julie['dob'] + " have fastest 03 running time as : "+ julie['timings'])
print(mikey['Name'] + " born on : " + mikey['dob'] + " have fastest 03 running time as : "+ mikey['timings'])
print(sarah['Name'] + " born on : " + sarah['dob'] + " have fastest 03 running time as : "+ sarah['timings'])