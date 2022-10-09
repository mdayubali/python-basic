
my_password = "12345"
stored_pw = "12345"
admin = False

if my_password==stored_pw:
    print('password match')
elif admin:
    print('password didn\'t match but ADMIN granted')
else:
    print('No password match and no admin granted')