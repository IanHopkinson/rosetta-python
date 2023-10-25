#!/usr/bin/env python
# encoding: utf-8

"""
A commandline utility to count words in a file
"""

import sys


def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print(f"{len(sys.argv) - 1} arguments provided, 1 expected. Exiting without action")
        sys.exit()

    word_count = word_statistics(file_path)

    print(f"File {file_path} counts {word_count} words", flush=True)


def word_statistics(file_path: str) -> int:
    word_count = 0

    with open(file_path, mode="r", encoding="utf-8") as file_handle:
        for line in file_handle.readlines():
            words = line.split(" ")
            word_count += len(words)

    return word_count


if __name__ == "__main__":
    main()
