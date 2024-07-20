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

    

    # Categorize instructions
    instruction_categories = {
        "Compute": [
            "lui", "addi", "srli", "mv", "subw", "li", "sub", "sext.w", "and", "srliw",
            "slli", "andi", "sll", "snez", "negw", "bltz", "blt", "slliw", "not", "srai",
            "bltu", "lh", "lb", "xor", "sllw", "seqz", "srlw", "sltu"
        ],
        "Load/Store": [
            "ld", "sd", "lw", "lbu", "sb", "sh", "sw", "lhu", "lb", "sh", "sw", "lbu", "lhu"
        ],
        "Control": [
            "rdcycle", "jal", "ret", "auipc", "beqz", "j", "bnez", "jalr", "bgez", "beq",
            "or", "bge", "srl", "sll", "bne", "blez", "addiw", "bgeu", "lb", "lhu", "neg",
            "bgtz", "xori", "xor", "sraiw", "sraw", "ecall", "sltu"
        ]
    }

    # Categorize instructions and count occurrences in each category
    categorized_counts = {category: 0 for category in instruction_categories}
    for instruction, count in instruction_profile.items():
        for category, category_instructions in instruction_categories.items():
            if instruction in category_instructions:
                categorized_counts[category] += count

    # Print categorized counts
    print("\nCategory Counts:")
    for category, count in categorized_counts.items():
        print(f"{category}: {count} times")

