import re
import traceback

# interpreter is python 3.9. Developed on a M1 Mac OS 11.4 Big Sur
# to run application go to root directory in terminal/console in the directory


# validates if user entered a number or not
def user_input():
    number = input("Enter the number of words to count:  ")
    if number.isdigit():
        return number
    else:
        print("Error only enter integers, Try again: ")
        user_input()


if __name__ == '__main__':
    try:
        # get user input on number of words to process and count
        number_of_words = user_input()

        # load file
        common_words_file = open('1-1000.txt', 'r')

        # iterate through and add to dictionary
        common_words_lines = common_words_file.readlines()

        # common words to exclude
        words_to_be_excluded = {}
        for line in common_words_lines:
            # add to dictionary
            # strip new line characters and make lowercase
            words_to_be_excluded[line.strip().lower()] = ""

        # dictionary that will store the words that we will scan
        words_to_be_counted = {}

        for line in open("alice_in_wonderland.txt", 'r').readlines():
            for word in line.split():
                # strip punctuation and make lower case to count easier
                clean_word = re.sub(r'[^\w\s]', '', word).lower()

                # if empty or in common words skip
                if clean_word in words_to_be_excluded or clean_word.strip() == '':
                    continue

                # if word is already added to dict just increment the counter
                elif clean_word in words_to_be_counted:
                    words_to_be_counted[clean_word] += 1

                # if not a common word and not added dict add to dict
                else:
                    words_to_be_counted[clean_word] = 1

        # sort descending to get the top first
        sorted_words = sorted(words_to_be_counted.items(), key=lambda kv: kv[1], reverse=True)

        # start output
        print("Count  Word")
        print("===    ====")

        # create counter
        counter = 0
        # iterate through sorted words and format output
        for k, v in sorted_words:
            if counter < int(number_of_words):
                counter += 1
                print("{:<6} {:<15}".format(v, k))

    # exception block
    except Exception as exception:
        print(exception.__class__.__name__)
        print(exception)
        print(__file__ +  " : Line " + str(exception.__traceback__.tb_lineno))





