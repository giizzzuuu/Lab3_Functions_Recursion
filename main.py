# main.py

from curses import wrapper
from itertools import count
from unittest import result

import Lab3_Functions_Evangelista.grades as grades
# Student Identity Configuration
LAST_NAME = "Evangelista"
STUDENT_ID = "TUPM-25-0295"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(digit) for digit in STUDENT_ID if digit.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_mark(grade)

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average,2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)

import access_control as ac
import media_engine as me

# --- Global Variables ---
CONTROL_NUM = "5"
FAVORITE_ARTIST = "Drake"
ARTIST_LEN = len(FAVORITE_ARTIST)

# --- Exercise 2: Recursive Signal Shutdown ---
def signal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@signal_decorator
def signal_shutdown(power, count=0):
    if power <= 0:
        return count
    print(f"Current signal strength: {power}")
    return signal_shutdown(power - 1, count + 1)

def run_exercises():
    print("--- Exercise 1: Secure Access System ---")
    access_lvl = ac.compute_access_level(CONTROL_NUM)
    decision = ac.validate_access(access_lvl)
    print(f"Access Level: {access_lvl}")
    print(f"Decision: {decision}\n")

print("--- Exercise 2: Recursive Signal Shutdown ---")
# Initial power: CONTROL_NUM + len(FAVORITE_ARTIST) = 9 + 6 = 15
initial_power = CONTROL_NUM + ARTIST_LEN
total_calls = signal_shutdown(initial_power)
print(f"Total recursive calls: {total_calls}\n")
print("--- Exercise 3: Streaming Analytics ---")
# Limit: CONTROL_NUM + len(FAVORITE_ARTIST) = 15
limit = CONTROL_NUM + ARTIST_LEN
total_plays, num_records, generated_list = me.run_analytics(limit)
print(f"Generated Counts: {generated_list}")
print(f"Total Plays: {total_plays}")
print(f"Records Processed: {num_records}")
