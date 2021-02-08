# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
prefix, metric, _, hop, update, inf = ospf_route.replace(',', '').split()

template = '''
Prefix             {}
AD/Metric          {}
Next-Hop           {}
Last update        {}
Outbound Interface {}
'''

# перед разбивкой из строки удаляю "via" и ","
ospf_list = ospf_route.replace('via','').replace(',','').split()
print(len(ospf_list),' elements in ',ospf_list)
print(template.format(*ospf_list))

print(f'''
Prefix             {prefix}
Ad/Metric          {metric}
Next-Hop           {hop}
Last update        {update}
Outbound Interface {inf}
''')

