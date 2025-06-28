source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=$(pwd)
export PYTHONPATH="$PYTHONPATH"
set -a
source .env
set +a
clear
python3 app/run.py
