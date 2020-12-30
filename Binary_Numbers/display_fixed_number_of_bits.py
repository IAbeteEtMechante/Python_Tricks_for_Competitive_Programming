def fixed_number_of_bits(n, number_of_bits):

    """
        Args:
            param1: number n
            param2: total number of bits. Sometimes we consider param1 n as having leading zeros 
            
        Returns:
            a string
            
    """    
    #if n has more bits, we truncate n
    if n >= (1 << number_of_bits):
        mask = (1 << number_of_bits) - 1 # 11111..1111
        n &= mask
    
    return '{:b}'.format(n).zfill(number_of_bits)





#example:

def ri():
    return int(input())

n = ri()
number_of_bits = ri()

print(fixed_number_of_bits(n, number_of_bits))