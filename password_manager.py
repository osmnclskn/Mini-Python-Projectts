from cryptography.fernet import Fernet

'''
def write_key():
    key=Fernet.generate_key()
    with open ("key.key",'wb') as key_file:
        key_file.write(key)'''


def load_key():
    file=open('key.key','rb')
    key=file.read()
    file.close()
    return key



master_pwd=input("What is the master password? ")
key=load_key() + master_pwd.encode()
fer=Fernet(key)

def view():
    with open("passwords.txt",'r')as f:
        for line in f.readlines():
            data=(line.rstrip())
            user,passw=data.split('|')
            print("User: ",user,",Password: ",
                   fer.decrypt(passw.encode()).decode())

def add():
    name=input('Account Name: ')
    pwd=input("Password :  ")
    with open ('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def delete(account_name):
    lines=[]
    with open ("passwords.txt",'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,_=data.split("|")
            if user.lower() !=account_name.lower():
                lines.append(line)
    with open('passwords.txt','w') as f:
        f.writelines(lines)


def update(account_name):
    lines=[]
    with open('passwords.txt','r') as f:
        lines=[line.rstrip() for line in f]

    for i, line in enumerate(lines):
        user,_=line.split('|')
        if user.lower()==account_name.lower():
            new_pwd=input(f'Enter the new password for {account_name} : ')
            lines[i]=f"{user}|{fer.encrypt(new_pwd.encode()).decode()}"
    
    with open('passwords.txt','w') as f:
        f.write('\n'.join(lines) + '\n')

while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add) if you want to quit press (q). Also you can delete your account and update your password. (delete/update): ").lower()
    if mode=="q":
        break


    elif mode=="view":
        view()
    elif mode=="add":
        add()
    elif mode=='delete':
        account_to_delete=input('Enter the account name you want to delete : ')
        delete(account_to_delete)
        print(f'{account_to_delete} has been deleted')
    elif mode=='update':
        account_to_update=input('Enter the account name you want to update :  ')
        update(account_to_update)
        print(f'{account_to_update} has been updated.')
    else:
        print("Invalid mode.")
        continue