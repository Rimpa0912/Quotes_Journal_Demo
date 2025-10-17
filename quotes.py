import random

quotes = {
    "Motivation": [
        "The secret of getting ahead is getting started.",
        "The elevator to success is out of order. You'll have to use the stairs, one step at a time",
        "It is never too late to be what you might have been.",
        "Setting goals is the first step in turning the invisible into the visible"
    ],
    "Coding": [
        "Code is like humor. When you have to explain it, it's bad.",
        "Programming isn't about what you know; it's about what you can figure out.",
        "In the beginner's mind, there are many possibilities; in the expert’s mind, there are few.",
        "First, solve the problem. Then, write the code."
    ],
    "Life": [
        "In the middle of difficulty lies opportunity.",
        "If you cannot do great things, do small things in a great way",
        "You are not stuck where you are unless you decide to be.",
        "Strive not to be a success, but rather to be of value."
    ]
}

print("Categories:", ", ".join(quotes.keys()))
selected = input("Choose a category: ").capitalize()
if selected in quotes:
    quote = random.choice(quotes[selected])
else:
    all_quotes = sum(quotes.values(), [])
    quote = random.choice(all_quotes)

print("Random Quote:", quote)

with open("history.txt", "a") as file:
    file.write(quote + "\n")

