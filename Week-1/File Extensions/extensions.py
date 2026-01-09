user_input_extension = input('File name: ').strip().lower()


if user_input_extension.endswith('.gif'):
    print('image/gif')
elif user_input_extension.endswith('.jpg'):
    print('image/jpeg')
elif user_input_extension.endswith('.jpeg'):
    print('image/jpeg')
elif user_input_extension.endswith('.png'):
    print('image/png')
elif user_input_extension.endswith('.pdf'):
    print('application/pdf')
elif user_input_extension.endswith('.txt'):
    print('text/plain')
elif user_input_extension.endswith('.zip'):
    print('application/zip')
elif user_input_extension.endswith(''):
    print('application/octet-stream')
