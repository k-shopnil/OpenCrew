import os
from gtts import gTTS


def numcallmachine(number):
    numbers_dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "five", "5": "five", "6": "six",
                    "7": "seven", "8": "eight", "9": "nine"}
    your_number = str(number)
    numbers_in_words = ""
    numbers_in_words_speech = ""
    while True:
        for i in your_number:
            if i in numbers_dict:
                numbers_in_words += " " + numbers_dict.get(i)
                numbers_in_words_speech += numbers_dict.get(i)
            else:
                break
        return numbers_in_words


def numcallmachine2(number):
    numbers_dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "five", "5": "five", "6": "six",
                    "7": "seven", "8": "eight", "9": "nine"}
    your_number = str(number)
    numbers_in_words = ""
    numbers_in_words_speech = ""
    while True:
        for i in your_number:
            if i in numbers_dict:
                numbers_in_words += " " + numbers_dict.get(i)
                numbers_in_words_speech += numbers_dict.get(i)
            else:
                break
        return numbers_in_words_speech
