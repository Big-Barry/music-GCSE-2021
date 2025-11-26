import random
import time
import stdiomask as mask
from tinydb import TinyDB, Query, where

score_db = TinyDB('scorers.json')
login = TinyDB('logins.json')
song = TinyDB('songs.json')

score = 0
tries = 0
chances = 2

login_check = 'False'

print("Welcome the music game quiz")
while login_check == "False":
    login_username = input("Enter login username: ")
    login_password = mask.getpass(mask='*', prompt='Enter login password: ')

    login_arr = login.get(where('username') == login_username)#Gets the login data of the specific username inputed else if its not found it tells the user that the username was not found
    if login_arr == None:
        print("username not found, try again\n")
        continue

    login_user_formated = f"{login_arr['username']}"
    login_pass_formated = f"{login_arr['password']}"
    if login_username == login_user_formated and login_password == login_pass_formated:#Checks if login username and password match else it tells the user that the password was wrong, however if they match it goes to the main menu
        login_check = 'True'
        print("Login successful\n\n\n")
        pass
    if login_check != 'True':
        print("Password is incorrect, try again\n")
        continue

login_check2 = 'False'
while login_check2 == 'False':
    try:
        login_choice = int(input('Game menu:\nEnter 1 to play game.\nEnter 2 to see top 5 scorers leaderboard\nEnter value: '))
    except ValueError:
        print("Invalid value\n")
        continue
    if login_choice != 1 and login_choice != 2:
        print("Invalid Integer, try again\n")
        continue
    login_check2 = 'True'
    pass

if login_choice == 1:
    song_main_check = 'False'
    songs_arr = song.all()

    while song_main_check == 'False':
        if song_main_check == 'True':
            break
        tries = 0
        song_random_int = (random.randint(0, len(songs_arr))) - 1
        song_random_song_dict = (songs_arr[song_random_int])
        song_name_formated = f"{song_random_song_dict['name']}"
        song_artist_formated = f"{song_random_song_dict['artist']}"
        song_answer_arr = [song_name_formated.lower(), song_artist_formated.lower()]#Gets all songs from json file and randomly picks one after user has guessed correctly it is then removed from the list so that it wouldn't be randomly picked again

        song_name_firstletter = song_name_formated.split()
        song_name_letters2 = ""
        for word in song_name_firstletter:
            song_name_letters2 = song_name_letters2 + word[0]
        song_name_firstletters = (" ".join(song_name_letters2).upper())#Formats an checks if the answer was formated properly

        song_answer_check = 'False'
        while song_answer_check == 'False':
            print(f"\n\nFirst letter(s) of the song name is {song_name_firstletters}\nThe song artist is {song_artist_formated}\n\n")
            song_answer = str(input(f"Enter song name the artist has been given\n\nChances/Lives: {chances}\nCurrent score: {score}\n\nEnter Answer: ").lower())
            if song_answer == song_name_formated.lower():
                print(f"correct answer, answer was {song_name_formated} by {song_artist_formated}\nNext song\n\n\n")
                time.sleep(2)
                if tries == 0:
                    score = score + 3
                if tries > 0:
                    score = score + 1
                del songs_arr[song_random_int]
                break

            if song_answer != song_artist_formated.lower():
                tries = tries + 1
                chances = chances -1
                if chances == 0:
                    print(f"Game over\nFinal score: {score}")#The code to the functionality of the game/game logic
                    song_main_check = 'True'
                    song_answer_check = 'True'
                    time.sleep(3)
                    song_final_score_name = str(input("\n\nEnter First name to be saved to the leaderboard\n\nEnter name: "))
                    score_db.insert({'name' : song_final_score_name, 'score' : score})#After the player loses they are prompted to enter their name to be saved to the scorers database json file.
                    continue

                if chances != 2:
                    print("Wrong answer, try again\n\n")
                    time.sleep(3)
                    continue

if login_choice == 2:
    score_all_arr = score_db.all()#Gets the contents of the json file 
    score_loop_value = 0
    score_all_arr_formated = {}

    for i in score_all_arr:
        score_all_temp_name = f"{i['name']}"
        score_all_temp_score = f"{i['score']}"
        score_all_arr_formated[score_all_temp_name] = int(score_all_temp_score)#Formats the contents of the json file

    score_all_arr_sorted = sorted(score_all_arr_formated.items(), key=lambda x: x[1], reverse=True)#Sorts the items inside the dict from biggest to smallest
    
    score_count = 1
    print("The top 5 scorers are as follows:\n\n")
    for j in score_all_arr_sorted:
        print(f"Player name {j[0]} at position number {score_count} has a score of {j[1]}")#Formats the top 5 winners
        score_count = score_count + 1
        if score_count == 6:
            break

print("\nRe-run code to play again :)")