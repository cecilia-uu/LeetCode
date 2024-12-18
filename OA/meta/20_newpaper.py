def solution(paragraphs, aligns, width):
    # Initialize the result with a border
    res = ["*" * (width + 2)]
    
    # Process each paragraph
    for p, a in zip(paragraphs, aligns):
        line = []
        width_record = 0
        
        for w in p:
            # Check if adding the next word exceeds the width
            if width_record + len(w) + len(line) > width:
                # Add the current line to the result with the correct alignment
                if a == "LEFT":
                    res.append("* " + " ".join(line).ljust(width) + " *")
                else:  # RIGHT
                    res.append("* " + " ".join(line).rjust(width) + " *")
                line = []  # Start a new line
                width_record = 0  # Reset width record for the new line
            
            line.append(w)  # Add the word to the line
            width_record += len(w)  # Update the width record

        # Handle the last line of the paragraph
        if a == "LEFT":
            res.append("* " + " ".join(line).ljust(width) + " *")
        else:  # RIGHT
            res.append("* " + " ".join(line).rjust(width) + " *")

    # Add the bottom border
    res.append("*" * (width + 2))
    return res



paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["please look", "and align", "to right"]]
aligns = ["LEFT", "RIGIT", "RIGIT"]
width = 16 
print(solution(paragraphs, aligns, width))