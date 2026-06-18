from jamdict import Jamdict
import random
import re
import pyttsx3
import time

jmd = Jamdict()

engine = pyttsx3.init()

def wholeprogwork():
    # changes to Microsoft Zira for closing or restarting the program and narrating the necessary inputs upon startup
    voice = engine.getProperty('voices')[1]
    engine.setProperty('voice' , voice.id)
    engine.setProperty('rate', 180)
    
    engine.say("What would you like to set the time limit for each word as? (Number of seconds only) ")
    engine.runAndWait()
    enter_time_limit = int(input("What would you like to set the time limit for each word as? (Number of seconds only) "))
    engine.say("How many words would you like to try? ")
    engine.runAndWait()
    enter_word_limit = int(input("How many words would you like to try? "))
    engine.say("Would you like to display and read the meanings? (y or n?) ")
    engine.runAndWait()
    meaning_dec = input("Would you like to display and read the meanings? (y/n) ")

    i = 0
    while i < enter_word_limit:

        # add randomizer here (randomly selects a six digit number, then multiplies it with ten)
        random_integer_id = random.randrange(100000, 300000) * 10

        """if the number doesn't match, try and accept blocks will be used for error handling, 
        and another number will be generated, this continues till a number matches"""
        try:
            random_integer_id = str(random_integer_id)

            # add dictionary with numbers here
            result = jmd.lookup('id#' + random_integer_id)
            result_of_search = result.entries[0]
            usable_result_jp = str(result_of_search)
            usable_result = str(result_of_search)

            '''separate parts of text before kanji in brackets and exclude the ID number
            from entry (can be done with regex)'''
            usable_result_jp = re.findall(r"[^(?:\[id#\d{7}\]\(\n]+", usable_result_jp)[0]
            print (usable_result_jp)

            # Reading the Japanese with TTS. Microsoft Haruka for now, change to MS Ichiro when WinRT is avaialble for Py3.8+
            engine.setProperty('rate' , 120)
            voice = engine.getProperty('voices')[2]
            engine.setProperty('voice' , voice.id)
            engine.say(usable_result_jp)
            engine.runAndWait()

            if meaning_dec == "y":

                ''' separate meaning (english letters from A to Z, case insensitive)
                from entry (can be done with regex)'''
                usable_result = re.findall(r'[a-zA-Z]+', usable_result)
                usable_result = usable_result[1:]
                usable_result = " ".join(usable_result)

                # Microsoft David's voice for english meanings
                print (usable_result)
                voice = engine.getProperty('voices')[0]
                engine.setProperty('voice' , voice.id)
                engine.say(usable_result)
                engine.runAndWait()

            i += 1

            # use time module for a countdown starting from input, to zero
            while enter_time_limit > 0:
                time_accurator = time.gmtime()
                time.sleep(1)
                enter_time_limit-=1

        except:
            print("Processing... \n ID number not found in Database! \n Retrying...")


wholeprogwork()

end = "yes"
while True:
    voice = engine.getProperty('voices')[1]
    engine.setProperty('voice' , voice.id)
    engine.setProperty('rate', 180)
    engine.say("Press 'Enter' to stop. Enter any key to restart. ")
    engine.runAndWait()
    end = input("Press 'Enter' to stop. Enter any key to restart. ")
    if end == "":
        break
    else:
        wholeprogwork()



# [id#1358280] たべる (食べる) : 1. to eat ((Ichidan verb|transitive verb)) 2. to live on (e.g. a salary)/to live off/to subsist on
# [id#1358300] たべすぎる (食べ過ぎる) : to overeat ((Ichidan verb|transitive verb))
# [id#1852290] たべつける (食べ付ける) : to be used to eating ((Ichidan verb|transitive verb))
# [id#2145280] たべはじめる (食べ始める) : to start eating ((Ichidan verb))
# [id#2449430] たべかける (食べ掛ける) : to start eating ((Ichidan verb))
# [id#2671010] たべなれる (食べ慣れる) : to be used to eating/to become used to eating/to be accustomed to eating/to acquire a taste for ((Ichidan verb))
# [id#2765050] たべられる (食べられる) : 1. to be able to eat ((Ichidan verb|intransitive verb)) 2. to be edible/to be good to eat ((pre-noun adjectival (rentaishi)))
# [id#2795790] たべくらべる (食べ比べる) : to taste and compare several dishes (or foods) of the same type ((Ichidan verb|transitive verb))
# [id#2807470] たべあわせる (食べ合わせる) : to eat together (various foods) ((Ichidan verb))