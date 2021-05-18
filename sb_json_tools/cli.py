import sys
import json

import typer

import json_streams
from json_streams import jsonlib
from sb_json_tools import jt_val


__version__ = "0.9.0"


cli = typer.Typer()


@cli.command()
def validate(
    infile: typer.FileBinaryRead,
    outfile: typer.FileBinaryWrite,
    schema: typer.FileBinaryRead = typer.Option(
        ..., "--schema", "-s", help="Schema to use for validating."
    ),
):
    """Validates a json-file with a schema (json-schema.org)."""
    schema_json = json.load(schema)
    data = json_streams.load(infile)
    correct, errors = jt_val.validate(schema_json, data)
    json_streams.dump(correct, outfile)
    print(f"errors = {errors}")
    if errors:
        # (out_root, out_ext) = os.path.splitext(outfile)
        # errors_file_name = os.path.join(out_root, ".errors", out_ext)
        json_streams.dump(errors, sys.stderr)
        # click.echo("ERRORs found!!!")
        # click.echo("Errors are written to {0}".format(errors_file_name))
        raise typer.Exit(130)


@cli.command()
def convert(src: typer.FileBinaryRead, dst: typer.FileBinaryWrite):
    json_streams.dump(json_streams.load(src), dst)


if __name__ == "__main__":
    cli()
