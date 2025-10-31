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

def register():
    os.makedirs("Data",exist_ok=True)
    path = "data/users.txt"

    Invalid = ["select","from","Drop","insert","delete","update","user",";","--","'","\""]


    username=input("Enter su nombre de usuario: ")
    
    username_lower = username.lower()

    for palabras in Invalid:
        if palabras.lower() in username_lower:
            print("Nombre de usuario invalido. Intente de nuevo.")
            return
        
    password=pwinput.pwinput("Enter la contrasena: ", mask='*')

  
    hashed_password=Hashpassword(password)

    with open(path,'a') as file:
        file.write(f"{username},{hashed_password}\n")
    logging.info(f"Nuevo usuario registrado: {username}")
    print("Registracion exitosa!")



def main():

    os.makedirs("data",exist_ok=True)
    while True:
        print("1. Register")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == '1':
            register()
        elif opcion == 'q':
            print("Saliendo...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
        



main()



