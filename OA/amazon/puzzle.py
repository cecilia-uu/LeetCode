def assemble_puzzle(pieces):
    # Step 1: Index the pieces by their ID
    left_to_right = {}
    top_to_bottom = {}
    for piece in pieces:
        if piece['leftId']:
            left_to_right[piece['leftId']] = piece['rightId']
        else:
            left_to_right["null"] = piece['rightId']
        if piece['topId']:
            top_to_bottom[piece['topId']] = piece['bottomId']
        else:
            top_to_bottom["null"] = piece['bottomId']
        if piece['leftId'] == None and piece['topId'] == None:
            top_left = [piece['rightId'], piece['bottomId']]
    
    # Step 3: Build the puzzle
    puzzle = []
    r, c = top_left

    while c != "null":
        current_r = r
        row = []

        # Traverse horizontally to build the row
        while current_r != "null":
            row.append(current_r)
            print(row)
            next_piece_id = left_to_right[current_r['rightId']]
            current_r = next_piece_id

        puzzle.append(row)

        # Move to the next row by using the bottomId of the first piece in the current row
        next_row_start_id = top_to_bottom[c['bottomId']]
        c = next_row_start_id

    # Convert puzzle to a 2D array of IDs for clarity
    return puzzle

# Example Usage
pieces = [
    {
        "id": "a5e93",
        "topId": "2184a",
        "leftId": None,
        "rightId": "8179f",
        "bottomId": None
    },
    {
        "id": "bc895",
        "leftId": None,
        "topId": None,
        "rightId": "47b84",
        "bottomId": "2184a"
    },
    {
        "id": "10ccb",
        "leftId": "8179f",
        "topId": "8881a",
        "rightId": None,
        "bottomId": None
    },
    {
        "id": "562d1",
        "leftId": "47b84",
        "topId": None,
        "rightId": None,
        "bottomId": "8881a"
    }
]

result = assemble_puzzle(pieces)
print(result)