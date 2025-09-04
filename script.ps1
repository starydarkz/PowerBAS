#ATTACK - PB-T1592.001-01 - Enumerate PlugNPlay Camera

echo "#ATTACK - PB-T1592.001-01 - Enumerate PlugNPlay Camera" | Add-Content -Path PowerBAS.log
#STEP 0
$command = Get-CimInstance -Query "SELECT * FROM Win32_PnPEntity WHERE (PNPClass = 'Image' OR PNPClass = 'Camera')"
#Logging
echo Request: Get-CimInstance -Query "SELECT * FROM Win32_PnPEntity WHERE (PNPClass = 'Image' OR PNPClass = 'Camera')" | Add-Content -Path PowerBAS.log
Add-Content -Path PowerBAS.log -Value "Response: '$command'"

