# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(text, word):
  punctuation = "!?.,:;/() _-"
  censored = ""
  for char in word:
    if char in punctuation:
      censored += char
    else:
      censored += "#"
  return text.replace(word, censored)

print("==================== Email One ====================")
print(censor_one(email_one, "learning algorithms"))


import re

def censor_two(text, censor_list):
  punctuation = "!?.,:;/() _-"
  for word in censor_list:
    censored = ""
    for char in word:
      if char in punctuation:
        censored += char
      else:
        censored += "#"
    regex = re.compile(r'\b%s\b' % word, re.IGNORECASE)
    text = re.sub(regex, censored, text)
    # been looking for a way to avoid replacing a string within a word (e.g. researcHERs => researc###s), came up with using regular expressions, works like a charm!
    # https://docs.python.org/3/library/re.html
    # https://stackoverflow.com/questions/3995034/do-regular-expressions-from-the-re-module-support-word-boundaries-b
    # https://stackoverflow.com/questions/17730788/search-and-replace-with-whole-word-only-option

  return text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "learning algorithms", "her", "herself"]

print("=================== Email Two ====================")
print(censor_two(email_two, proprietary_terms ))

import re

def censor_three(text, censor_list, negative_list):
  punctuation = "!?.,:;/() _-"

  for word in censor_list:
    censored_word = ""
    for char in word:
      if char in punctuation:
        censored_word += char
      else:
        censored_word += "#"
    regex = re.compile(r'\b%s\b' % word, re.IGNORECASE)
    text = re.sub(regex, censored_word, text)

  count = 0
  for word in negative_list:
    if word in text:
      count += 1
      if count >= 2:
        for word in negative_list:
          censored_word = ""
          for char in word:
            if char in punctuation:
              censored_word += char
            else:
              censored_word += "#"
          regex = re.compile(r'\b%s\b' % word, re.IGNORECASE)
          text = re.sub(regex, censored_word, text)
        break
  return text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "learning algorithms", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

print("==================== Email Three ====================")
print(censor_three(email_three, proprietary_terms, negative_words))

import re

def censor_four(text, censor_list):
  punctuation = "!?.,:;/() _-"

  for word in censor_list:
    censored_word = ""
    for char in word:
      if char in punctuation:
        censored_word += char
      else:
        censored_word += "#"
    regex = re.compile(r'\b%s\b' % word, re.IGNORECASE)
    text = re.sub(regex, censored_word, text)

  # now we separate each paragraph inside a list, and then we separate each word from each paragraph
  censored_paragraphs = []
  separate_paragraphs = text.split("\n")
  for paragraph in separate_paragraphs:
    separate_words = paragraph.split(" ")
    index_list = []
    for i in range(len(separate_words)):
      if ("#" in separate_words[i]):
        if (i == (len(separate_words) - 1)):
          index_list.append(i - 1)
        elif (i == 0):
          index_list.append(i + 1)
        else:
          index_list.append(i + 1)
          index_list.append(i - 1)

    for j in index_list:
      # separate_words[j] = "#"*len(separate_words[j])
      censored_word = ""
      for char in separate_words[j]:
        if char in punctuation:
          censored_word += char
        else:
          censored_word += "#"
      separate_words[j] = censored_word

    censored_paragraphs.append(" ".join(separate_words))
  
  censored_text = "\n".join(censored_paragraphs)
  
  return censored_text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "learning algorithms", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

censor_list = proprietary_terms + negative_words

print("==================== Email Four ====================")
print(censor_four(email_four, censor_list))