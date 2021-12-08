import matplotlib.pyplot as plt


def open_file(file_name):
    new_list = []
    with open(file_name) as file:
        lines = file.readlines()
        for item in lines[1:]:
            stripped = item.strip()
            splitted = stripped.split()
            new_list.append(splitted[0])
        return new_list


def letter_position(name_list, pos):
    new_dict = {}
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    for letter in letters:
        new_dict[letter] = []
        for name in name_list:
            if name[pos] == letter:
                new_dict[letter].append(name)
    return new_dict


def plot_data(title, x1, y1, x2, y2, y_label, x_label, plot_code1='-b', plot_code2='-r'):
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.plot(x1, y1, plot_code1, x2, y2, plot_code2)
    plt.axis([0, 26, 0, 1])


def get_percent(name_dict, names_len):
    new_list = []
    alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']
    for letter in alphabet1:
        new_list.append(len(name_dict[letter])/names_len)
    return new_list


def use_condition(names_1, names_2, list_condition_1, list_condition_2, index):
    list_s1 = []
    list_ns1 = []
    list_s2 = []
    list_ns2 = []

    for name in names_1:
        if name[index] in list_condition_1:
            list_s1.append(name)
        else:
            list_ns1.append(name)
    for name in names_2:
        if name[index] in list_condition_1:
            list_s1.append(name)
        else:
            list_ns1.append(name)
    for name in names_1:
        if name[index] in list_condition_2:
            list_s2.append(name)
        else:
            list_ns2.append(name)
    for name in names_2:
        if name[index] in list_condition_2:
            list_s2.append(name)
        else:
            list_ns2.append(name)
    return list_s1, list_ns1, list_s2, list_ns2


####################
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
####################
# OPEN AND LENGTH #
male_names = open_file('male_names.txt')
male_names_len = len(male_names)

female_names = open_file('female_names.txt')
female_names_len = len(female_names)
####################
# FIRST LETTERS #
male_first = letter_position(male_names, 0)
female_first = letter_position(female_names, 0)
male_percent_list_first = get_percent(male_first, male_names_len)
female_percent_list_first = get_percent(female_first, female_names_len)
####################
# LAST LETTERS #
male_last = letter_position(male_names, -1)
female_last = letter_position(female_names, -1)
male_percent_last = get_percent(male_last, male_names_len)
female_percent_last = get_percent(female_last, female_names_len)
####################
# 2ND LETTER #
male_second = letter_position(male_names, 1)
female_second = letter_position(male_names, 1)
male_percent_second = get_percent(male_second, male_names_len)
female_percent_second = get_percent(female_second, female_names_len)
####################
# 3RD LETTER #
male_second_last = letter_position(male_names, -1)
female_second_last = letter_position(female_names, -1)
male_percent_second_last = get_percent(male_second_last, male_names_len)
female_percent_second_last = get_percent(female_second_last, female_names_len)
####################
# plot_data('First Letter', alphabet, male_percent_list_first, alphabet, female_percent_list_first, 'Percent', 'Letter')
# plt.show()
#
# plot_data('Last Letter', alphabet, male_percent_last, alphabet, female_percent_last, 'Percent', 'Letter')
# plt.show()
#
# plot_data('2nd Letter', alphabet, male_percent_second, alphabet, female_percent_second, 'Percent', 'Letter')
# plt.show()
#
# plot_data('2nd to Last Letter', alphabet, male_percent_second_last, alphabet, female_percent_second_last, 'Percent',
#           'Letter')
# plt.show()
####################

