import re
from collections import Counter

def parse_log_file(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    instructions = []
    instr_count = Counter()

    between_cycles = False

    for line in lines:
        if "cycle" in line:
            between_cycles = not between_cycles
            continue
        
        if between_cycles:
            match = re.search(r'\S+\s+\S+\s+\S+\s+\(0x[0-9a-f]+\)\s+(\S+)\s+', line)
            if match:
                instruction = match.group(1)
                instructions.append(instruction)

                if instruction in ['mul', 'mulh', 'mulshu', 'mulhu', 'div', 'divu', 'rem', 'remu']:
                    instr_count['mul'] += 1
                elif instruction.endswith('.d'):
                    instr_count['double'] += 1
                elif instruction.startswith('f'):
                    instr_count['float'] += 1
                elif instruction.startswith('c.'):
                    instr_count['compressed'] += 1
                elif instruction.startswith('lr.') or instruction.startswith('sc.') or instruction.startswith('amo'):
                    instr_count['atomic'] += 1
                else:
                    instr_count['integer'] += 1

    return instructions, instr_count

# Example usage:
log_file = "spike.txt"  # Provide the path to your log file
instructions, instr_count = parse_log_file(log_file)
# print("Instructions:", instructions)
print("Instruction counts:", instr_count)

