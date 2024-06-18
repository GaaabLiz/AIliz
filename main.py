import typer

import core.cli.init

app = typer.Typer()


@app.command()
def scan_image(
        image_path: str,
        ai_scan: bool = False,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    core.cli.init.check_init()


@app.command()
def media_move(
        input_path: str,
        output_path: str,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    core.cli.init.check_init()


@app.command()
def init_clear():
    core.cli.init.delete_init()


@app.command()
def init():
    """
    Initialize the application on your system by creating the configuration file.
    """
    core.cli.init.check_init(True)
    core.cli.init.exec_init()


if __name__ == "__main__":
    app()
