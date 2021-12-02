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


def plot_data(title, x1, y1, plot_code='-xr'):
    plt.ylabel(title)
    plt.plot(x1, y1, plot_code)
    plt.axis([0, 26, 0, 1])


def get_percent(name_dict, names_len):
    new_list = []
    alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']
    for letter in alphabet1:
        new_list.append(len(name_dict[letter])/names_len)
    return new_list


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
plt.subplot(2, 1, 1)
plot_data('Male First', alphabet, male_percent_list_first)
plt.subplot(2, 1, 2)
plot_data('Female First', alphabet, female_percent_list_first)
plt.show()

plt.subplot(2, 1, 1)
plot_data('Male Last', alphabet, male_percent_last)
plt.subplot(2, 1, 2)
plot_data('Female Last', alphabet, female_percent_last)
plt.show()

plt.subplot(2, 1, 1)
plot_data('Male 2nd', alphabet, male_percent_second)
plt.subplot(2, 1, 2)
plot_data('Female 2nd', alphabet, female_percent_second)
plt.show()

plt.subplot(2, 1, 1)
plot_data('Male 2nd Last', alphabet, male_percent_second_last)
plt.subplot(2, 1, 2)
plot_data('Female 2nd Last', alphabet, female_percent_second_last)
plt.show()

