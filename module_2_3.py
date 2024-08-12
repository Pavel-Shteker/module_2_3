my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_position = 0
while list_position <= len(my_list) -1:
    if my_list[list_position] > 0:
        print (my_list[list_position])
        list_position += 1
    elif my_list[list_position] == 0:
        list_position += 1
    else:
        print ('Закончено.')
        break