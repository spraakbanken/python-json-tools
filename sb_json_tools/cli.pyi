import typer
from json_streams import jsonlib as jsonlib
from sb_json_tools import jt_val as jt_val
from typing import Any

cli: Any

def validate(infile: typer.FileBinaryRead, outfile: typer.FileBinaryWrite, schema: typer.FileBinaryRead=...) -> Any: ...
def convert(src: typer.FileBinaryRead, dst: typer.FileBinaryWrite) -> Any: ...
