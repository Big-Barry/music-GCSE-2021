d = {'Ash v4': 9, 'ash v6': 0, 'ash v3': 1, 'ash v2': 0, 'ash': 4, 'Ash v5': 7}
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)