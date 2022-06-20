import csv
import re
from config import PHOHE, PHONE_SUB

with open("files/phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def get_list():
    inter_list = []
    for item in contacts_list[1:]:
        name = ' '.join(item[:3]).split(' ')
        result = [name[0], name[1], name[2], item[3], item[4],
                  re.sub(PHOHE, PHONE_SUB, item[5]), item[6]]
        inter_list.append(result)
    return inter_list


def filter(p_list):
    for item in p_list:
        for new_item in p_list:
            if item[0] == new_item[0] and item[1] == new_item[1]:
                if item[2] == "":
                    item[2] = new_item[2]
                if item[3] == "":
                    item[3] = new_item[3]
                if item[4] == "":
                    item[4] = new_item[4]
                if item[5] == "":
                    item[5] = new_item[5]
                if item[6] == "":
                    item[6] = new_item[6]
    return p_list


def new_list(old_list):
    new_list = [['lastname', 'firstname', 'surname',
                 'organization', 'position', 'phone', 'email']]
    for item in old_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


with open("files/phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list(filter(get_list())))
