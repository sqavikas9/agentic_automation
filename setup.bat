call python -m venv venv
call .\venv\Scripts\Activate
timeout /t 1 /nobreak > NUL
pip install --upgrade pip
pip install -r requirements.txt
pip