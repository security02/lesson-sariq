mahsulotlar = ['anor','uzum','olma','gosht','non','suv','piyoz','sabzi','guruch','un']
savat = []
print('Kamida 5 ta mahsulot kiriting:')
for a in range(1,6):
    savat.append(input(f'{a}-mahsulotni kiriting:'))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f'{mahsulot} dokonimizda bor')
    else: print(f'{mahsulot} dokonimizda yoq')