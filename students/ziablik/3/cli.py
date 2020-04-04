# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
import os   # noqa I001


def ls_execution(directory=None):
    """Ls command execution function."""
    dirs_and_files = []
    if directory is None:
        directory = os.getcwd()
    for dir_name in os.listdir(directory):
        if '.' not in dir_name:
            dirs_and_files.append(dir_name)
    for file_name in os.listdir(directory):
        if '.' in file_name:
            dirs_and_files.append(file_name)
    return dirs_and_files


def mk_execution(file_name):
    """Mk command execution function."""
    try:    # noqa: WPS229
        if os.path.isfile(file_name):
            return False
        else:
            new_file = open(file_name, 'w+')    # noqa: WPS515
            new_file.close()
        return True
    except OSError:
        return False


def rm_execution(file_name):
    """Rm command execution function."""
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        return False
    return True


def contains_execution(file_name):
    """Contains command execution function."""
    if os.path.isfile(file_name):
        return True
    return False


def since_execution(given_datetime, directory=None):    # noqa: C901
    """Since command execution function."""
    if directory is None:
        directory = os.getcwd()
    try:    # noqa: WPS229
        date = datetime.strptime(given_datetime, '%Y-%m-%d %H:%M:%S')
        files = []
        for file_name in os.listdir(directory):
            if directory == os.getcwd():
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(file_name),
                )
            else:
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(directory / file_name),
                )
            if file_datetime > date:
                files.append(file_name)
        return files
    except ValueError:
        return 'Using mask Y-M-D H:M:S'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        type=str,
        nargs='*',
    )
    command = parser.parse_args()
    caller = command.command[0]
    args = None
    command_list = {
        'ls': ls_execution,
        'mk': mk_execution,
        'rm': rm_execution,
        'contains': contains_execution,
        'since': since_execution,
    }
    if caller in command_list:
        if len(command.command) > 1:
            args = command.command[1]
        function_to_call = command_list[caller]
        print(function_to_call(args))   # noqa: T001
    else:
        print('Invalid command without arguments')  # noqa: T001
