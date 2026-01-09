question = (input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')).strip().lower()
answers = ["42", "forty-two", 'forty two']

if question in answers:
    print('Yes')
else:
    print('No')