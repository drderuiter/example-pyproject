import logging
from pathlib import Path

import click
import numpy as np
import yaml

from example_project.config import Config
from example_project.pipeline import Pipeline


@click.command()
@click.argument("config-file", type=click.Path(dir_okay=False, path_type=Path))
def main(config_file: Path):
    logging.basicConfig(level=logging.INFO)
    click.echo("Starting, reading config file.")
    config_raw = yaml.safe_load(config_file.read_text("utf-8"))
    config = Config(**config_raw)
    click.echo("Done reading config.")
    click.echo("Creating pipeline...")
    pipeline = Pipeline.from_config(config.steps)
    output = pipeline.run(np.array(config.input_value))
    click.echo(f"Done running pipeline. Output:\n  {output}")
