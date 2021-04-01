def split(string):
    result = []
    tmp = ""
    counter = 0
    for char in string:
        if char == '{':
            counter += 1
            tmp += char
        elif char == '}':
            counter -= 1
            tmp += char
            if counter == 0:
                result.append(tmp)
                tmp = ""
        elif counter > 0:
            tmp += char
    return result
