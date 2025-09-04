# PowerBAS v0.1 - StaryDarkz
from colorama import Fore, init
from os import system

init()
system("cls")

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

menu1 = f"""{Fore.CYAN}
    {Fore.WHITE} ⋆         ⋆                  ⋆ {Fore.CYAN}
   _______________________________________
 / \                                      \\
|   |                                     | {Fore.WHITE} ⋆{Fore.CYAN}
\__ | ___                   ___   _   ___ |
    || _ \_____ __ ____ _ _| _ ) /_\ / __||{Fore.WHITE}⋆{Fore.CYAN}
{Fore.WHITE} ⋆{Fore.CYAN}  ||  _/ _ \ V  V /-_) '_| _ \/ _ \\\__ \|
    ||_| \___/\_/\_/\__|_| |___/_/ \_\___/|
{Fore.WHITE}   ⋆{Fore.CYAN}| ____________________{Fore.WHITE}v0.1{Fore.CYAN}____________|
    |                                     |  {Fore.WHITE}⋆{Fore.CYAN}
    |  ▄                                  |
    |   ▀▄                                |
{Fore.WHITE}⋆{Fore.CYAN}   |  ▄▀ ▄▄                              |{Fore.WHITE}⋆{Fore.CYAN}
    |                                     |
   {Fore.WHITE}⋆{Fore.CYAN}|  ___________________________________|{Fore.WHITE} ⋆{Fore.CYAN}
    \_/__@starydarkz_____________________/{Fore.WHITE}⋆{Fore.CYAN}

{Fore.WHITE}Resources:
{Fore.WHITE}- {Fore.CYAN}Attacks ID: https://127.0.0.1./xxx/xxx
{Fore.WHITE}- {Fore.CYAN}Source Code: https://github.com/starydarkz/powerbas

{Fore.WHITE}Ingresa los ID(s) de ataques separados por coma:
 -->🕯 {Fore.LIGHTCYAN_EX}"""

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
# FALTA - Mecanismo para seleccionar ataques
# FALTA - Base de datos de ataques unicos 
# FALTA - Conexion con base de datos

#Output
# FALTA - Funcion para obtener el hash del script ps1 final
# FALTA - Falta generador de AttackFlow

main()