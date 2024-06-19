cat_colours = { 
    'Dave': 'brown', 
    'Aragorn': 'grey',
    'Boris': 'orange',
    'Tart': 'orange',
    'Gandalf': 'white'
    }

names = [ name.upper() 
          for name in cat_colours
          if cat_colours[name] == 'orange'
          if name[0] == 'T' ]
print(names)