def max_chars(string):
    str_dict = {}
    max = 0
    max_char = ''

    for char in string:
        if (not char in str_dict):
            str_dict[char] = 1
        else:
            str_dict[char] = str_dict[char] + 1
    
    for char in str_dict:
        if str_dict[char] > max:
            max = str_dict[char]
            max_char = char
    return max_char,max 
if __name__ == '__main__':
    string = 'Hello Therel!'
    print('Most Repeated Characters',max_chars(string))