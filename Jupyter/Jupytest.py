
def je_palindrom(retezec):
    print("START")    
    """
    # pomoci techto prikazu muzete nastavit breakpoint a krokovat kod:
    import pdb
    pdb.set_trace()
    """
    if len(retezec) < 2:
        print(retezec + " IS")
        return True
    
    for index in range(int(len(retezec)/2)):
        print(retezec[index] + "[" + str(index)+"] = " + retezec[len(retezec)-1-index]+"["+ str(index)+ "]"+ " from " +retezec)
        if retezec[index] is not retezec[len(retezec)-1-index]:
            
            return False
    print("THIS IS "+retezec)
    return True






assert je_palindrom('')
assert je_palindrom('a')
assert je_palindrom('aa')
assert je_palindrom('aaa')
assert je_palindrom('aba')
assert not je_palindrom('abc')
assert not je_palindrom('abcd')
assert not je_palindrom('palindrom')
assert je_palindrom('kobylamamalybok')
assert je_palindrom('kobylammalybok')


