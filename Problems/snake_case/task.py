val = input()

if not val.islower():
    connection = ""
    for s in val:
        if s.islower():
            connection += s
        else:
            connection += "_"
            connection += s.lower()

    print(connection)
else:
    print(val)
