import datetime
from collections import namedtuple

# Define a flashcard structure
Flashcard = namedtuple("Flashcard", ["question", "answer", "next_review", "interval"])

def schedule_next_review(card, quality):
    """
    Update the card's review schedule based on the user's response quality.
    Quality can be 0 (don't remember) to 5 (remembered well).
    """
    if quality < 3:
        new_interval = 1
    else:
        new_interval = card.interval * 2

    next_review = datetime.datetime.now() + datetime.timedelta(days=new_interval)
    return card._replace(next_review=next_review, interval=new_interval)

def review_flashcards(cards):
    """
    Simulate a review session. User inputs their response quality.
    """
    for card in cards:
        print(f"Question: {card.question}")
        input("Press enter to show the answer...")
        print(f"Answer: {card.answer}")

        quality = int(input("How well did you remember? (0-5): "))
        updated_card = schedule_next_review(card, quality)
        yield updated_card

# Example flashcards
flashcards = [
    Flashcard(question="What is the capital of France?", answer="Paris", next_review=datetime.datetime.now(), interval=1),
    Flashcard(question="What is 2 + 2?", answer="4", next_review=datetime.datetime.now(), interval=1)
]

# Start a review session
updated_cards = list(review_flashcards(flashcards))

# You can then save 'updated_cards' to a file or database for future reviews
