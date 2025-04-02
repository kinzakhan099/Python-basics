counter=10
def increment():
    global counter
    counter += 5
    print(f"Counter incremented to: {counter}")
def decrement():
    counter=20
    counter -= 3
    print(f"Counter decremented to: {counter}")

increment()
print(f"Global counter after increment: {counter}")
decrement()
print(f"global counter after decrement: {counter}")
