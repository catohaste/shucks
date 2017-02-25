cd ENV
. bin/activate
cd shucks
pip install --editable .
export FLASK_APP=shucks.py
export FLASK_DEBUG=true
cd shucks
flask run