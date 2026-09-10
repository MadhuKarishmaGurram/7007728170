# Q3: Bayes Rule Applied to Text

# P(c) is the prior probability of a class before seeing the document.
# P(d|c) is the probability of the document given that class.
# P(c|d) is the posterior probability of the class after seeing the document.

print("Q3: Bayes Rule Applied to Text")
print("P(c): prior probability of class c.")
print("P(d|c): probability of document d given class c.")
print("P(c|d): probability of class c given document d.")
print()
print("Bayes rule: P(c|d) = P(c) * P(d|c) / P(d)")
print()
print("P(d) can be ignored when comparing classes because the same document")
print("has the same P(d) for every candidate class. It therefore does not")
print("change which class has the largest posterior probability.")
