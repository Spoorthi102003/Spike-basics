import re
from collections import Counter

def parse_log_file(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    instructions = []

    instruction_pattern = re.compile(r'\S+\s+\S+\s+\S+\s+\(0x[0-9a-f]+\)\s+(\S+)\s+')

    for line in lines:
        match = instruction_pattern.search(line)
        if match:
            instruction = match.group(1)
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
    log_file = 'spike.txt'

    instructions = parse_log_file(log_file)

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

    # Print instruction profile
    print_instruction_profile(instruction_profile)

    # Print categorized counts
    print("\nCategory Counts:")
    for category, count in categorized_counts.items():
        print(f"{category}: {count} times")

