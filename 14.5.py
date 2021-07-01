a=input('Kalit soz kiriting').lower()
dic={'integer':'butun son',
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
b=dic.get(a)
if b==None:
    print("bunday soz mavjud emas")
else:
    print(f"{a} {b} deb tarjima qilinadi")