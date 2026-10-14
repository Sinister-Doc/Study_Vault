# Master Unattended PowerShell Runner for CST Research Pipeline
$ErrorActionPreference = "Continue"

$PythonExe = "D:\Softwares\pyenv\Scripts\python.exe"
$RunnerPy = "D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\_cst_scripts\run_pipeline.py"

Write-Host "Executing CST Research Pipeline Unattended in OUTPUT_ROOT (CST\Agy)..." -ForegroundColor Cyan
& $PythonExe $RunnerPy $args

Write-Host "Pipeline Execution Completed. See CST\Agy\_run\actions.log" -ForegroundColor Green
