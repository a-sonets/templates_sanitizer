import os
import glob
import re


def get_all_tags_classes(string):
    re1 = '.*?'
    re2 = '(class=)'
    re4 = '"(.*?)"'
    rg = re.compile(re1+re2+re4, re.IGNORECASE | re.DOTALL)

    return convert_regex_result_to_set(re.findall(rg, string))


def get_all_tags_ids(string):
    re1 = '.*?'
    re2 = '(id=)'
    re3 = '"(.*?)"'
    rg = re.compile(re1+re2+re3, re.IGNORECASE | re.DOTALL)

    return convert_regex_result_to_set(re.findall(rg, string))


def convert_regex_result_to_set(regex_result):
    results = set()
    for sub_result in regex_result:
        for rg_result in sub_result[1].split(' '):
            results.add(rg_result)
    return results


files = glob.glob(os.getcwd() + "/templates/*.html")
buffer = ''

for file_name in files:
    f = open(file_name, 'r')
    buffer += f.read() + " \n"
    f.close()

buffer = buffer.replace("\n", '').strip().replace("'", '').replace('{{', '').replace('}}', '').replace('{%', '').replace('%}', '')

html_classes = get_all_tags_classes(buffer)
html_ids = get_all_tags_ids(buffer)

f = open(os.getcwd() + '/results.txt', 'w+')

f.write('___CLASSES___\n')
for res in html_classes:
    f.write('.' + res + '\n')
f.write('\n___IDS___\n')
for res in html_ids:
    f.write("#" + res + '\n')
f.close()

# print buffer
