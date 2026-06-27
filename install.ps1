# Requires -RunAsAdministrator

# === CONFIGURATION ===
$TargetDir = "C:\jpp"
$RepoZipUrl = "https://github.com"
$ZipFile = "$TargetDir\project.zip"
# =====================

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "   Setting up JPP Environment for Windows" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# 1. Create target directory
if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    Write-Host "[+] Created target directory: $TargetDir" -ForegroundColor Green
} else {
    Write-Host "[*] Target directory $TargetDir already exists." -ForegroundColor Yellow
}

# 2. Download project sources using Windows native web client
Write-Host "[*] Downloading project sources..." -ForegroundColor Cyan
try {
    Invoke-WebRequest -Uri $RepoZipUrl -OutFile $ZipFile -TimeoutSec 60
    Write-Host "[+] Download complete!" -ForegroundColor Green
} catch {
    Write-Error "[-] Failed to download project sources. Check your URL or internet connection."
    Exit
}

# 3. Extract sources into C:\jpp
Write-Host "[*] Extracting files..." -ForegroundColor Cyan
try {
    # Extract to a temporary folder to avoid nested root directory issues from GitHub ZIPs
    $TempExtract = "$TargetDir\temp_extract"
    Expand-Archive -Path $ZipFile -DestinationPath $TempExtract -Force

    # Move everything from the inner folder directly to C:\jpp
    $InnerFolder = Get-ChildItem -Path $TempExtract | Select-Object -First 1
    Get-ChildItem -Path $InnerFolder.FullName | Move-Item -Destination $TargetDir -Force

    # Cleanup temp files
    Remove-Item -Path $TempExtract -Recurse -Force
    Remove-Item -Path $ZipFile -Force
    Write-Host "[+] Project sources successfully deployed to $TargetDir" -ForegroundColor Green
} catch {
    Write-Error "[-] Extraction failed."
    Exit
}

# 4. Check for Python and Install Nuitka compiler
Write-Host "`n[*] Setting up compiler environment..." -ForegroundColor Cyan
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "[*] Installing/Updating Nuitka and dependencies..." -ForegroundColor Cyan
    python -m pip install --upgrade pip | Out-Null
    python -m pip install nuitka | Out-Null

    # If you have a requirements.txt in your project, uncomment the line below:
    # if (Test-Path "$TargetDir\requirements.txt") { python -m pip install -r "$TargetDir\requirements.txt" | Out-Null }

    Write-Host "[+] Nuitka installed successfully!" -ForegroundColor Green
} else {
    Write-Host "[-] WARNING: Python not found in PATH!" -ForegroundColor Red
    Write-Host "[-] Please install Python manualy to compile the project." -ForegroundColor Yellow
}

# 5. Update User PATH
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($UserPath -notlike "*$TargetDir*") {
    $NewPath = $UserPath + ";" + $TargetDir
    $NewPath = $NewPath -replace ";+", ";"
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    Write-Host "[+] Successfully added $TargetDir to User PATH!" -ForegroundColor Green
} else {
    Write-Host "[*] $TargetDir is already in PATH." -ForegroundColor Cyan
}

# 6. Compilation Instructions
Write-Host "`n=========================================" -ForegroundColor Magenta
Write-Host "           INSTALLATION COMPLETE         " -ForegroundColor Magenta
Write-Host "=========================================" -ForegroundColor Magenta
Write-Host "To compile your interpreter into 'jppi.exe', run these commands:" -ForegroundColor White
Write-Host "1. cd $TargetDir" -ForegroundColor Yellow
Write-Host "2. python -m nuitka --onefile main.py -o jppi.exe" -ForegroundColor Yellow
Write-Host "   (Replace 'main.py' with your main entry point script)" -ForegroundColor Gray
Write-Host "`n[*] IMPORTANT: Please RESTART your terminal/VS Code for PATH changes to take effect." -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Magenta
