def most_freq(str, n):
    dict = {}
    punc = [' ', ',', '.', '-', '?', ';' , ':']
    for char in str:
        if not char in punc:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    keys = []
    for key in dict:
        if dict[key] >= n:
            keys.append(key)
    keys.sort()
    skey = ""
    for char in keys:
        skey += char
    return skey

if __name__ == '__main__':
    str = 'today is that saturday'
    n = 3
    keys = most_freq(str, n)
    print(keys)