def decoding_message(parts) :
    ## initialisation
    debut = [i for i in parts if i.startswith('A')]
    parts.remove(debut[0])
    n = len(parts)
    
    while n != 0 : 
        last_character = debut[-1][-1]
        tmp = [i for i in parts if i.startswith(last_character)]
        debut.append(tmp[0])
        parts.remove(tmp[0])
        n = n - 1
        
    ## suppression des balises
    for i in range(len(debut)) :
        debut[i] = debut[i][1:-1]
    return "".join(debut)
