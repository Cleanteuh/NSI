animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

def selection_enclos (table_animaux, num_enclos):
    tab = []
    for animaux in table_animaux : 
        if animaux['enclos'] == num_enclos :
            tab.append(animaux)
    return tab
        
