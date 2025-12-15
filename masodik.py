def jelszo_erosseg(jelszo):
    if len(jelszo) == 0:
        return 0
    
    
    if 'jelszo' in jelszo or '123' in jelszo:
        return 0
    
    erosség = 1
    
    
    if len(jelszo) >= 5:
        erosség += 1
    
    
    if len(jelszo) >= 8:
        erosség += 2
    

    for char in jelszo:
        if char in '_-.':
            erosség += 2
    
    return erosség

# Példák a használatra
print(jelszo_erosseg("1234")) 
print(jelszo_erosseg("jelszo123"))
print(jelszo_erosseg("abcd"))  
print(jelszo_erosseg("abcd_"))  
print(jelszo_erosseg("abcd-123")) 
print(jelszo_erosseg("abcde123")) 
print(jelszo_erosseg("abcdefghi"))
print(jelszo_erosseg("abcdefgh."))