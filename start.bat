@echo off
REM Lancer une nouvelle fenêtre cmd avec le venv activé et les commandes suivantes
start cmd /k "pip install -r requirements.txt && .\.venv\Scripts\activate && cd monitoring && docker-compose up -d && cd.."
