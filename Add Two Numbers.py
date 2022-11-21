def addTwoNumbers(one, two):
    one.reverse()
    two.reverse()
    one = int("".join([str(i) for i in one]))
    two = int("".join([str(i) for i in two]))
    output = [int(i) for i in list(str(one + two))]
    output.reverse()
    return output
    
    
    

print(addTwoNumbers([9,9,9,9], [9,9,9,9,9,9,9]))
