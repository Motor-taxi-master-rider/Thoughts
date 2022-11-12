import math
import pathlib
from collections import OrderedDict
from operator import itemgetter
from typing import Dict


def get_dir_size(path: pathlib.Path) -> int:
    path_size = 0
    for p in path.rglob("*"):
        path_size += p.stat().st_size
    return path_size


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def calculate_size(path: pathlib.Path, sort_by_size):
    if path.is_file():
        # single file
        print(f"{path.name:<40}{convert_size(path.stat().st_size):<40}")
        return

    size_map: Dict[pathlib.Path, int] = OrderedDict()

    for path in path.iterdir():
        if path.is_dir():
            size_map[path] = get_dir_size(path)
        elif path.is_file():
            size_map[path] = path.stat().st_size

    if sort_by_size:
        sorted_by_size = sorted(size_map.items(), key=itemgetter(1), reverse=True)
        for path, path_size in sorted_by_size:
            print(f"{path.name:<40}{convert_size(path_size):<40}")
    else:
        for path, path_size in size_map.items():
            print(f"{path.name:<40}{convert_size(path_size):<40}")


if __name__ == '__main__':
    size = calculate_size(pathlib.Path("G:\sg-phngrm-1.2-pc"))
    print(size)
