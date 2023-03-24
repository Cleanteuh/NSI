def nombres_de_mots (phrase) : 
    mot = 0
    for i in phrase : 
        if i == ' ' : 
            mot += 1
    if phrase[len(phrase)-1] == '?' or phrase[len(phrase)-1] == '!' : 
        return mot
    else : 
        return mot + 1 

print(nombres_de_mots('Bonjour je suis nicolas ?'))  