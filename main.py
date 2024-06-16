import typer

import controller.init
from controller import *

app = typer.Typer()


@app.command()
def main():
    """
    Start the application
    :return:
    """
    pass


@app.command()
def init():
    """
    Initialize the application on your system by creating the configuration file.
    """
    controller.init.exec_init()


if __name__ == "__main__":
    app()
