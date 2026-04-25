# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


#with open('config_sw1.txt') as src,  open('result.txt', 'w') as dest:
#    for line in src:       
#        if not line.startswith('!'):
#            line_list = line.split()
#            if list(set(line_list) & set(ignore)) == []:
#                dest.write(line)
#

from sys import argv

ignore = ["duplex", "alias", "configuration"]

src_file = argv[1]
dst_file = argv[2]

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            dst.write(line)
        
