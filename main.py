import typer

import core.controller.init
import core.controller.media
from core.controller.eagle_imp import *

app = typer.Typer()


@app.command()
def scan_image(
        image_path: str,
        ai_scan: bool = False,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    core.controller.init.check_init()


@app.command()
def media_org(
        input_path: str,
        output_path: str,
        chooser: bool = False,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    core.controller.init.check_init()
    core.controller.media.organize_media(input_path, output_path, chooser, add_comment_metadata, create_ailiz_file)


@app.command()
def eagle_imp(
        input_path: str,
        ai_comment: bool = False,
        ai_tag: bool = False,
        ai_metadata: bool = False,
        ai_rename: bool = False,
):
    core.controller.init.check_init()
    eagle_dir_importer(input_path, ai_comment, ai_tag, ai_metadata, ai_rename)


@app.command()
def init_clear():
    core.controller.init.delete_init()


@app.command()
def init():
    """
    Initialize the application on your system by creating the configuration file.
    """
    core.controller.init.check_init(True)
    core.controller.init.exec_init()


if __name__ == "__main__":
    app()
