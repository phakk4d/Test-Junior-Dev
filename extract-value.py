def extract_values (nbrs):
    values = []
    for item in nbrs :
        if isinstance(item, int) :
            values.append(item)
        else:
            values.extend(extract_values(item))
    return values

nbrs = (1, 2, (3, 4, 5, (6, 7),8), 9, 10)
values = extract_values(nbrs)
for value in values :
    print (value) 