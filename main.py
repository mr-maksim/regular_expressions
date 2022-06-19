from pprint import pprint
import csv
import re
with open("files/phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)
string = ''
for line in contacts_list:
    string+='\n'
    for item in line:
        string = item+','
        pattern = re.compile(r'(\,)*')
        result = re.sub(pattern,r'\1',string)
        pattern = re.compile('([А-Я][а-я]+)\s*\,*([А-Я][а-я]+)\s*\,*')
        result = re.sub(pattern,r'\1,\2,', result)
        pattern = re.compile('(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
        result = re.sub(pattern,r'+7(\2)\3-\4-\5', result)
        pattern = re.compile('\s*\(*(доб.)\s*(\d+)\)*\s*')
        result = re.sub(pattern,r' \1\2', result)
        print(result) 