# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


with open('CAM_table.txt') as f:
    result_list = []
    vlans = []
    for line in f: 
        line_list = line.strip('-').split()
        #print(line_list)
        if len(line_list) == 4:
            line_list.pop(2)
            line_list[0] = int(line_list[0])
            result_list.append(line_list)
            
    #print(result_list)
            #vlan, mac, intf = line_list
            #print(f'{vlan:8} {mac:20} {intf:10}')

    #result_list.sort(key=None)
    result_list = sorted(result_list)
    #print (result_list)
    for sring in result_list:
        vlan, mac, intf = sring
        #print(f'{vlan:<8} {mac:20} {intf:10}')
        
    vlan_str = input('Enter VLAN number: ')
    for line in result_list:
        if int(vlan_str) in line:
            vlan, mac, intf = line
            print(f'{vlan:<8} {mac:20} {intf:10}')
