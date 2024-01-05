import nltk
from nltk.corpus import stopwords
import re
from blogextract import content
from words import negative_words , positive_words


def findnegative(word):
    # store all the contents of the text file
    text_file_contents = negative_words
    # Split the text file contents into a list of words
    text_file_words = text_file_contents.split("\n")

    # Check if the word is in the list of words
    is_present = word in text_file_words

    # Print the result
    return (is_present)


def findpositive(word):
    # store all the contents of the text file
    text_file_contents = positive_words
    # Split the text file contents into a list of
    text_file_words = text_file_contents.split("\n")

    # Check if the word is in the list of words
    is_present = word in text_file_words

    # Print the result
    return (is_present)


# count variable for positive and negative count
pc = 0
nc = 0
# take the whole content of the txt file and store it in the string
original_string = content
# split the string into list it makes it easier for comparisions
modified_string = original_string.split()
for i in modified_string:
    if findpositive(i):
        pc = pc + 1
    if findnegative(i):
        nc = nc + 1

print("Positivity Score= ", pc, "\nNegativity Score= ", nc)

# find polarity score
sum_var = pc + nc
diff_var = pc - nc
pscore = diff_var / (sum_var + 0.00001)
print("Polarity Score=", pscore)


# function to find total clean words
def cleanwords(text):
    # Remove punctuation
    punctuation = set(r',.?!;()[]{}\"\'')  # Create a set of punctuation characters
    clean_words = []
    for word in text.split():
        if word not in punctuation:
            clean_words.append(word)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    clean_words_no_stopwords = [word for word in clean_words if word not in stop_words]

    # Count the total clean words
    total_clean_words = len(clean_words_no_stopwords)

    return total_clean_words


# variable to store the number of clean words
store_clean_words = cleanwords(original_string)

#subjectivity score
subscore= sum_var / (store_clean_words + 0.00001)
print("Subjectivity Score= ", subscore )



def count_sentences(paragraph):
  # Split the paragraph into sentences using regular expressions
  sentences = re.split(r'[.?!;]+', paragraph)

  # Count the number of sentences
  sentence_count = len(sentences)

  return sentence_count


sentence_avg_range = store_clean_words/count_sentences(original_string)
print("Average sentence range =", sentence_avg_range)

#now we will calculate percetage of complex words
def count_syllables(word):
    vowels = "aeiouy"
    num_vowels = 0
    last_was_vowel = False
    for wc in word:
        found_vowel = False
        for v in vowels:
            if v == wc:
                if not last_was_vowel:
                    num_vowels += 1
                    found_vowel = True
                last_was_vowel = True
                break
        if not found_vowel:
            last_was_vowel = False
    return num_vowels

complex_total = 0
for i in modified_string:
    if count_syllables(i)>2:
        complex_total=complex_total+1

#now finally we can print total number of complex words percentage
per_complex_words = (complex_total/store_clean_words)*100
print("Percentage of Complex words=",per_complex_words, "%")

#print the fog index
fog_index= 0.4* (sentence_avg_range+per_complex_words)
print("Fog Index = ", fog_index)

#avg words per sentence
print("Avg no. words per sentence=", sentence_avg_range)

#to print total words count
print("Total Complex Words= ",complex_total)

#syllables per word with exception
def count_syllables_new(word):
    vowels = "aeiouy"
    num_vowels = 0
    last_was_vowel = False
    for wc in word:
        found_vowel = False
        for v in vowels:
            if v == wc:
                if not last_was_vowel:
                    num_vowels += 1
                    found_vowel = True
                last_was_vowel = True
                break
        if not found_vowel:
            last_was_vowel = False
    if word.endswith("es") or word.endswith("ed"):
        num_vowels -= 1
    return num_vowels

#count the syllables
syl_per_word=0
for i in modified_string:
    if count_syllables_new(i)>2:
        syl_per_word=syl_per_word+1

print("Syllables per word=", syl_per_word)

#number of personal pronoun

def count_personal_pronouns(paragraph):
    # Define personal pronouns to match
    personal_pronouns_pattern = r"\b(I|we|my|ours|us|(?-i:us)\b)"

    # Split the paragraph into words
    words = paragraph.split()

    # Count the number of personal pronouns (excluding "US")
    pronoun_count = 0
    for word in words:
        if word != "US" and re.search(personal_pronouns_pattern, word):
            pronoun_count += 1

    return pronoun_count

print ("Number of personal pronouns=", count_personal_pronouns(original_string))

#fun to find avg word lenght
total_words_character = cleanwords(original_string)
total_words = len(modified_string)
print("Average word length= ",(total_words_character/total_words))












