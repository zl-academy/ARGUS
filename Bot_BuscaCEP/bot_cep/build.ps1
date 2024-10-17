$exclude = @("venv", "bot_cep.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cep.zip" -Force