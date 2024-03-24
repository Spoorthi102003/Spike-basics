
def categorize_instructions(log_file):
    # Initialize counters for each instruction category
    instr_count = {
        'integer': 0,
        'mul': 0,
        'double': 0,
        'float': 0,
        'atomic': 0,
        'compressed': 0
    }

    # Open the log file for reading
    with open(log_file, 'r') as file:
        # Flag to indicate if we're between two "cycle" words
        between_cycles = False

        # Iterate through each line in the log file
        for line in file:
            # Check if the line contains the keyword 'cycle'
            if 'cycle' in line:
                # Toggle the flag indicating we're between cycles
                between_cycles = not between_cycles
                # If this is the end of a cycle block, break the loop
                if not between_cycles:
                    break
            # If we're between cycles and the line contains instructions
            elif between_cycles and line.strip():
                # Extract the instruction from the line
                instr = line.split()[-2]
                # Categorize the instruction based on keywords
                if instr in ['mul', 'mulh', 'mulshu', 'mulhu', 'div', 'divu', 'rem', 'remu']:
                    instr_count['mul'] += 1
                elif instr.endswith('.d'):
                    instr_count['double'] += 1
                elif instr.startswith('f'):
                    instr_count['float'] += 1
                elif instr.startswith('c.'):
                    instr_count['compressed'] += 1
                elif instr.startswith('lr.') or instr.startswith('sc.') or instr.startswith('amo'):
                    instr_count['atomic'] += 1
                else:
                    instr_count['integer'] += 1

    # Print the count of instructions in each category
    for category, count in instr_count.items():
        print(f'{category}: {count}')


# Usage example
log_file = '/home/spoorthi-s/Desktop/profiler/spike.txt'
categorize_instructions(log_file)

