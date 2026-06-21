# Question 9:
# Take a character from the user and check whether it is a Vowel or Consonant

# Taking character input
ch = input("ENTER ANY CHARACTER = ")

# Converting character to lowercase
ch = ch.lower()

# Checking vowel or consonant
if ch in ('a', 'e', 'i', 'o', 'u'):
    print("VOWEL")
else:
    print("CONSONANT")