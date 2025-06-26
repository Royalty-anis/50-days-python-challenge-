def S_names(names):
    Snames = {}
    for name in names:   
        if name[0].lower() == 's':
            if name in Snames:
                Snames[name] += 1
            else:
                 Snames[name] = 1
        
        else:
            pass
    return Snames 
