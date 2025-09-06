# PowerBAS - @StaryDarkz
from colorama import Fore, init
from os import system


init()
system("clear")

version = "v0.2-beta"


db = {"PB-T1592.001-01":{
    "idMitre":"T1592.001",
    "attackName":"Enumerate PlugNPlay Camera",
    "tags":["powershell", "discovery_info"],
    "requirements":["None"],
    "commands": ["Get-CimInstance -Query \"SELECT * FROM Win32_PnPEntity\""],
    "cleanup":["None"]
  },
  "PB-T1007-01":{
    "idMitre":"T1592.001",
    "attackName":"Enumerate System Services",
    "tags":["processcmd", "discovery_info"],
    "requirements":["None"],
    "commands": ["net start"],
    "cleanup":["None"]
  }
}



# MENUES

menu1 = f"""{Fore.LIGHTGREEN_EX}
    {Fore.WHITE} ⋆         ⋆                  ⋆ {Fore.LIGHTGREEN_EX}
   _______________________________________
 / \                                      \\
|   |                                     | {Fore.WHITE} ⋆{Fore.LIGHTGREEN_EX}
\__ | ___                   ___   _   ___ |
    || _ \_____ __ ____ _ _| _ ) /_\ / __||{Fore.WHITE}⋆{Fore.LIGHTGREEN_EX}
{Fore.WHITE} ⋆{Fore.LIGHTGREEN_EX}  ||  _/ _ \ V  V /-_) '_| _ \/ _ \\\__ \|
    ||_| \___/\_/\_/\__|_| |___/_/ \_\___/|
{Fore.WHITE}   ⋆{Fore.LIGHTGREEN_EX}| _______________{Fore.WHITE}{version}{Fore.LIGHTGREEN_EX}____________|
    |                                     |  {Fore.WHITE}⋆{Fore.LIGHTGREEN_EX}
    |  ▄                                  |
    |   ▀▄                                |
{Fore.WHITE}⋆{Fore.LIGHTGREEN_EX}   |  ▄▀ ▄▄                              |{Fore.WHITE}⋆{Fore.LIGHTGREEN_EX}
    |                                     |
   {Fore.WHITE}⋆{Fore.LIGHTGREEN_EX}|  ___________________________________|{Fore.WHITE} ⋆{Fore.LIGHTGREEN_EX}
    \_/__@starydarkz_____________________/{Fore.WHITE}⋆{Fore.LIGHTGREEN_EX}

{Fore.WHITE}Resources:
{Fore.WHITE}- {Fore.CYAN}Attacks ID: https://github.com/starydarkz...
{Fore.WHITE}- {Fore.CYAN}Source Code: https://github.com/starydarkz/powerbas
"""
menu2 = f"""{Fore.WHITE}Tipo de BAS:\n{Fore.CYAN}1|- Local attack using ps1\n2|- Remote Attack using WinRM
 {Fore.LIGHTWHITE_EX}\n-->🕯 {Fore.LIGHTYELLOW_EX}"""
menu3 = f"""{Fore.WHITE}Ingresa los ID(s) de ataques separados por coma:
 {Fore.LIGHTWHITE_EX}\n->🕯 {Fore.LIGHTYELLOW_EX}"""

def save_script(script):
    ''' Funcion para guardar los scripts '''

    file = open("script.ps1", "w")
    file.write(script)
    file.close
    print (Fore.LIGHTGREEN_EX, script, "\nSe ha creado un script")

def format_devices(devices):
    ''' Formatear entrada de usuario para la lista de equipos en la funcion de Ataque Remoto WinRM'''
    if devices[-1] == ",":
        devices = devices[:-1]
       
    devices =  devices.replace(" ", "")
    devices =  devices.split(",")
    return devices

def format_attacksId(ids):
    ''' Formatear entrada del usuario para la lista de id de ataques '''

    if "," in ids:
        ids =  ids.replace(" ", "")
        ids =  ids.split(",")
        return ids
    else:
        element = [ids]        
        return element

def localps1_constructor(select, db=db):

    script = "#PowerBAS v0.2 \n\n"

    count = 0
    count_it = 0

    if len(select) == 1: # Un solo ataque
        attackName = db[select[0]]["attackName"]
        script = f"#ATTACK - {select[0]} - {attackName}\n"


        # REQUIREMENTS STEPS 
        if "None" not in db[select[0]]["requirements"]:
            
            for r_step in db[select[0]]["requirements"]:
                script = script + f"#STEP - {count}\n"
                script = script + f'Invoke-Expression "{r_step}"\n'

                count += 1
        
        script = script + f'''echo "#ATTACK - {select[0]} - {attackName}" | Add-Content -Path PowerBAS.log\n'''

        # STEPS
        if len(db[select[0]]["commands"]) > 1: # Si tiene mas de un comando

            for step in db[select[0]]["commands"]:

                script = script + f"#STEP - {count}\n"
                script = script + f'$command = '+'{ '+step+' }\n'

                #Response Logging
                script = script + f'\n#Logging\n'
                script = script + f'''$request = @'\nRequest: {step}\n'@\n'''
                script = script + f'''Add-Content -Path PowerBAS.log -Value $request\n'''
                script = script + f'''echo Response:| Add-Content -Path PowerBAS.log\n'''
                script = script + f'$command | Add-Content -Path PowerBAS.log\n'            
                count += 1
        else: # Si solo tiene un comando
            script = script + f"#STEP {count}\n"
            script = script + f'$command = {db[select[0]]["commands"][0]}\n'
            
            #Repsonse Logging
            script = script + f'\n#Logging\n'
            script = script + f'''echo Request: {db[select[0]]["commands"][0]} | Add-Content -Path PowerBAS.log\n'''

            script = script + f'''echo Response:| Add-Content -Path PowerBAS.log\n'''
            script = script + f'$command | Add-Content -Path PowerBAS.log\n'            
            count += 1   
        
        # Cleanup
        
        if "None" not in db[select[0]]["cleanup"]:

            for c_step in db[select[0]]["cleanup"]:
                script = script + f"#Cleanup\n"
                script = script + f'Invoke-Expression "{c_step}"\n'
    else: # Mas de un ataque

        for ID in select:

            attackName = db[ID]["attackName"]

            script = script+ f"\n#ATTACK - {ID} - {attackName}\n\n"
            


            # REQUIREMENTS STEPS 
            if "None" not in db[ID]["requirements"]:
                
                for r_step in db[ID]["requirements"]:
                    script = script + f"#STEP - {count}\n"
                    script = script + f'$command = '+'{ '+step+' }\n'
                    count += 1
            
            script = script + f'''echo "#ATTACK - {ID} - {attackName} | Add-Content -Path PowerBAS.log\n'''

            # STEPS
            if len(db[ID]["commands"]) > 1: # Si tiene mas de un comando

                for step in db[ID]["commands"]:

                    script = script + f"#STEP - {count}\n"
                    script = script + f'$command = '+'{ '+step+' }\n'
                    script = script + "$result = Invoke-Command -ComputerName $device -ScriptBlock $command"

                    #Response Logging
                    script = script + f'\n#Logging\n'
                    script = script + f'''#request = @'\nRequest: {step}\n'@\n'''
                    script = script + f'''Add-Content -Path PowerBAS_$device.log -Value $request\n'''
                    script = script + f'''echo Response:| Add-Content -Path PowerBAS.log\n'''
                    script = script + f'$command | Add-Content -Path PowerBAS.log\n'                 
                    count += 1
            else: # Si solo tiene un comando
                script = script + f"#STEP - {count}\n"
                script = script + f'$command = '+'{ '+db[ID]["commands"][0]+' }\n'

                #Repsonse Logging
                script = script + f'\n#Logging\n'
                script = script + f'''echo "Request: {db[ID]["commands"][0]}" | Add-Content -Path PowerBAS_$device.log\n'''
                script = script + f'''echo Response:| Add-Content -Path PowerBAS.log\n'''
                script = script + f'$command | Add-Content -Path PowerBAS.log\n'
                count += 1   
            
            # Cleanup
            
            if "None" not in db[ID]["cleanup"]:

                for c_step in db[ID]["cleanup"]:
                    script = script + f"#Cleanup\n"
                    script = script + f'Invoke-Expression "{c_step}"\n'  
    save_script(script)
def remotewinrm_constructor(select, devices, db=db):
    
    script = "#PowerBAS v0.2 \n\n"
    count = 0
    count_it = 0

    device_text = ""
    for device in devices:
        if count_it == 0:
            device_text = device_text+f'"{device}"'
        else:
            device_text = device_text+", " +f'"{device}"'

        count_it += 1
    script = script + f"$devices = @({device_text})\n"
    script = script + "foreach ($device in $devices) {\n"


    if len(select) == 1: # Un solo ataque
        tab = "    "
        attackName = db[select[0]]["attackName"]

        script = script+ f"\n{tab}#ATTACK - {select[0]} - {attackName}\n"
        
    
        # REQUIREMENTS STEPS 
        if "None" not in db[select[0]]["requirements"]:
            
            for r_step in db[select[0]]["requirements"]:
                script = script + f"{tab}#STEP - {count}\n"
                script = script + f'{tab}Invoke-Command -ComputerName $device {"{r_step}"}'

                count += 1
        
        script = script + f'''{tab}echo "#ATTACK - {select[0]} - {attackName} - Device: $device" | Add-Content -Path PowerBAS_$device.log\n'''

        # STEPS
        if len(db[select[0]]["commands"]) > 1: # Si tiene mas de un comando

            for step in db[select[0]]["commands"]:

                script = script + f"{tab}#STEP - {count}\n"
                script = script + f'{tab}$command = '+'{ '+step+' }\n'
                script = script + "{tab}$result = Invoke-Command -ComputerName $device -ScriptBlock $command"

                #Response Logging
                script = script + f'\n{tab}#Logging\n'
                script = script + f'''{tab}#request = @'\nRequest: {step}\n'@\n'''
                script = script + f'''{tab}Add-Content -Path PowerBAS_$device.log -Value $request\n'''
                script = script + f'''{tab}echo Response:| Add-Content -Path PowerBAS_$device.log\n'''
                script = script + f'{tab}$result | Add-Content -Path PowerBAS_$device.log\n'
                count += 1
        else: # Si solo tiene un comando
            script = script + f"{tab}#STEP {count}\n"
            script = script + f'{tab}$command = '+'{ '+db[select[0]]["commands"][0]+' }\n'
            script = script + f"{tab}$result = Invoke-Command -ComputerName $device -ScriptBlock $command"
            
            #Repsonse Logging
            script = script + f'\n{tab}#Logging\n'
            script = script + f'''{tab}echo "Request: {db[select[0]]["commands"][0]}" | Add-Content -Path PowerBAS_$device.log\n'''
            script = script + f'''{tab}echo Response:| Add-Content -Path PowerBAS_$device.log\n'''
            script = script + f'{tab}$result | Add-Content -Path PowerBAS_$device.log\n'
            count += 1   
        
        # Cleanup
        
        if "None" not in db[select[0]]["cleanup"]:

            for c_step in db[select[0]]["cleanup"]:
                script = script + f"{tab}#Cleanup\n"
                script = script + f'{tab}Invoke-Expression "{c_step}"\n'
    else: # Mas de un ataque

        for ID in select:

            tab = "    "
            attackName = db[ID]["attackName"]

            script = script+ f"\n{tab}#ATTACK - {ID} - {attackName}\n\n"
            


            # REQUIREMENTS STEPS 
            if "None" not in db[ID]["requirements"]:
                
                for r_step in db[ID]["requirements"]:
                    script = script + f"#STEP - {count}\n"
                    script = script + f'{tab}Invoke-Command -ComputerName $device {"{r_step}"}'

                    count += 1
            
            script = script + f'''{tab}echo "#ATTACK - {ID} - {attackName} - Device: $device" | Add-Content -Path PowerBAS_$device.log\n'''

            # STEPS
            if len(db[ID]["commands"]) > 1: # Si tiene mas de un comando

                for step in db[ID]["commands"]:

                    script = script + f"{tab}#STEP - {count}\n"
                    script = script + f'{tab}$command = '+'{ '+step+' }\n'
                    script = script + "$result = Invoke-Command -ComputerName $device -ScriptBlock $command"

                    #Response Logging
                    script = script + f'\n{tab}#Logging\n'
                    script = script + f'''{tab}#request = @'\nRequest: {step}\n'@\n'''
                    script = script + f'''{tab}Add-Content -Path PowerBAS_$device.log -Value $request\n'''
                    script = script + f'''{tab}echo Response:| Add-Content -Path PowerBAS_$device.log\n'''
                    script = script + f'{tab}$result | Add-Content -Path PowerBAS_$device.log\n'                    
                    count += 1
            else: # Si solo tiene un comando
                script = script + f"{tab}#STEP {count}\n"
                script = script + f'{tab}$command = '+'{ '+db[ID]["commands"][0]+' }\n'
                script = script + f"{tab}$result = Invoke-Command -ComputerName $device -ScriptBlock $command"
                
                #Repsonse Logging
                script = script + f'\n{tab}#Logging\n'
                script = script + f'''{tab}echo "Request: {db[ID]["commands"][0]}" | Add-Content -Path PowerBAS_$device.log\n'''
                script = script + f'''{tab}echo Response:| Add-Content -Path PowerBAS_$device.log\n'''
                script = script + f'{tab}$result | Add-Content -Path PowerBAS_$device.log\n'
                count += 1   
            
            # Cleanup
            
            if "None" not in db[ID]["cleanup"]:

                for c_step in db[ID]["cleanup"]:
                    script = script + f"{tab}#Cleanup\n"
                    script = script + f'{tab}Invoke-Expression "{c_step}"\n'
    script = script + '}\n'  
    save_script(script)


def main(menu1=menu1, menu2=menu2, menu3=menu3):

    print (menu1) 
    sel2 = input(menu2) #Tipo de BAS
    sel3 = input(menu3) #Lista de ID de ataques

  
    if sel2 == "1": #Local Attack using ps1
        id_formated = format_attacksId(sel3)
        localps1_constructor(id_formated, db=db)

    elif sel2 == "2": #Remote attack using WinRM
        
        devices = input(f"{Fore.WHITE}Agrega los hostnames de los equipos separados por coma:\n{Fore.LIGHTWHITE_EX}\n->🕯 {Fore.LIGHTYELLOW_EX}")
        devices_formated = format_devices(devices)
        id_formated = format_attacksId(sel3)
        remotewinrm_constructor (id_formated, devices_formated, db=db)

main()
