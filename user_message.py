EXPECTED_OUTPUT_STR = """EXPECTED OUTPUT
Return only the labels for the snippets above. Do not return any 
other text. Use the following format:

Snippet 1: <LABEL>
Snippet 2: <LABEL>
Snippet 3: <LABEL>
..."""


def generate_user_message(texts, num_start=1):
    return 'SENTENCES\n' + '\n'.join(
        f'Snippet {i}: {text}' 
        for i, text in enumerate(texts, start=num_start)
    ) + '\n\n' + EXPECTED_OUTPUT_STR
