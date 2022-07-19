Write-Host 'start clear migrations files'
$var = Get-Location
Set-Location .\mos_web_server\accio\migrations
Get-Location
Remove-Item -Path .\000?_*.py
Set-Location $var
Set-Location .\mos_web_server\erecto\migrations
Get-Location
Remove-Item -Path .\000?_*.py
Set-Location $var
Set-Location .\mos_web_server\flagrate\migrations
Get-Location
Remove-Item -Path .\000?_*.py
Set-Location $var
Set-Location .\mos_web_server\reparo\migrations
Get-Location
Remove-Item -Path .\000?_*.py
Set-Location $var
Set-Location .\mos_web_server\users\migrations
Get-Location
Remove-Item -Path .\000?_*.py
Set-Location $var
Write-Host 'migrations files cleared'
