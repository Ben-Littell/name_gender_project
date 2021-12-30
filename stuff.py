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
    alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U',
                 'V', 'W', 'X', 'Y', 'Z']
    for letter in alphabet1:
        new_list.append(len(name_dict[letter]) / names_len)
    return new_list


def use_condition(names_1, names_2, list_condition_1, condition2, index):
    boys_tp = 0
    boys_fp = 0
    boys_fn = 0
    boys_tn = 0
    girls_tp = 0
    girls_fp = 0
    girls_fn = 0
    girls_tn = 0
    u_b = []
    u_g = []

    for name in names_1:
        if name[index] in list_condition_1:
            boys_tp += 1
            girls_tn += 1
        elif name[index] in condition2:
            boys_fn += 1
            girls_fp += 1
        else:
            u_b.append(name)
    for name in names_2:
        if name[index] in list_condition_1:
            boys_fp += 1
            girls_fn += 1
        elif name[index] in condition2:
            girls_tp += 1
            boys_tn += 1
        else:
            u_g.append(name)
    return boys_tp, boys_fn, boys_fp, boys_tn, girls_tp, girls_fn, girls_fp, girls_tn, u_b, u_g


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

b_tp, b_fn, b_fp, b_tn, g_tp, g_fn, g_fp, g_tn, unknown_b, unknown_g = use_condition(male_names, female_names,
                                                                                     ['L', 'N', 'R', 'S', 'T'],
                                                                                     ['A', 'E', 'I'], -1)

b_tp2, b_fn2, b_fp2, b_tn2, g_tp2, g_fn2, g_fp2, g_tn2, unknown_b2, unknown_g2 = use_condition(unknown_b, unknown_g,
                                                                                               ['D', 'O'], ['Y'], -1)

print(f'Boys TP: {b_tp2}')
print(f'Boys FN: {b_fn2}')
print(f'Boys FP: {b_fp2}')
print(f'Girls TN: {b_tn2}')
print(f'Boys Unknown: {len(unknown_b2)}')
print()
print(f'Girls TP: {g_tp2}')
print(f'Girls FN: {g_fn2}')
print(f'Girls FP: {g_fp2}')
print(f'Boys TN: {g_tn2}')
print(f'Girls Unknown: {len(unknown_g2)}')
