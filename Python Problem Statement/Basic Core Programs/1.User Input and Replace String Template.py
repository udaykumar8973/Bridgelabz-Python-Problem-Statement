username = input('Enter your "name" : ')
if len(username) > 3:
    print('Hello', username, 'How are you?')
else:
    print("invalid character length should be greater than 3")