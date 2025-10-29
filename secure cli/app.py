import os,hashlib,pwinput,logging


logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def Hashpassword(password) :
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def register() :
    os.makedirs("Users",exist_ok=True)
    path = "data/users.txt"


    username=input("Enter su nombre de usuario: ")
    password=pwinput.pwinput("Enter la contrasena: ", mask='*')

    if username == "Select"  or username == "select" or username == "From"  or username == "from" :
        print("User Invalido")
        return

    hashed_password=Hashpassword(password)

    with open(path,'a') as file:
        file.write(f"{username},{hashed_password}\n")
    logging.info(f"Nuevo usuario registrado: {username}")
    print("Registracion exitosa!")













