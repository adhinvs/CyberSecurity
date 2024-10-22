from itertools import product, combinations

# Load base words and dictionary words from files
def load_words(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

# Custom characters to use
custom_characters = "!@#$%&*1234567890"

# Length of generated passwords (adjust as needed)
min_length = 8
max_length = 8

# Function to create wordlist
def generate_wordlist(base_words, dictionary_words):
    with open("custom_wordlist.txt", "w") as f:
        # Generate combinations of base words with custom characters
        for bw1, bw2 in combinations(base_words, 2):
            for char in custom_characters:
                combined_base = bw1 + char + bw2
                if min_length <= len(combined_base) <= max_length:
                    f.write(combined_base + "\n")
                
                # Also try combinations like bw1 + bw2, bw2 + char + bw1
                reversed_combined = bw2 + char + bw1
                if min_length <= len(reversed_combined) <= max_length:
                    f.write(reversed_combined + "\n")

        for base in base_words:
            for length in range(min_length, max_length + 1):
                # Combine base words with dictionary words
                for num_words in range(1, length - len(base) + 1):
                    for combo in combinations(dictionary_words, num_words):
                        potential_password = base + "".join(combo)
                        if min_length <= len(potential_password) <= max_length:
                            f.write(potential_password + "\n")

                        # Insert characters between the words
                        for char in custom_characters:
                            # Example: base + char + combo
                            mixed_password = base + char + "".join(combo)
                            if min_length <= len(mixed_password) <= max_length:
                                f.write(mixed_password + "\n")
                                
                            # Insert the base word at different positions with custom characters
                            for i in range(len(combo) + 1):
                                parts = list(combo)
                                parts.insert(i, base)
                                mixed_password = char.join(parts)
                                if min_length <= len(mixed_password) <= max_length:
                                    f.write(mixed_password + "\n")

                            # Add characters at the beginning or end
                            with_prefix = char + potential_password
                            with_suffix = potential_password + char

                            if min_length <= len(with_prefix) <= max_length:
                                f.write(with_prefix + "\n")
                            if min_length <= len(with_suffix) <= max_length:
                                f.write(with_suffix + "\n")

# Load base words from "base_words.txt" and dictionary words from "dictionary.txt"
base_words = load_words("guess.txt")
dictionary_words = load_words("dictionary.txt")
generate_wordlist(base_words, dictionary_words)
