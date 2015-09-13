__author__ = 'cwang'

def suffix_match(my_string):
    sz = len(my_string)
    ch0 = my_string[0]
    match = [i for i, ch in enumerate(my_string) if ch == ch0]
    count = len(match)
    for i in range(1, sz):
        temp = []
        ch = my_string[i]
        for j in range(len(match)):
            if match[j] + 1 < sz and my_string[match[j] + 1] == ch:
                temp.append(match[j] + 1)
                count += 1
        match = temp
    return(count)

if __name__ == '__main__':
    my_string = 'abab'
    rlt = suffix_match(my_string)
    print(rlt)