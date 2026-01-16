@echo off
REM Activa el entorno virtual ubicado en la carpeta env

if not exist "env\Scripts\activate.bat" (
    echo El entorno virtual no existe en la carpeta "env".
    pause
    exit /b 1
)

call env\Scripts\activate.bat

echo Entorno virtual activado.
cmd /k