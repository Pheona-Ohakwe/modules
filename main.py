# Lesson 1: Assignments | Modules

#================================= 1. Python Modules and Data Handling Assignment====================================

# Task 1: Your Mood Today

import mood_responses

moods = input("How are you feeling today? Please choose either: excited, sad, grouchy, happy, angry, distraught, chill, confused." ).lower()
print(mood_responses.mood_response(moods))



#================================ 2. Mastering Python Modules and Aliases========================================================================

# Task 1: Custom Module with Aliases




import text_utils as cap
str = "This is my string"
print(cap.capitalize_string(str))
print(cap.reverse_string(str))





