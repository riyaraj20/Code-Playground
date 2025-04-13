import time
import random  # This import is necessary to use random.choice()

# List of sentences to choose from
sentences = [
    "Python is an amazing programming language.",
    "Coding is a skill that gets better with practice.",
    "Random sentence for typing speed test.",
    "Accuracy is as important as speed in programming.",
    "Programming is like solving puzzles."
]

# Function to calculate Words Per Minute (WPM)
def calculate_wpm(time_taken, sentence_length):
    words = sentence_length / 5  # Approximate: 1 word = 5 characters
    wpm = (words / time_taken) * 60  # Calculate WPM (words per minute)
    return wpm

# Randomly select a sentence
sentence = random.choice(sentences)

# Exhibit the sentence for the user to type
print("Kindly type the following sentence:")
print(sentence)

# Start the timer
start_time = time.time()

# Get user input
user_input = input()

# Stop the timer
end_time = time.time()

# Calculate the time taken to type the sentence
time_taken = end_time - start_time

# Calculate typing speed in WPM
typing_speed = calculate_wpm(time_taken, len(user_input))

# Print the results
print(f"Duration: {time_taken:.2f} seconds")
print(f"Typing velocity: {typing_speed:.2f} WPM")