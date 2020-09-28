import stackADT

def convert_dec_bin(decimal_value):
    binary_value = ''
    m = stackADT.Stack()
    if type(decimal_value) is not int:
        return 'Value must be decimal integer'
    
    else:
        
        quotient = decimal_value
        
        while quotient != 0:
            reminder = quotient%2
            quotient = int(quotient/2)
            m.push(reminder)
            
            print(m.peek(), quotient, reminder)
        
        while not m.is_empty():
            binary_value = binary_value + str(m.pop())

    print('binary equivalent of '+ str(decimal_value) + ': ' + binary_value)

convert_dec_bin(233)
