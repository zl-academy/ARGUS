$exclude = @("venv", "bot_argus.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_argus.zip" -Force