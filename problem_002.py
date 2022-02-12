def sum_f():   
    _sum = 0         
    a, b = 0, 1
    while b < 4_000_000:
        a, b = b, a + b
        if b % 2 == 0:
            _sum += b
    return _sum


print(sum_f())
    


        
