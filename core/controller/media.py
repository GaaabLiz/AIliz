import os

import rich
import typer

from cli.asker import ask_yes_no, ask_which_media_format
from core.model.ailiz_image import AilizImage
from util import osutils


def organize_media(
        input_path: str,
        output_path: str,
        chooser: bool = False,
        add_comment_metadata: bool = False,
        create_ailiz_file: bool = False,
):
    # Check if the paths are valid
    try:
        osutils.check_path_2(input_path)
        osutils.check_path_2(output_path)
    except Exception as e:
        rich.print(f"Error while checking input/output path: {e}")
        print("Make sure the paths are valid and try again.")
        raise typer.Exit()

    # Scan input path
    rich.print(f"Scanning input path: {input_path}")
    input_image_files_paths = osutils.scan_directory_match_bool(input_path, osutils.is_image_file)
    rich.print(f"Found {len(input_image_files_paths)} image files in {input_path}")
    input_images = []
    for image_path in input_image_files_paths:
        try:
            image = AilizImage(image_path)
            input_images.append(image)
            rich.print(f"Loaded image: {image}")
        except Exception as e:
            rich.print(f"[red]Error[/red] while processing image {image_path}: {e}")
    rich.print(f"Processed {len(input_images)}/{len(input_image_files_paths)} images.")

    # check available disk space for all the images
    total_size_mb = sum([image.size_mb for image in input_images])
    if not osutils.has_disk_free_space(output_path, total_size_mb):
        rich.print(f"[red]Error[/red]: Not enough disk space (on output directory) to copy all the images.")
        raise typer.Exit()

    # ask which format to use for the output directory
    output_format = ask_which_media_format("Which format do you want to use for the output directory? ")

    # ask confirmation for moving
    ask_confirmation = ask_yes_no("All the images will be moved to the output directory. Do you want to continue?")
    if not ask_confirmation:
        rich.print("Operation aborted.")
        raise typer.Exit()

    # creo cartella di output per tutte le immagini
    for image in input_images:
        image.load_output_path(output_format, output_path)
        os.makedirs(image.output_path, exist_ok=True)

    # move the images or open the chooser
    for image in input_images:
        full_path = os.path.join(image.output_path, image.file_name)
        duplicate = os.path.exists(full_path)
        if duplicate:
            rich.print(f"Skipping [bold]{image.file_name}[/bold] because it already exists in the output directory.")
        else:
            rich.print(f"Moving [green]{image.file_name}[/green] to {image.output_path}")
            # shutil.move(image.path, image.output_path)

