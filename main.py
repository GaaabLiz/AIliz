import typer

import controller.init
from controller import *

app = typer.Typer()


@app.command()
def scan_image(
        image_path: str,
        ai_scan: bool = False,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    controller.init.check_init()


@app.command()
def media_move(
        input_path: str,
        output_path: str,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    controller.init.check_init()


@app.command()
def init_clear():
    controller.init.delete_init()


@app.command()
def init():
    """
    Initialize the application on your system by creating the configuration file.
    """
    controller.init.check_init(True)
    controller.init.exec_init()


if __name__ == "__main__":
    app()
