size = int(input('Размер жеского диска: '))
count_cache = int(input('Размер кэша: '))
сount_users = int(input('Количество пользователей: '))
free_space = size - count_cache * сount_users
print('Свободное место: ', free_space)