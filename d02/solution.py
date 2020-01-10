def checksum(spreadsheet):
    """Compute the checksum of the spreadsheet."""
    checksum = 0
    for row in spreadsheet:
        checksum += max(row) - min(row)
    return checksum


def evenly_disible_checksum(spreadsheet):
    """Compute the checksum of the spreadsheet from evenly divible values."""
    checksum = 0
    for row in spreadsheet:
        match = False
        for value in row:
            for second_value in row:
                if second_value != value and value % second_value == 0:
                    checksum += value // second_value
                    match = True
                    break
            if match:
                break
    return checksum


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    spreadsheet = [list(map(int, row.split("\t"))) for row in input.splitlines()]
    print(checksum(spreadsheet))
    print(evenly_disible_checksum(spreadsheet))
