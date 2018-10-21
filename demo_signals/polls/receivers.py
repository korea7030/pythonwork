def receiver(sender, **kwargs):
    print("receivers.py - I got it")
    print(kwargs['name'])
    print("Receiver was called.")
    print()

def receiver_second(sender, **kwargs):
    print("call second")
