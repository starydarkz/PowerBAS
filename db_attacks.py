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
