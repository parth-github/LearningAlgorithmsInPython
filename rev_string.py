import stackADT
def rev_string(item):
    m = stackADT.Stack()
    rev_str = str()
    for s in item:
        m.push(s)
        

    while not m.is_empty():
        rev_str += m.pop()
    
    print(rev_str)
    return rev_str

rev_string('Saronica Pal')


