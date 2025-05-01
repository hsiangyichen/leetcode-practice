# Question: Given a paragraph and a list of banned words, return the most common word that is not in the banned list. 
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"

# def mostCommonWord(self, paragraph, banned):
    # input: 1 string, 1 list; output: string
    
    # Method 1: O(n^2)
    # build a list for it
    # remove the value that is in banned
    # check if count > max_count
    # if yes, replace new word
    # words = re.findall(r'\w+', paragraph.lower())
    
    # filtered_words = []
    # for word in words:
    #     if word and word not in banned:
    #         filtered_words.append(word)
    
    # max_count = 0
    # result_word = ""

    # for i in range(len(filtered_words)):
    #     count = 0
    #     for j in range(i, len(filtered_words)):
    #         if filtered_words[i] == filtered_words[j]:
    #             count += 1
    #     if count > max_count:
    #         max_count = count
    #         result_word = filtered_words[i]

    # return result_word

    # Method 2: O(n)
    # build a list for it
    # make it a dict
    # remove the one that is in banned
    # return the key that has the max value
    # words = re.findall(r'\w+', paragraph.lower())
    
    # filtered_words = []
    # for word in words:
    #     if word and word not in banned:
    #         filtered_words.append(word)
    
    # words_dict = defaultdict(int)

    # for word in filtered_words:
    #     words_dict[word] += 1

    # max_count = 0
    # result_word = ""

    # for word, count in words_dict.items():
    #     if count > max_count:
    #         result_word = word
    #         max_count = count
    # return result_word