import sys
import json

import typer

import json_arrays
from sb_json_tools import jt_val


__version__ = "0.10.0"


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
    data = json_arrays.load(infile)
    correct, errors = jt_val.validate(schema_json, data)
    json_arrays.dump(correct, outfile)
    print(f"errors = {errors}")
    if errors:
        # (out_root, out_ext) = os.path.splitext(outfile)
        # errors_file_name = os.path.join(out_root, ".errors", out_ext)
        json_arrays.dump(errors, sys.stderr.buffer)
        # click.echo("ERRORs found!!!")
        # click.echo("Errors are written to {0}".format(errors_file_name))
        raise typer.Exit(130)


@cli.command()
def convert(src: typer.FileBinaryRead, dst: typer.FileBinaryWrite):
    json_arrays.dump(json_arrays.load(src), dst)


if __name__ == "__main__":
    cli()
