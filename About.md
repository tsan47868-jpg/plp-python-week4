## Week 4 Assignment: Hands-On Lab — Grades, Eligibility & Smart Decisions
##  DescriptionAssignment: Grades, Eligibility & Smart Decisions

Duration: About 90 minutes

This week your programs learn real judgement. You will build three decision-making programs that use everything from a simple if to nested conditionals.

This assignment will help you practice:

Multi-way decisions with if / elif / else
Combining conditions with and, or, and not
Validating user input before using it
Nesting one decision inside another

Files to create (use these exact names):

grade_classifier.py
eligibility_checker.py
atm_menu.py

GitHub repository name to use (public, exact): plp-python-week4

All weekly assignments follow the same repository naming pattern — plp-python-week3, plp-python-week4, and so on. Your submission for this assignment is one link: your public GitHub repository containing all the files above. Use these exact file and repository names so your submission matches the marking checklist.


Part A — Grade Classifier

Create the file grade_classifier.py.

Ask the user for a score between 0 and 100 and convert it with int().
First, validate: if the score is below 0 or above 100, print an error

message and do not grade it.

Otherwise use if / elif / else to decide the grade:

A (80+), B (70–79), C (60–69), D (50–59), otherwise F.

Print the grade clearly, e.g. "A score of 84 earns grade: A".

Required results:

A working grade_classifier.py with validation and all five grades reachable.
A screenshot of at least three runs: one valid score, one invalid score (e.g. 140), one boundary score (e.g. exactly 70).
Part B — Eligibility Checker

Create the file eligibility_checker.py. A local coding club is recruiting members. The rules:

Members must be 13 or older and have parental consent if under 18.
Anyone 18 or older does not need consent.
Ask for the person's age.
If they are under 18, also ask "Do you have parental consent? (yes/no)".
Use and / or / not in your conditions to decide and print one of:

"Welcome to the club!" or "Sorry, you are not eligible yet."

Add a comment above each condition explaining it in plain English.

Required results:

A working eligibility_checker.py using at least two of and / or / not.
A screenshot of three runs: an adult, a 15-year-old with consent, a 15-year-old without consent.
Part C — ATM Menu (Nested Decisions)

Create the file atm_menu.py. Start with a balance in your code, e.g. balance = 1000.

Ask the user for a 4-digit pin. The correct PIN is one you choose in your code.
If the PIN is wrong, print "Incorrect PIN" and stop.
If the PIN is correct, ask how much they want to withdraw.
Inside that decision: if the amount is less than or equal to the balance,

print the new balance; otherwise print "Insufficient funds".

Required results:

A working atm_menu.py with one decision nested inside another.
A screenshot of three runs: wrong PIN, successful withdrawal, withdrawal larger than the balance.
Submission Requirements

Your submission is one link to a public GitHub repository.

Create a public GitHub repository named exactly: plp-python-week4
Add all your work. The repository must contain:
grade_classifier.py
eligibility_checker.py
atm_menu.py
screenshots/ — a folder with your screenshots of each program running
README.md — the assignment title, one line describing each file, and 2–3

sentences: when is elif better than several separate if statements?

Submit the repository link on the LMS:

https://github.com/<your-username>/plp-python-week4

Before you submit: open your link in a private/incognito browser window — if you can see the files without logging in, the repo is public and your instructor can mark it.