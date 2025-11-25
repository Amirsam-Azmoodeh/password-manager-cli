import crypto_utils # ماژولی که در آن مراحل رمنگاری و رمزگشایی انجام میشود
import db_manager #دیتابیسی که در آن اطلاعات ذخیره میشوند


while True :

    command = input('>>> ')
    
    if command == 'add' :
        try :

            service = input("Service : ")
            username = input("Username : ")
            password = input("Password : ")

            db_manager.add(service , username , crypto_utils.encrypt_password(password))

            print('was registered')

        except Exception as error:
            print(f'Try again -> {error}')


    elif command == 'get' :
        try : 

            service = input("Service : ")
            username = input("Username : ")

            data_base = db_manager.get(service , username)
            print(f'ID : {data_base[0][0]}\nPassword : {crypto_utils.decrypt_password(data_base[0][3])}\n')

        except Exception as error:
            print(f'Try again -> {error}')                


    elif command == 'delete' :
        try : 

            username = input("Username : ")
            data_base = db_manager.delete(username)
            print('was deleted')

        except Exception as error:
            print(f'Try again -> {error}')
    

    
    elif command == 'list' :
        try :

            data_base = db_manager.list()
            for i in data_base :
                print(f'ID : {data_base[i][0]}\nService : {data_base[i][1]}\nUsername : {data_base[i][2]}\nPassword : {crypto_utils.decrypt_password(data_base[i][3])}\n')


        except Exception as error:
            print(f'Try again -> {error}')
    
    elif command == 'help' :
        print("""
              Commands:
    add     → Add new password
    get     → Retrieve password
    list    → Show all passwords
    delete  → Delete by username
    exit    → Quit 
              """)

    elif command == 'exit' :
        print('Hope to see you!')
        break