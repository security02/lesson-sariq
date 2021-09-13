taomlar = ['osh','somsa','shashlik','gumma','manti']
nonushta = taomlar[:]
print(taomlar)
print(nonushta)
del nonushta[2]
del nonushta[3]
nonushta.remove('osh')
nonushta.append('tuxum')
nonushta.append('blinchik')
print(nonushta)
print(taomlar)
nonushta = tuple(nonushta)
print(nonushta)
taomlar[0] = "qaymoq va non"
print(taomlar)