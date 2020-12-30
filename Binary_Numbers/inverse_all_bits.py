#working with complements doesnt work
#it just bring in negative numbers


def inverse_all_bits(n, number_of_bits):

    """
        Args:
            param1: number n
            param2: total number of bits. Sometimes we consider param1 n as having leading zeros 
                    we want to inverse as well
            
        Returns:
            an integer. All bits have been inversed
            If n has more bits than number_of_bits, we truncate n to have only number_of_bits, then we inverse that
    """    
    #if n has more bits, we just keep the first bits of n
    if n >= (1 << number_of_bits):
        n &= (1 << number_of_bits)

    mask = (1 << number_of_bits) - 1  # 1111...11 , all ones, number_of_bits 
    return n ^ mask


#example:

def ri():
    return int(input())

n = ri()
number_of_bits = ri()

inversed_n = inverse_all_bits(n, number_of_bits)

print('{:b}'.format(n).zfill(number_of_bits))
print('{:b}'.format(inversed_n).zfill(number_of_bits))
