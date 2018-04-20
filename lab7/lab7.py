def main():
    global listOfUser
    listOfUser={'log0':['pass0','admin'],'log1':['pass1','admin'],'log2':['pass2', 'user'],'log3':['pass3','user']}
    print("База пользователей")
    while(True):
        print("\nВыберите действие:")
        print("1 Войти в учетную запись")
        print("2 Зарегистрировать нового пользователя")
        print("3 Выход")
        flag=input()
        if (flag=='1'): 
            enterAccount()
        elif (flag=='2'): 
            makeNewUser()        
        elif (flag=='3'): 
            sys.exit()
        else: print("Неверный код действия")
#####
def enterAccount():
     print("Введите логин")
     login=input()
     user=checkLogin(login)
     if (user==None):
         print("Пользователя с таким логином в базе нет")
     else:
         print("Введите пароль")
         password=input()
         if (password!=listOfUser[user][0]):
             print("Неверный пароль")
         else:
             print ("Вы успешно вошли в учетную запись", user)
             selectAccountType(user) 
#####
def selectAccountType(user):
    if (listOfUser[user][1]=='user'):
        accountActivityUser(user)
    else:
        accountActivityAdmin(user)
#####
def accountActivityUser(user):
    while(True):
        print("\nВыберите действие:")
        print("1 Изменить логин учетной записи")
        print("2 Изменить пароль учетной записи")
        print("3 Удалить учетную запись")
        print("4 Выйти из учетной записи")
        print("5 Выход")
        flag=input()
        if (flag=='1'): 
            user=changeLogin(user)
        elif (flag=='2'): 
            user=changePassword(user)
        elif (flag=='3'):
            deleteAccount(user)
            break
        elif (flag=='4'):
            break
        elif (flag=='5'): 
            sys.exit()
        else: print("Неверный код действия")
#####
def accountActivityAdmin(user):
    print("Вы зашли как администратор")
    while(True):
        print("\nВыберите действие:")
        print("1 Создать новую учетную запись")
        print("2 Изменить логин своей учетной записи")
        print("3 Изменить пароль своей учетной записи")
        print("4 Изменить пароль учетной записи обычного пользователя")
        print("5 Вывести список пользователей")
        print("6 Назначить администратора")
        print("7 Удалить свою учетную запись")
        print("8 Выйти из учетной записи")
        print("9 Выход")
        flag=input()
        if (flag=='1'): 
            makeNewUser()
        elif (flag=='2'): 
            user=changeLogin(user)
        elif (flag=='3'): 
            user=changePassword(user)
        elif (flag=='4'): 
            changeUserPassword()
        elif (flag=='5'): 
            printListOfUser()
        elif (flag=='6'): 
            makeAdmin()
        elif (flag=='7'):
            deleteAccount(user)
            break
        elif (flag=='8'):
            break
        elif (flag=='9'): 
            sys.exit()
        else: print("Неверный код действия")
#####
def changeLogin(user):
    while(True):
        print("Введите новый логин")
        login=input()
        if (checkLogin(login)==None):
            listOfUser[login]=listOfUser.pop(user)
            print("Логин учетной записи ",login," был успешно изменен", listOfUser[login])
            return login
        else: print("Этот логин уже занят, пожалуйста, введите другой")
#####
def changePassword(user):
    print("Введите старый пароль")
    password=input()
    if (password==listOfUser[user][0]):
        print("Введите новый пароль")
        password=input()
        listOfUser[user][0]=password
        print("Пароль учетной записи ",user," был успешно изменен", listOfUser[user])
    else:
        print("Введен неверный пароль")
    return user
#####
def changeUserPassword():
    print("Введите логин учетной записи")
    login=input()
    if (checkLogin(login)==None):
        print("Такой учетной записи не существует")
    else:
        if (listOfUser[login][1]=='admin'):
            print("Вы не можете сбросить пароль у администратора")
        else:
            print("Введите новый пароль")
            password=input()
            listOfUser[login][0]=password
            print("Пароль учетной записи ",login," был успешно изменен", listOfUser[login])
#####
def printListOfUser():
    print("Список пользователей")
    for key in sorted(listOfUser):
        print(key, "=>", listOfUser[key][1])
#####
def makeAdmin():
    print("Введите логин учетной записи")
    login=input()
    if (checkLogin(login)==None):
        print("Такой учетной записи не существует")
    else:
        listOfUser[login][1]='admin'
        print("Пользователь ",login," успешно стал администратором")
#####
def deleteAccount(user):
    del listOfUser[user]
    print("Учетная запись пользователя ",user," успешно удалена")
#####
def makeNewUser():
    while(True):
        print("Введите логин")
        login=input()
        if (checkLogin(login)==None):
            print("Введите пароль")
            password=input()
            listOfUser[login]=[password,'user']
            print ("Пользователь ",login," успешно создан", listOfUser[login])
            break
        else: print("Этот логин уже занят, пожалуйста, введите другой")
#####
def checkLogin(login):
    if (login in listOfUser):
        return login
    return None
#####
import sys
main()
