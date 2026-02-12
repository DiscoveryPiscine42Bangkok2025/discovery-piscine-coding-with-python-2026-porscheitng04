org = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for i in org:
    if i > 5:
        result = i + 2
        if result not in new:
            new.append(result)

print(org)
print(new)
