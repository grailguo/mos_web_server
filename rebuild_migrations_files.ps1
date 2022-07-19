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
python manage.py makemigrations
python manage.py migrate
[string]$load_data = 'N'
Write-Host 'Do you want to load data?'
Write-Host -NoNewline '[Y] Yes  '
write-host -NoNewline '[N] No ' -ForegroundColor yellow
$load_data = Read-Host '(default is "N")'
if (($load_data[0] -eq 'Y') -OR ($load_data[0] -eq 'y')) {
python manage.py loaddata --app users data
python manage.py loaddata --app erecto data
python manage.py loaddata --app reparo data
python manage.py loaddata --app accio 101_cartridge.json
python manage.py loaddata --app accio 102_compound.json
python manage.py loaddata --app accio 103_compoundcodecounter.json
python manage.py loaddata --app accio 104_cartridge_compound.json
python manage.py loaddata --app accio 105_compoundtag.json
python manage.py loaddata --app accio 106_compound_compoundtag.json
python manage.py loaddata --app accio 107_experiment.json
python manage.py loaddata --app accio 108_spectrumtag.json
python manage.py loaddata --app accio 109_spectrum.json
python manage.py loaddata --app accio 110_spectrum_spectrumtag.json
python manage.py loaddata --app accio 111_quantmethod.json
python manage.py loaddata --app accio 112_quantmethodcodecounter.json
python manage.py loaddata --app accio 113_cartridge_quantmethod.json
python manage.py loaddata --app flagrate data
}
