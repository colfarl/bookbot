def get_num_words(text):
    return len(text.split())

def get_char_dict(text):
    res = dict()
    for c in text:
        lowered = c.lower()
        if lowered not in res:
            res[lowered] = 0
        res[lowered] += 1
    return res

def sort_on(item):
    return item['amt']

def sort_char_dict(char_dict):
    arr = []
    for key in char_dict.keys():
        arr.append({"char": key, "amt": char_dict[key]})
    arr.sort(reverse=True, key=sort_on)
    return arr
    