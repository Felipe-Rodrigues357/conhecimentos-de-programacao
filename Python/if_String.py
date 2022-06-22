Str = "it's python!"

print("Before if:", Str)

if 'p' in Str:
    Str = "It's Python"
elif 'i' in Str:
    Str.capitalize()
else:
    pass

print("After if:", Str)