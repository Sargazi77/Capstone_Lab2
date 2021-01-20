Classes_registered = {'ITEC 2200', 'ITEC 2600', ' ENGL 1000', 'BIOL 22260', 'BIOL 1165'}

only_itec = [c for c in Classes_registered if c.startswith('ITEC')]
print(only_itec)
only_biol = [c for c in Classes_registered if c.startswith('biol')]
print(only_biol)