def find_entrance_and_floor(apartment_number):
  
    apartments_per_entrance = 9 * 4  # 9 floors * 4 apartments per floor
    
    
    entrance_number = (apartment_number - 1) // apartments_per_entrance + 1
    

    floor_number = ((apartment_number - 1) % apartments_per_entrance) // 4 + 1
    
    return entrance_number, floor_number
