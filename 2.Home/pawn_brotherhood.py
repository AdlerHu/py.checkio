def safe_pawns(pawns: set) -> int:
    # from b4 to (1,3)
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((col, row))
    
    unsafe_count = 0
    for p in pawns_indexes:
        if not (p[0]-1, p[1]-1) in pawns_indexes:
            if not (p[0]+1, p[1]-1) in pawns_indexes:
                unsafe_count += 1
    return len(pawns_indexes) - unsafe_count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")