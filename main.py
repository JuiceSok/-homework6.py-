my_dict = {'Денис': 2000, 'Саша': 1888, 'таня ': 2010}
print(my_dict)
print(my_dict['Денис'])
print(my_dict.get('Даша'))

my_dict.update({'Паша': 1999,
                'Артем': 2009})
a = my_dict.pop('Паша')
print('Deleted value: ', a)
print('Modified dictionary:', my_dict)


my_set = {1, 2, 3, 5, 6, 'Star', 20, 1, 2, 'Star', 2, 5, 6,}
print(my_set)
my_set.add((4, 33))
my_set.add(4)
my_set.add(55)
print(my_set)
my_set.discard(55)
print(my_set)
