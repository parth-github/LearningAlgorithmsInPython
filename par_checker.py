import stackADT

def par_checker(symbol_string):
    balanced = True
    m = stackADT.Stack()
    for symbol in symbol_string:
        if balanced is True:
            if symbol == '(':
                m.push(symbol)
            else:
                if m.is_empty():
                    balanced = False
                else:
                    m.pop()
    
    if balanced and m.is_empty():
        return True
    else: return False


print(par_checker('((()))'))
print(par_checker('(()'))

