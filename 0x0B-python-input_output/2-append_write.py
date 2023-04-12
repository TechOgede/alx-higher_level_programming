#!/usr/bin/python3
''' This module defines a function that
    appends a string to a  text file '''


def append_write(filename="", text=""):
    ''' Appends text onto a file referred to by 'filename
        Args:
            filename (str): name of file
            text (str): text content to be appended to the file
        Returns:
                the number of characters added to the file '''
    with open(filename, "a", encoding='utf-8') as f:
        num_chars_written = f.write(text)
    return num_chars_written
