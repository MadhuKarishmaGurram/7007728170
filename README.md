# 7007728170
Homework-1
# CS5760 Natural Language Processing - Homework 1

**University:** University of Central Missouri  
**Course:** CS5760 Natural Language Processing  
**Semester:** Fall 2026  
**Student Name:** Madhu Karishma Gurram 
**Student ID:** 7007728170

## Contents

This repository contains the source code for Homework 1.

- `Q1_Regex.py` - six regular-expression tasks.
- `Q2_BPE.py` - coding portions 2.2 and 2.3 for Byte Pair Encoding.
- `Q3_Bayes.py` - Bayes Rule explanations.
- `Q4_Smoothing.py` - add-1 smoothing calculations.
- `Q5_Tokenization.py` - naive/manual tokenization, NLTK comparison, MWEs, and reflection.

## Q2 Manual Work

The first three BPE merges for Question 2.1 are completed in the written
homework because the assignment specifically asks for those calculations by hand.

The program implements the coding portions of Q2.2 and Q2.3. It adds the `_`
end-of-word marker, counts adjacent pairs, merges the most frequent pair, prints
the top pair and vocabulary size, and produces word segmentations.

## Q3

The program explains `P(c)`, `P(d|c)`, and `P(c|d)` and explains why `P(d)` can
be ignored when comparing candidate classes for the same document.

## Q4

Given a negative-class token count of 14 and vocabulary size 20:

- Denominator = `14 + 20 = 34`
- `P(predictable | -) = (2 + 1) / 34 = 3/34 ≈ 0.0882`
- `P(fun | -) = (0 + 1) / 34 = 1/34 ≈ 0.0294`

## Q5

The program shows naive space-based tokenization, manually corrected
tokenization, an NLTK comparison, three multiword expressions, and a reflection.

## Running the code

Run each file from Command Prompt/Terminal:

```text
python Q1_Regex.py
python Q2_BPE.py
python Q3_Bayes.py
python Q4_Smoothing.py
python Q5_Tokenization.py
```

If NLTK is not installed:

```text
python -m pip install nltk
```

