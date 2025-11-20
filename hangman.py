import numpy as np

array_of_7_letter_words = np.array([
  "through",
  "picture",
  "country",
  "believe",
  "without",
  "teacher",
  "morning",
  "cabinet",
  "machine",
  "freedom"
])

upper_exclusive_bound_of_length_of_array_of_7_letter_words = len(array_of_7_letter_words)
# print(f"{upper_exclusive_bound_of_length_of_array_of_7_letter_words=}")

random_number_generator = np.random.default_rng()

index_of_random_7_letter_word = random_number_generator.integers(0,upper_exclusive_bound_of_length_of_array_of_7_letter_words)
# print(f"{index_of_random_7_letter_word=}")

random_7_letter_word = array_of_7_letter_words[index_of_random_7_letter_word]
# print(f"{random_7_letter_word=}")
random_7_letter_word_as_an_array_of_characters = np.array(list(random_7_letter_word))
# print(f"{random_7_letter_word_as_an_array_of_characters=}")

user_has_guessed_the_word = False
guesses_left = 6
word_showing_only_guessed_letters_as_an_array = np.array(["_","_","_","_","_","_","_",])
# print(f"{word_showing_only_guessed_letters_as_an_array=}")

letters_still_available = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

# while the under the guess_limit and the user has not guessed the word
while guesses_left > 0 and user_has_guessed_the_word == False:

    print(f"{guesses_left=}")
    print(f"{letters_still_available=}")

    word_showing_only_guessed_letters_as_a_string = ''.join(word_showing_only_guessed_letters_as_an_array)
    print(f"{word_showing_only_guessed_letters_as_a_string=}")

    users_guess_for_the_word = input("What is your guess? ")
    # print(f"{users_guess_for_the_word=}")
    users_guess_for_the_word_as_an_array = np.array(list(users_guess_for_the_word))

    user_has_guessed_the_word = True if users_guess_for_the_word == random_7_letter_word or word_showing_only_guessed_letters_as_a_string == random_7_letter_word else False

    if user_has_guessed_the_word == False:

        for index_of_guessed_letter, guessed_letter in enumerate(users_guess_for_the_word_as_an_array):
            # print(f"{guessed_letter=}")

            if guessed_letter in letters_still_available:
                # print("Letter was still available")
                index_of_letter_to_guess_in_letters_still_available = np.where(letters_still_available == guessed_letter)
                # print(f"{index_of_letter_to_guess_in_letters_still_available=}")
                letters_still_available[index_of_letter_to_guess_in_letters_still_available] = "_"

            if guessed_letter in random_7_letter_word_as_an_array_of_characters:
                indices_of_matching_letters_in_word_to_guess = np.where(random_7_letter_word_as_an_array_of_characters == guessed_letter)
                # print(f"{indices_of_matching_letters_in_word_to_guess=}")

                word_showing_only_guessed_letters_as_an_array[indices_of_matching_letters_in_word_to_guess] = guessed_letter



        
        # for index_of_letter_to_guess, letter_to_guess in enumerate(random_7_letter_word):
        #     print(f"{index_of_letter_to_guess=}, {letter_to_guess=}")

        #     guessed_letter = users_guess_for_the_word_as_an_array[index_of_letter_to_guess]
        #     print(f"{guessed_letter=}")

        #     if letter_to_guess == guessed_letter:
        #         word_showing_only_guessed_letters_as_an_array[index_of_letter_to_guess] = guessed_letter

        #     if guessed_letter in letters_still_available:
        #         print("Letter was still available")
        #         index_of_letter_to_guess_in_letters_still_available = letters_still_available.index(guessed_letter)
        #         print(f"{index_of_letter_to_guess_in_letters_still_available=}")

        #         letters_still_available[index_of_letter_to_guess_in_letters_still_available] = "_"


    guesses_left = guesses_left - 1

user_wins = True if user_has_guessed_the_word else False

if user_wins:
    print("You got it!")
else:
    print("it's over")


