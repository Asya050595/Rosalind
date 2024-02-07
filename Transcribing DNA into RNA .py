def transcribe_DNA_to_RNA(text):
    for i in text:
        if i == 'T':
            text = text.replace('T', 'U')
    return text

text = input()
print(transcribe_DNA_to_RNA(text))
