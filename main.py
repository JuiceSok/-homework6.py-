my_dict = {'Денис': 2000, 'Саша': 1888, 'таня ': 2010}
print(my_dict)
print(my_dict['Денис'])
print(my_dict.get('Даша'))
my_dict.update({'Паша': 1999,
                'Артем': 2009})
print(my_dict)
del my_dict['Паша']
print(my_dict['Артем'])
print(my_dict)


