mahsulotlar = ['anor','uzum','olma','gosht','non','suv','piyoz','sabzi','guruch','un']
royxat =[]
bor_mahsulotar = []
yoq_mahsulotlar = []
print('5 ta mahsulot kiriting:')
for n in range(1,6):
    mahsulot = input(f'{n}-mahsulotni kiriting')
    royxat.append(mahsulot)
for m in royxat:
        if m in mahsulotlar:
            bor_mahsulotar.append(m)

        else:
            yoq_mahsulotlar.append(m)
if yoq_mahsulotlar:
    print("dokonimizda quyidagi mahsulotlar yoq:\n")
    for m in yoq_mahsulotlar:
        print(m)
else: print('dokonimizda barcha mahsulotalr bor')


