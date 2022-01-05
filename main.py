import time

"""
This program uses the Jaccard Index to determine the similarity between the inputed word and all of the words in the txt file
"""
# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words

def jaccard_index(text, all_words):
  # Making a list to store the Jaccard Index value for each of the words in the file
  jaccard_indexes = []
  list_text = list(text)
  # For loop to go through all of the words and comparing them with the imputed word
  for words in all_words:
    list_words = list(words)
    ###
    intersection = len(list(set(list_text).intersection(list_words)))
    union = (len(list_text) + len(list_words)) - intersection
    jaccard_index = float(intersection) / union
    ### Above code found at https://www.statology.org/jaccard-similarity-python/
    
    # Adding every Jaccard Index value to the list in the order of the words in the txt file
    jaccard_indexes.append(jaccard_index)
  display_similar(jaccard_indexes, all_words)

# Displays the most similar word based on the highest Jaccard Index value
def display_similar(jaccard_indexes, all_words):
  # Sorts the Jaccard Index value list putting the largest ones at the end of the list
  sorted_JIndex = sorted(jaccard_indexes)  
  last_index = len(jaccard_indexes)-1
  # Gets the corresponding index of the highest Jaccard Index value in the list with the list with all the words
  print("The most similar word to yours is: \n\"" + (all_words[jaccard_indexes.index(sorted_JIndex[last_index])]) + "\"")

def suggest(text, all_words):
  if text in all_words:
    print(text + ' is already a correct word.')
  else:
    jaccard_index(text, all_words)

def main():
    all_words = load_words()
    print('Enter an incorrect or correct word, or \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()

