@echo off
setlocal

REM Executa a calculadora CLI
python --version >nul 2>&1
if %errorlevel% neq 0 (
  echo Python nao encontrado no PATH. Instale o Python 3.10+ e tente novamente.
  exit /b 1
)

python calculadora.py

endlocal
