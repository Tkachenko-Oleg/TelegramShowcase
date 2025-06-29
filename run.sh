source ./.venv/bin/activate
set -a
source .env
set +a

PYTHONPATH=$(pwd)
export PYTHONPATH="$PYTHONPATH"

clear

python3 app/run.py
