def get_num_words(words):
    num = words.split()
    return len(num)

def get_letters(text):
    letters_dict = {}
    lowertext = text.lower()
    words = lowertext.split()
    for word in words:
        for letter in word:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict

def sort(dict):
    dict_list = []
    for dic in dict:
        if dic.isalpha() == True:
            new_dict = {"char": dic, "num": dict[dic]}
            dict_list.append(new_dict)
    def sort_on(dict):
        return dict["num"]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list