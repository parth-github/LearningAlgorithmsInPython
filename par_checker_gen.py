import stackADT

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

def par_checker_gen(symbol_string):
    balanced = True
    m = stackADT.Stack()
    for symbol in symbol_string:
        if balanced is True:
            if symbol in '([{':
                m.push(symbol)
            else:
                if m.is_empty():
                    balanced = False
                else:
                    top = m.pop()
                    if not matches(top, symbol):
                        balanced  =  False
    
    if balanced and m.is_empty():
        return True
    else: return False


print(par_checker_gen('{{([][])}()}'))
print(par_checker_gen('[{()}]'))