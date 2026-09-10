# Q4: Add-1 Smoothing

negative_total = 14
vocabulary_size = 20
predictable_count = 2
fun_count = 0

# Add-1 smoothing changes the denominator from N to N + V.
denominator = negative_total + vocabulary_size

predictable = (predictable_count + 1) / denominator
fun = (fun_count + 1) / denominator

print("Q4: Add-1 Smoothing")
print(f"Denominator = {negative_total} + {vocabulary_size} = {denominator}")
print(f"P(predictable | -) = 3/34 = {predictable:.4f}")
print(f"P(fun | -) = 1/34 = {fun:.4f}")
