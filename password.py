from cryptography.fernet import Fernet #allows to encrypt & decrypt text
import os
## a function just to create .key file
'''def write_key_key():
    key=Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)

write_key_key()'''

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

key=load_key()
fer=Fernet(key)#initializing the decryption module

def add():
    name=input("Enter the UserName:")
    passw=input("Enter the password:")

    with open("passwords.txt","a")as f:
        f.write(name+"|"+fer.encrypt(passw.encode()).decode()+"\n")

def view():
        if os.path.getsize("passwords.txt")==0:
            print("File Is empty!!\n")
            print("Try adding a password and then try viewing!!\n")
            pass
        else:
            with open("passwords.txt","r") as f:
                for lines in f.readlines():
                    data=lines.rstrip()
                    un,p=data.split("|")
                    print("UserName: ",un," Password: ",fer.decrypt(p.encode()).decode())


while(True):
    mode=input("Would you like to add a new password or just view the existing ones(add/view) or press 'q' to quit:").lower()
    if(mode=='q'):
        break
    if(mode=='add'):
        add()
    elif(mode=='view'):
        view()
    else:
        print("Invalid:")
        continue
