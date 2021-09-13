soz=input('qaysi python atamisini bilishni istaysiz?').lower()
dic={'integr':'butun son',
     'float':'haqiqiy son',
     'string':'matn',
     'flask':'python frameworki',
     'title()':'sozlar b harf',
     'upper()':'sozni k h bn y',
     'git':'kod j sayt',
     'list':'royxat',
     'massiv':'o q s belgi',
     'tuple':'ozgarmas royxat'
     }
k=dic.get(soz)
if k==None:
    print("bunday soz mavjud emas")
else:
    print(f"{k} {soz} deb tarjima qilinadi")


