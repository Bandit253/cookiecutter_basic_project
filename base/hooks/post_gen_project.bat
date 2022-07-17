python -m venv env{{cookiecutter.pyversion}}

"env{{cookiecutter.pyversion}}/Scripts/python.exe" -m pip install --upgrade pip

@REM "env{{cookiecutter.pyversion}}/scripts/pip" install -r ../requirements.txt