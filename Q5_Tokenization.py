import re

# The paragraph is the Romanized Telugu paragraph used for the homework.
paragraph = (
    'Ninna saayantram memu park lo nadichaamu. '
    'Akka cheppindi, “Repati exam kosam baaga chaduvu!” '
    'Maa friends andaroo bus-stop daggara kalisaaru. '
    'Vaallu cricket aadutoo snacks tinnaru.'
)

# Q5.1: Naive tokenization simply splits on spaces.
naive = paragraph.split()
print("===== Q5.1 NAIVE SPACE TOKENIZATION =====")
print(naive)

# Manual correction: separate sentence punctuation and quotation marks.
# The hyphenated compound "bus-stop" is intentionally kept together.
manual_text = re.sub(r'([.,!?“”])', r' \1 ', paragraph)
manual_text = re.sub(r'\s+', ' ', manual_text).strip()
manual = manual_text.split()

print("\n===== Q5.1 MANUAL TOKENIZATION =====")
print(manual)

print("\n===== DIFFERENCES =====")
print("Naive tokenization attaches punctuation to words.")
print("Manual tokenization separates punctuation and keeps bus-stop as one compound.")

# Q5.2: Compare with NLTK.
try:
    from nltk.tokenize import word_tokenize
    nltk_tokens = word_tokenize(paragraph, preserve_line=True)
    print("\n===== Q5.2 NLTK TOKENIZATION =====")
    print(nltk_tokens)
    print("\nNLTK may differ from the manual list in quotation marks, punctuation,")
    print("and treatment of the hyphenated expression bus-stop.")
except ImportError:
    print("\nNLTK is not installed.")
    print("Install it with: python -m pip install nltk")
    print("Then run this program again.")

# Q5.3: Three example MWEs.
mwes = {
    "bus stop": "A common place-related expression referring to one concept.",
    "good morning": "A fixed greeting whose meaning is conventional as a phrase.",
    "exam preparation": "A common phrase describing preparation for an exam."
}
print("\n===== Q5.3 MULTIWORD EXPRESSIONS =====")
for expression, reason in mwes.items():
    print(f"{expression}: {reason}")

# Q5.4: Reflection required by the assignment.
reflection = """
The hardest part of tokenization in Romanized Telugu is deciding consistent
word boundaries when punctuation and compounds are present. Naive space-based
tokenization is simple, but it leaves punctuation attached to neighboring words.
English has similar punctuation problems, while Romanized Telugu can also have
spelling variation because Telugu is represented with Latin characters. Morphology
and multiword expressions can make tokenization harder than simple whitespace
splitting. Overall, a useful tokenizer should consider punctuation, word formation,
and phrase-level meaning rather than spaces alone.
"""
print("\n===== Q5.4 REFLECTION =====")
print(reflection.strip())
