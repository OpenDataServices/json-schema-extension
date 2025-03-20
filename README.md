# Open Data Services JSON Schema Extension

An extension to JSON Schema that adds keywords related to codelists and deprecation.

If you are viewing this on GitHub, open the [full documentation](https://json-schema-extension.readthedocs.io) for additional details.

## Maintenance

## Set up your development environment

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

## Update the metaschemas

If you edited a metaschema patch, run the following command to update the metaschemas:

```
python manage.py pre-commit
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