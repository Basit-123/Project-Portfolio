import random

def build_markov_chain(text, n=2):
    """
    Build a Markov Chain from the input text.
    :param text: Input text as a string.
    :param n: Number of words to use as the key (state size).
    :return: A dictionary representing the Markov Chain.
    """
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)

    return markov_chain

def generate_text(chain, length=50):
    """
    Generate text using the Markov Chain.
    :param chain: The Markov Chain dictionary.
    :param length: Number of words to generate.
    :return: A string of generated text.
    """
    if not chain:
        return "No chain to generate text."

    # Start with a random key
    key = random.choice(list(chain.keys()))
    words = list(key)

    for _ in range(length - len(key)):
        if key in chain:
            next_word = random.choice(chain[key])
            words.append(next_word)
            key = tuple(words[-len(key):])  # Update key
        else:
            break

    return " ".join(words)

def main():
    print("Welcome to Markov Chain Composer!")
    print("Provide some text, and I'll generate new text based on it.")

    # Get input text
    input_text = input("Enter your text: ")
    if not input_text.strip():
        print("No text provided. Exiting...")
        return

    # Build the Markov Chain
    n = int(input("Enter the state size (e.g., 2 for pairs of words): ") or 2)
    chain = build_markov_chain(input_text, n=n)

    # Generate new text
    print("\nGenerated Text:")
    generated_text = generate_text(chain, length=50)
    print(generated_text)

if __name__ == "__main__":
    main()
