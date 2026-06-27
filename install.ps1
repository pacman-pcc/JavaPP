# Requires -RunAsAdministrator

$BinaryName = "jppi.exe"
$TargetDir = "C:\jppi"

# 1. Провека наявності бінарника в поточній папці
if (-not (Test-Path .\$BinaryName)) {
    Write-Error "Error: '$BinaryName' not found in the current directory!"
    Exit
}

# 2. Створення цільової папки, якщо її немає
if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    Write-Host "Created target directory: $TargetDir" -ForegroundColor Purple
}

# 3. Копіювання бінарника
Copy-Item -Path .\$BinaryName -Destination $TargetDir -Force
Write-Host "Successfully copied $BinaryName to $TargetDir" -ForegroundColor Purple

# 4. Отримання поточного Path користувача
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")

# 5. Перевірка та додавання до Path
if ($UserPath -notlike "*$TargetDir*") {
    $NewPath = $UserPath + ";" + $TargetDir
    # Очищаємо від випадкових подвійних крапок з комою
    $NewPath = $NewPath -replace ";+", ";"
    
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    Write-Host "Successfully added $TargetDir to User PATH!" -ForegroundColor Green
    Write-Host "Please RESTART your terminal/VS Code for changes to take effect." -ForegroundColor Yellow
} else {
    Write-Host "$TargetDir is already in PATH." -ForegroundColor Cyan
}
