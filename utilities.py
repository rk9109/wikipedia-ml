import mmap

def number_lines(filename):
    """
    Return: Number of lines in file
    """
    fn = open(filename, "r+")
    buf = mmap.mmap(fn.fileno(), 0)
    lines = 0
    while buf.readline(): lines += 1

    return lines
