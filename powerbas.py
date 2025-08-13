# PowerBAS v0.1 - StaryDarkz
from colorama import Fore, init


init()

db = {"PB-T1592.001-01":{
    "idMitre":"T1592.001",
    "attackName":"Enumerate PlugNPlay Camera",
    "tags":["powershell", "request_info"],
    "requirements":["None"],
    "commands": ["Get-CimInstance -Query \"SELECT * FROM Win32_PnPEntity WHERE (PNPClass = 'Image' OR PNPClass = 'Camera')\""],
    "cleanup":["None"]
  }
}



# MENUES

menu1 = f"""{Fore.CYAN}PowerBAS

Ingresa el ID unico:
--->{Fore.WHITE}"""


def save_script(script):

    file = open("script.ps1", "w")
    file.write(script)
    file.close
    print (script)
    print ("\n\nSe ha creado un script")


def constructor(select, db=db):


    attackName = db[select]["attackName"]

    script = f"#ATTACK - {select} - {attackName}\n\n"

    count = 0

    # REQUIREMENTS STEPS 
    if "None" not in db[select]["requirements"]:
        
        for r_step in db[select]["requirements"]:
            script = script + f"#STEP - {count}\n"
            script = script + f'Invoke-Expression "{r_step}"\n'

            count += 1
    
    script = script + f'''echo "#ATTACK - {select} - {attackName}" | Add-Content -Path PowerBAS.log\n'''

    # STEPS
    if len(db[select]["commands"]) > 1: # Si tiene mas de un comando

        for step in db[select]["commands"]:

            script = script + f"#STEP - {count}\n"
            script = script + f'$command = {step}\n'

            #Response Logging
            script = script + f'#Logging\n'
            script = script + f'''$request = @'\nRequest: {step}\n'@\n'''
            script = script + f'''Add-Content -Path PowerBAS.log -Value $request\n'''
            script = script + f'''Add-Content -Path PowerBAS.log -Value "Response: '$command'"\n'''
            count += 1
    else: # Si solo tiene un comando
        script = script + f"#STEP {count}\n"
        script = script + f'$command = {db[select]["commands"][0]}\n'
        
        #Repsonse Logging
        script = script + f'#Logging\n'
        script = script + f'''echo Request: {db[select]["commands"][0]} | Add-Content -Path PowerBAS.log\n'''

        script = script + f'''Add-Content -Path PowerBAS.log -Value "Response: '$command'"\n'''
        count += 1   
    
    # Cleanup
    
    if "None" not in db[select]["cleanup"]:

        for c_step in db[select]["cleanup"]:
            script = script + f"#Cleanup\n"
            script = script + f'Invoke-Expression "{c_step}"\n'
    script = script + '\n'  
    save_script(script)


def main(menu1=menu1):

    select = input(menu1) 
    #select = "PB-T1592.001-01" - DEBUG CODE
    constructor(select, db=db)


    pass


#Input
# FALTA - Menu  mas agradable
# FALTA - Mecanismo para seleccionar ataques
# FALTA - Base de datos de ataques unicos 
# FALTA - Conexion con base de datos

#Output
# FALTA - Funcion para obtener el hash del script ps1 final
# FALTA - Falta generador de AttackFlow

main()