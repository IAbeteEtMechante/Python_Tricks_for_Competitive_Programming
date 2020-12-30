def string_to_binary(ss):

    """
        Args:
            ss: string
            
        Returns:
            an integer, whose binary representation is ss
            
    """    

    return int(ss, 2)
    
#example

ss = input()
n = string_to_binary(ss)
print(n)
print("{:b}".format(n))