import json
import json_merge_patch
from pathlib import Path

import click

basedir = Path(__file__).resolve().parent
schemadir = basedir / "schema"


def json_dump(filename, data):
    """Write JSON data to the given filename."""
    with (schemadir / filename).open("w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def json_load(filename):
    """Load JSON data from the given filename."""
    with (schemadir / filename).open() as f:
        return json.load(f)


def get_metaschema(version):
    """Patches and returns the metaschema."""
    
    if version in ["draft-04", "2020-12"]:
        return json_merge_patch.merge(
        json_load(f"{version}/json-schema-{version}.json"), json_load(f"{version}/patch/metaschema-patch.json")
    )
    else:
        raise ValueError(f"Unsupported JSON Schema version: {version}")


@click.group()
def cli():
    pass


@cli.command()
def pre_commit():
    """
    Update metaschema files.
    """

    for version in ["draft-04", "2020-12"]:
        json_dump(f"{version}/metaschema.json", get_metaschema(version))


if __name__ == "__main__":
    cli()