# wenxi-ai-tools

A simple Python package by Wenxi with a command-line entry point.

## Install locally

```bash
pip install .
```

## Use as a Python package

```python
from wenxi_ai_tools import hello

hello()
```

## Use as a command

```bash
wenxi-ai-tools
```

## Build

```bash
python -m pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
```

## Upload to PyPI

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxxx
python -m twine upload dist/*
```

On Windows PowerShell:

```powershell
$env:TWINE_USERNAME="__token__"
$env:TWINE_PASSWORD="pypi-xxxx"
python -m twine upload dist/*
```
