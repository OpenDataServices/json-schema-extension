# Open Data Services JSON Schema Extension

An extension to JSON Schema that adds keywords related to codelists and deprecation.

If you are viewing this on GitHub, open the full documentation for additional details.

## Building the documentation

## Get started

```{note}
Building the documentation requires Python 3.9 or greater.
```
  
Create a virtual environment:

```
sudo apt-get install python3-venv
python3 -m venv .venv
source .ve/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

## Build the documentation

Sphinx, which builds the documentation, doesn’t watch directories for changes. To regenerate the documentation and refresh the browser whenever changes are made, run:

```
sphinx-autobuild docs docs/_build/dirhtml
```

Otherwise, build the docs into `docs/_build/dirhtml`:

```
cd docs
make dirhtml
```

View the documentation by running a local web server:

```
cd _build/dirhtml
python -m http.server
```

Go to http://localhost:8000/ in a browser.