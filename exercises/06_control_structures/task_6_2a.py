# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_adr = input("введите ip-адрес: ")

ip_address_correct = True



for i in ip_adr:
    if i in ["0","1","2","3","4","5","6","7","8","9","."]:
            pass
    else: 
        print("Неправильный IP-адрес")
        ip_address_correct = False
        break


octets = ip_adr.split(".")
octets_int = []

for octet in octets:
        octets_int.append(int(octet))

if len(ip_list) != 4:
    ip_address_correct = False
    
    
if ip_address_correct == True:
    
    for octet in octets_int:
        if 0 <= octet <= 255:
            continue
        else:
            print('Неправильный IP-адрес')


