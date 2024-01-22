def generate_user_message(texts, num_start=1, text_type='Sentence'):
    return '\n'.join(
        f'{text_type} {i}: {text}\n' 
        for i, text in enumerate(texts, start=num_start)
    )
