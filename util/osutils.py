import datetime
import os
import shutil
import subprocess


def get_home_dir():
    """
    Get the home directory of the current user
    :return: The home directory of the current user
    """
    return os.path.expanduser("~")


def get_app_home_dir(app_name, create_if_not: bool = True):
    """
    create and return the home directory for the application
    :param create_if_not: boolean flag to create the directory if it does not exist
    :param app_name:  name of the application
    :return: home directory for the application
    """
    home_dir = get_home_dir()
    app_home_dir = os.path.join(home_dir, app_name)
    if create_if_not:
        if not os.path.exists(app_home_dir):
            os.makedirs(app_home_dir)
    return app_home_dir


def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def check_path(path, create_if_not: bool = False) -> bool:
    """
    Check if the path exists and is readable
    :param path: path to check
    :param create_if_not: create the path if it does not exist
    :return: True if the path exists and is readable, False otherwise
    """
    if not os.path.exists(path):
        if create_if_not:
            os.makedirs(path)
        else:
            return False
    if not os.access(path, os.R_OK):
        return False
    return True


def check_path_2(path):
    # Check if the path exists and is readable
    if not os.path.exists(path):
        raise IOError(f'Path {path} does not exist!')
    if not os.access(path, os.R_OK):
        raise PermissionError(f'Path {path} is not readable!')
    # Check if the path is a directory
    if not os.path.isdir(path):
        raise NotADirectoryError(f'Path {path} is not a directory!')


def get_second_to_last_directory(path):
    # Divide il percorso in una lista di componenti
    path_components = os.path.normpath(path).split(os.sep)
    # Controlla che il percorso abbia almeno due componenti
    if len(path_components) < 2:
        return None
    # Restituisce il secondo componente dal fondo della lista
    return path_components[-2]


def count_pathsub_files(path):
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files)
    return count


def count_pathsub_dirs(path):
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(dirs)
    return count


def count_pathsub_elements(path):
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files) + len(dirs)
    return count


def get_folder_size_mb(path):
    # Inizializza la dimensione totale a 0
    total_size = 0
    # Scansione delle cartelle e dei file all'interno del percorso dato
    for root, dirs, files in os.walk(path):
        # Aggiungi le dimensioni dei file alla dimensione totale
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    # Converti la dimensione totale in megabyte (MB)
    total_size_mb = total_size / (1024 * 1024)
    return total_size_mb


def open_system_folder(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path {path} does not exist!")
    if os.name == 'nt':  # For Windows
        subprocess.Popen(['explorer', path])
    elif os.name == 'posix':  # For Linux, Mac
        subprocess.Popen(['open', path])
    else:
        raise OSError("Unsupported OS")


def folder_already_present(path1, path2):  # SBAGLIATO
    folder_name_from = os.path.basename(os.path.normpath(path1))
    folder_name_to = os.path.basename(os.path.normpath(path2))
    if os.path.exists(path2):
        return True
    else:
        return False


def has_disk_free_space(pathOfDisk, mbFree):
    stat = shutil.disk_usage(pathOfDisk)
    spazio_disponibile_mb = stat.free / (1024 * 1024)
    if spazio_disponibile_mb > mbFree:
        return True
    else:
        return False



