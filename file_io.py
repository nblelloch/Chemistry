"""
Author: Nicholas Blelloch
Last updated: August 26, 2018

load data from external sources (e.g., raw data from instrumentation) into the
project.

https://jakevdp.github.io/PythonDataScienceHandbook/index.html
"""

import tkinter as tk
from tkinter import filedialog


def main():
    filename = select_data_file()
    return filename


def select_data_file():
    """
    Opens a dialogue box allowing the user to select a .jpg, .txt, or .csv file.

    :return: Path of selected file as a string
    """
    root = tk.Tk()
    root.withdraw()

    root.filename = filedialog.askopenfilename(
        initialdir="/Users/nicholasblelloch/Documents/",
        title="Select file",
        filetypes=(
            ("jpeg files", "*.jpg"),
            ("text files", "*.txt"),
            ("csv files", "*.csv"),
            ("all files", "*.*")))

    if not root.filename:
        print('Cannot proceed without a selected file. Please run again.')
        return None
    else:
        print(root.filename, type(root.filename))
        return root.filename


if __name__ == '__main__':
    main()
