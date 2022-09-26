export PYTHONPATH=$PYTHONPATH:/Users/david.escandell/development/source-code/monopoly/src

pipenv run pytest -v tests/
python3 src/main.py
pipenv run python3 src/main.py
