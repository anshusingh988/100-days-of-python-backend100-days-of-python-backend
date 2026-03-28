# Start-Tracker.ps1
# Script to run both backend and frontend for the Expense Tracker

# Function to run command in a new window
function Run-In-New-Terminal($path, $command, $title) {
    Start-Process powershell -ArgumentList "-NoExit -Command cd `$path; $command" -WindowStyle Normal
}

Write-Host "--- Starting Expense Tracker Project ---" -ForegroundColor Cyan

# Start Backend
Write-Host "-> Launching Backend (Flask) on port 5000..." -ForegroundColor Green
Run-In-New-Terminal ".\backend" "python app.py" "Backend API"

# Start Frontend
Write-Host "-> Launching Frontend (Vite) on port 5173..." -ForegroundColor Green
Run-In-New-Terminal ".\frontend" "npm run dev" "Frontend UI"

Write-Host "`nProject is booting up! Check both terminal windows for status." -ForegroundColor Yellow
Write-Host "Backend API: http://127.0.0.1:5000"
Write-Host "Frontend UI: http://localhost:5173"
