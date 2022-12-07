import dataclasses
import sys
from pathlib import Path
from typing import Optional

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


@dataclasses.dataclass(frozen=True, eq=True)
class File:
    name: str
    size: int


class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.size: int = 0
        self.files: dict[str] = {}
        self.directories: dict[str] = {}
        self.parent = parent

    def add_file(self, file: File):
        if file.name not in self.files.keys():
            self.add_file_helper(file, file.size)

    def add_file_helper(self, file: File, size: int):
        self.files[file.name] = file
        curr = self
        while curr is not None:
            curr.size += size
            curr = curr.parent

    def add_directory(self, directory) -> bool:
        if directory.name not in self.directories.keys():
            self.directories[directory.name] = directory
            return True
        return False

    def tree(self, indent=""):
        print(f'{indent} - {self.name} (dir size={self.size})')
        for directory in self.directories.values():
            directory.tree(indent + "  ")

        for file in self.files.values():
            print(f'{indent}   - {file.name} (file, size={file.size})')

    def __repr__(self):
        return f"Directory(name={self.name}, size={self.size}, parent={self.parent})"


def main():
    lines = ProblemParser().load_input(2022, 7)
    root = Directory("/", None)
    curr = root
    dirs = set()
    for line in lines:
        split_line = line.split(" ")
        if split_line[0] == "$":
            cmd = split_line[1]
            if cmd == "ls":
                continue
            if cmd == "cd":
                name = split_line[2]
                if name == "..":
                    curr = curr.parent
                elif name == "/":
                    curr = root
                elif name in curr.directories:
                    curr = curr.directories[name]
                else:
                    directory = Directory(name, curr)
                    added = curr.add_directory(directory)
                    if added:
                        dirs.add(directory)
                    curr = curr.directories[name]

        else:
            name = split_line[1]
            if split_line[0] == "dir":
                directory = Directory(name, curr)
                added = curr.add_directory(directory)
                if added:
                    dirs.add(directory)
            elif split_line[0] != "dir":
                size = int(split_line[0])
                file = File(name=name, size=size)
                curr.add_file(file)

    result = [d.size for d in dirs if d.size <= 100000]
    print(f"Part 1: {sum(result)}")

    free_space = 70000000 - root.size
    need_to_free = -(free_space-30000000)
    result = [d.size for d in dirs if d.size >= need_to_free]
    print(f"Part 2: {min(result)}")




if __name__ == '__main__':
    main()
