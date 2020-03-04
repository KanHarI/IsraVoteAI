py -3.7 -m venv venv
call venv\Scripts\activate.bat
python -m pip install -U pip setuptools
pip install torch===1.4.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install .
