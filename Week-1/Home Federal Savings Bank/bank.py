user_greeting = input("Greeting: ")
if user_greeting.startswith('Hello'):
    print('$0')
elif user_greeting == "How you doing?":
    print('$20')
elif user_greeting == "What's happening?" or user_greeting == "What's up?":
    print('$100')