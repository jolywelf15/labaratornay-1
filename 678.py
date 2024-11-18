def add_zero_to_middle():
    number = int(input('Введите число: '))

    str_number = str(number)  
    middle_index = len(str_number) // 2 

  
    if len(str_number) % 2 == 0: 
        str_number = str_number[:middle_index] + '0' + str_number[middle_index:]
    else: 
        str_number = str_number[:middle_index] + '0' + str_number[middle_index:]

    number = int(str_number)  

    print('Число :', number)

add_zero_to_middle()
