#Record Program -13
#Nested Tuples

# Example nested tuple (you can change it)
nested = ((10, 20, 30), (40, 50), (60, 70, 80, 90))

print("Nested Tuple:", nested)
means = []

for tup in nested:
    total = 0
    for num in tup:
        total = total + num
    mean = total / len(tup)
    means.append(mean)
    print("Mean of", tup, "=", mean)

# Mean of all means
sum_means = 0
for m in means:
    sum_means = sum_means + m
overall_mean = sum_means / len(means)

print("Mean of means =", overall_mean)