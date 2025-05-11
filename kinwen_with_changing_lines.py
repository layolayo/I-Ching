import itertools
from fractions import Fraction
import io
import csv  # New import for CSV writing

# Context based on your information
current_datetime_info = "Saturday, May 10, 2025 at 10:23:53 PM WAT. Location: Lagos, Lagos, Nigeria."
print(f"Context: {current_datetime_info}\n")

# --- Trigram and King Wen Map Definitions (Programmatic Generation) ---
# (Assuming trigrams, king_wen_sequence_data, and generate_king_wen_map are defined as in the last correct version)
trigrams = {
    "Qian": (1, 1, 1), "Kun": (0, 0, 0), "Zhen": (1, 0, 0), "Kan": (0, 1, 0),
    "Gen": (0, 0, 1), "Sun": (0, 1, 1), "Li": (1, 0, 1), "Dui": (1, 1, 0)
}
king_wen_sequence_data = [
    (1, "Qian", "Qian", "Qian"), (2, "Kun", "Kun", "Kun"), (3, "Zhun", "Zhen", "Kan"), (4, "Meng", "Kan", "Gen"),
    (5, "Xu", "Qian", "Kan"), (6, "Song", "Kan", "Qian"), (7, "Shi", "Kan", "Kun"), (8, "Bi", "Kun", "Kan"),
    (9, "Xiao Chu", "Qian", "Sun"), (10, "Lu", "Dui", "Qian"),
    (11, "Tai", "Qian", "Kun"), (12, "Pi", "Kun", "Qian"), (13, "Tong Ren", "Qian", "Li"), (14, "Da You", "Li", "Qian"),
    (15, "Qian", "Gen", "Kun"), (16, "Yu", "Kun", "Zhen"), (17, "Sui", "Zhen", "Dui"), (18, "Gu", "Sun", "Gen"),
    (19, "Lin", "Dui", "Kun"), (20, "Guan", "Kun", "Sun"), (21, "Shi He", "Zhen", "Li"), (22, "Bi", "Li", "Gen"),
    (23, "Bo", "Kun", "Gen"), (24, "Fu", "Zhen", "Kun"), (25, "Wu Wang", "Zhen", "Qian"),
    (26, "Da Chu", "Qian", "Gen"),
    (27, "Yi", "Zhen", "Gen"),
    (28, "Da Guo", "Sun", "Dui"), (29, "Kan", "Kan", "Kan"), (30, "Li", "Li", "Li"),
    (31, "Xian", "Gen", "Dui"), (32, "Heng", "Sun", "Zhen"),
    (33, "Dun", "Gen", "Qian"),
    (34, "Da Zhuang", "Qian", "Zhen"), (35, "Jin", "Kun", "Li"), (36, "Ming Yi", "Li", "Kun"),
    (37, "Jia Ren", "Li", "Sun"), (38, "Kui", "Dui", "Li"), (39, "Jian", "Gen", "Kan"), (40, "Xie", "Kan", "Zhen"),
    (41, "Sun", "Dui", "Gen"), (42, "Yi", "Zhen", "Sun"), (43, "Guai", "Qian", "Dui"), (44, "Gou", "Sun", "Qian"),
    (45, "Cui", "Kun", "Dui"), (46, "Sheng", "Sun", "Kun"), (47, "Kun", "Kan", "Dui"),
    (48, "Jing", "Sun", "Kan"), (49, "Ge", "Li", "Dui"), (50, "Ding", "Sun", "Li"),
    (51, "Zhen", "Zhen", "Zhen"), (52, "Gen", "Gen", "Gen"), (53, "Jian", "Gen", "Sun"),
    (54, "Gui Mei", "Dui", "Zhen"), (55, "Feng", "Li", "Zhen"), (56, "Lu", "Gen", "Li"),
    (57, "Sun", "Sun", "Sun"), (58, "Dui", "Dui", "Dui"), (59, "Huan", "Kan", "Sun"),
    (60, "Jie", "Dui", "Kan"), (61, "Zhong Fu", "Dui", "Sun"), (62, "Xiao Guo", "Gen", "Zhen"),
    (63, "Ji Ji", "Li", "Kan"), (64, "Wei Ji", "Kan", "Li")
]


def generate_king_wen_map(trigram_data, sequence_data):
    generated_map = {}
    valid_trigram_names = trigram_data.keys()
    map_errors = []
    all_tuples_generated = []
    for number, name, lower_name, upper_name in sequence_data:
        if lower_name not in valid_trigram_names or upper_name not in valid_trigram_names:
            map_errors.append(f"Invalid trigram name for Hex {number} ({name})")
            continue
        lower_tuple = trigram_data[lower_name]
        upper_tuple = trigram_data[upper_name]
        hex_tuple = lower_tuple + upper_tuple
        if hex_tuple in generated_map:
            map_errors.append(
                f"Duplicate structure {hex_tuple} found! Original: {generated_map[hex_tuple]}, New: ({number}, '{name}')")
        generated_map[hex_tuple] = (number, name)
        all_tuples_generated.append(hex_tuple)

    if len(generated_map) != 64:
        map_errors.append(f"ERROR: Generated map has {len(generated_map)} entries, expected 64.")
    if len(all_tuples_generated) != len(set(all_tuples_generated)):
        map_errors.append("ERROR: Duplicate hexagram structures generated from sequence data! (sequence_data issue)")

    if not map_errors:
        print("Programmatically generated Hexagram map verified: Contains 64 unique entries.")
    else:
        print("ERROR(S) generating king_wen_map:")
        for error in map_errors:
            print(f"- {error}")
    return generated_map


king_wen_map = generate_king_wen_map(trigrams, king_wen_sequence_data)

# --- Probability Definitions (from user's 38-object model) ---
line_probs = {
    6: Fraction(2, 38),  # Old Yin
    7: Fraction(11, 38),  # Young Yang
    8: Fraction(17, 38),  # Young Yin
    9: Fraction(8, 38)  # Old Yang
}
line_values = [6, 7, 8, 9]
denominator = 38 ** 6
num_possible_outcomes = 4 ** 6


# --- Helper Functions (get_basic_hex_tuple, get_transformed_hex_info, get_hex_symbol, get_ordinal, get_changing_lines_text remain the same) ---
def get_basic_hex_tuple(line_sequence):
    basic_tuple = []
    for line in line_sequence:
        if line == 6 or line == 8:
            basic_tuple.append(0)  # Yin
        elif line == 7 or line == 9:
            basic_tuple.append(1)  # Yang
    return tuple(basic_tuple)


def get_hex_symbol(hex_number_val):
    if isinstance(hex_number_val, str):
        if hex_number_val.isdigit():
            hex_number_val = int(hex_number_val)
        else:
            return hex_number_val
    if 1 <= hex_number_val <= 64:
        return chr(0x4DC0 + hex_number_val - 1)
    return "Invalid #"


def get_transformed_hex_info(original_outcome_tuple, king_wen_map_dict):
    transformed_basic_lines = []
    has_changed_lines = False
    for line in original_outcome_tuple:
        if line == 6:
            transformed_basic_lines.append(1); has_changed_lines = True
        elif line == 9:
            transformed_basic_lines.append(0); has_changed_lines = True
        elif line == 7:
            transformed_basic_lines.append(1)
        elif line == 8:
            transformed_basic_lines.append(0)
        else:
            return "Error", "Invalid Line", "Error"
    if not has_changed_lines: return "N/A", "No Change", "N/A"
    transformed_basic_tuple = tuple(transformed_basic_lines)
    if transformed_basic_tuple in king_wen_map_dict:
        hex_num, hex_name = king_wen_map_dict[transformed_basic_tuple]
        return hex_num, hex_name, get_hex_symbol(hex_num)
    return "Error", "Transformed Hex Not Found", "Error"


def get_ordinal(n):
    if 11 <= (n % 100) <= 13: return str(n) + 'th'
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')


def get_changing_lines_text(original_outcome_tuple):
    descriptions = []
    positions = [get_ordinal(i + 1) for i in range(6)]
    for i, line_val in enumerate(original_outcome_tuple):
        if line_val == 6:
            descriptions.append(f"6 (Old Yin) in the {positions[i]} place")
        elif line_val == 9:
            descriptions.append(f"9 (Old Yang) in the {positions[i]} place")
    if not descriptions: return "No changing lines"
    if len(descriptions) == 1: return descriptions[0]
    return ", ".join(descriptions[:-1]) + ", and " + descriptions[-1]


# --- Main Calculation ---
print(f"\nCalculating probabilities for all {num_possible_outcomes} possible hexagram outcomes...")
# ... (other print statements remain the same) ...
print("-" * 30)

csv_output = io.StringIO()
# Create a CSV writer object. This will handle quoting fields with commas.
csv_writer = csv.writer(csv_output)

header = ["Line1", "Line2", "Line3", "Line4", "Line5", "Line6",
          "Probability_Numerator", "Probability_Denominator", "Probability_Percent_6dp",
          "Initial_Hex_Symbol", "Initial_Hex_Number", "Initial_Hex_Name",
          "Changing_Lines_Description",
          "Transformed_Hex_Symbol", "Transformed_Hex_Number", "Transformed_Hex_Name"]
csv_writer.writerow(header)  # Write header using the csv writer

total_prob = Fraction(0)

if len(king_wen_map) == 64:
    for hex_outcome in itertools.product(line_values, repeat=6):
        prob = Fraction(1)
        for line in hex_outcome:
            prob *= line_probs[line]
        total_prob += prob

        initial_hex_num_val = "Error"
        initial_hex_name = "Initial Hex Not Found"
        initial_hex_symbol = "Error"

        basic_initial_tuple = get_basic_hex_tuple(hex_outcome)
        if basic_initial_tuple in king_wen_map:
            initial_hex_num_val, initial_hex_name = king_wen_map[basic_initial_tuple]
            initial_hex_symbol = get_hex_symbol(initial_hex_num_val)

        changing_lines_desc = get_changing_lines_text(hex_outcome)
        trans_hex_num_val, trans_hex_name, trans_hex_symbol = get_transformed_hex_info(hex_outcome, king_wen_map)

        prob_percentage_str = f"{float(prob) * 100:.6f}%"
        line_str_list = [str(line) for line in hex_outcome]

        row_data = line_str_list + \
                   [str(prob.numerator), str(prob.denominator), prob_percentage_str,
                    initial_hex_symbol, str(initial_hex_num_val), initial_hex_name,
                    changing_lines_desc,  # This field will be properly quoted by csv_writer
                    trans_hex_symbol, str(trans_hex_num_val), trans_hex_name]
        csv_writer.writerow(row_data)  # Write data row using the csv writer

    # ... (The rest of the script: print completion, verification, CSV string retrieval, and file saving remains the same) ...
    print(f"\nCalculation complete for {num_possible_outcomes} outcomes.")
    print(f"Sum of all probabilities: {total_prob.numerator}/{total_prob.denominator}")
    if total_prob == 1:
        print("Verification successful: Total probability sums to 1.")
    else:
        print(f"Verification FAILED: Total probability is {total_prob}, should be 1.")

    full_csv_string = csv_output.getvalue()
    csv_output.close()

    print("\n--- Start of CSV Output (Header + First 5 Data Rows) ---")
    csv_lines = full_csv_string.splitlines()
    for i in range(min(6, len(csv_lines))): print(csv_lines[i])
    print("--- End of CSV Output Snippet ---")
    print(f"\nFull CSV data has {len(csv_lines)} lines (including header).")

    file_name = "hexagram_probabilities_full_details.csv"
    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as f:
            f.write(full_csv_string)
        print(f"\nSuccessfully saved the full CSV data to '{file_name}' in the current directory.")
    except Exception as e:
        print(f"\nError saving file '{file_name}': {e}")
else:
    print("\nSkipping main calculation due to errors in King Wen Map generation.")