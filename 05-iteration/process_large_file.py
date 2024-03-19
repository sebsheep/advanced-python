from typing import Generator, TextIO


def read_by_chunk(
    # The TextIO type represent what is returned by the
    # open() function, so TextIO barely is "a file".
    file_object: TextIO,
    chunk_size: int = 4096,
) -> Generator[str, None, None]:
    # use a while loop and the .read(size) method to create
    # a generator yield chunks of the file given in parameters.
    # The size of the chunks also are passed in parameters.
    pass


def count_e(file_object: TextIO) -> int:
    count = 0
    for chunk in read_by_chunk(file_object, 1024):
        count += chunk.count("e")
    return count


if __name__ == "__main__":
    # The `with` construction automatically close the file
    # when we exit the block.
    with open("README.md", "r") as file_object:
        print("README.md has", count_e(file_object), "occurences of the letter e")
