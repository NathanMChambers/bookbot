def count_words(string):
    list_words = string.split()
    return(len(list_words))

def count_letters(string):
    ouput_dict = {}
    string = string.lower()
    for char in string:
        if char not in ouput_dict:
            ouput_dict[char] = 1
        else:
            ouput_dict[char] += 1

    return ouput_dict

def sort_on(items):
    return items["num"]

def sort_dict(input_dict):
    working_list = []
    for char, num in input_dict.items():
        working_list.append({"char": char, "num": num})
    working_list.sort(reverse=True,key=sort_on)
    return working_list