# CS5760 NLP - Homework 1
# Q1: Regular Expressions
import re

# Q1(a): U.S. ZIP codes
zip_pattern = r'\b\d{5}(?:[- ]\d{4})?\b'

text = "ZIP codes: 64050, 64050-1234, and 64050 5678."

matches = re.findall(zip_pattern, text)

print("Q1(a) ZIP codes:", matches)

# Q1(b): Words that do not start with a capital letter
word_pattern = r"\b(?![A-Z])[A-Za-z]+(?:['-][A-Za-z]+)*\b"

text = "hello World don't state-of-the-art NLP student"

matches = re.findall(word_pattern, text)

print("Q1(b) lowercase-starting words:", matches)

# Q1(c): Numbers
number_pattern = r"[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?"

text = "Numbers: 42, -17, +3.14, 1,234.56, and 1.23e-4."

matches = re.findall(number_pattern, text)

print("Q1(c) numbers:", matches)


# Q1(d): Email / e-mail / e mail
email_pattern = r"\be(?:-| )?mail\b"

text = "Contact me by email, e-mail, or e mail."

matches = re.findall(email_pattern, text, re.IGNORECASE)

print("Q1(d) email variants:", matches)

# Q1(e): go, goo, gooo, etc.
go_pattern = r"\bgo+\b[!.,?]?"

text = "Responses: go, goo, gooo!, goooo? and stop."

matches = re.findall(go_pattern, text)

print("Q1(e) go variants:", matches)

# Q1(f): Lines ending in a question mark
question_pattern = r"^.*\?\s*[\"'\)\]\}]*\s*$"

text = """How are you?
Where do you live? 
Is this your homework?"
This is not a question.
Are you ready?"""

matches = re.findall(question_pattern, text, re.MULTILINE)

print("Q1(f) question-ending lines:", matches)