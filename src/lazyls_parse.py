import os

if __name__ == "__main__":
    # List the directory
    items: list[str] = os.listdir()
    flagdir_items: list[tuple[int, str]] = [
        (1, item) if os.path.isdir(item) else (0, item) for item in items
    ]
    # Sort the items
    flagdir_items.sort()
    # Generate indexed table, if dir, add suffix "/".
    indexed_table: list[tuple[str, str]] = [
        (str(ix), item + "/" * flag) for ix, (flag, item) in enumerate(flagdir_items)
    ]

    # Get input
    userinput: str = int(input())
    result: str = indexed_table[userinput][1]
    # Print the path in format
    print(f"::LZOUT::\t{result}\n", end="")
