import re
from collections import Counter

def parse_objdump(objdump_file):
    with open(objdump_file, 'r') as file:
        lines = file.readlines()

    instructions = []

    instruction_pattern = re.compile(r'\s+[0-9a-f]+:\s+([0-9a-f]+)\s+(\S+)\s+')

    for line in lines:
        match = instruction_pattern.match(line)
        if match:
            machine_code, instruction = match.groups()
            instructions.append(instruction)

    return instructions

def profile_instructions(instructions):
    instruction_counter = Counter(instructions)
    return instruction_counter

def print_instruction_profile(instruction_profile):
    print("Instruction Profile:")
    for instruction, count in instruction_profile.items():
        print(f"{instruction}: {count} times")

if __name__ == "__main__":
    objdump_file = 'objdump.txt'

    instructions = parse_objdump(objdump_file)

    instruction_profile = profile_instructions(instructions)

    print_instruction_profile(instruction_profile)

