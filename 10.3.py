login = input('Loginni kiriting:')
if login.lower() == 'admin' :
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" )
else:
    print(f'Xush kelibsiz, {login}')