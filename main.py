import pandas
import numpy
from pprint import pprint
from functions import find_anime_watch_status, find_season_show

with open("animelist_csv.csv") as data_file:
    ani_data = pandas.read_csv(data_file)
    ani_data_frame = pandas.DataFrame(ani_data)
    # print(ani_data_frame)

# changes name of the columns
ani_data_frame = ani_data_frame.set_axis(['ID', 'Title', 'Type', 'Episodes', 'Watched Episodes',
                          'Start Date', 'End Date', 'My Rating', 'Watch Status',
                          'Times Completed', 'Watch Priority', 'Tags'],
                         axis='columns') 

# changes the dates with no date to 'N/A'
for i in range(len(ani_data_frame)):
    if ani_data_frame['Start Date'][i] == "0000-00-00": 
        ani_data_frame['Start Date'][i] = 'N/A'
    if ani_data_frame['End Date'][i] == "0000-00-00":
        ani_data_frame['End Date'][i] = 'N/A'

# finds all anime in the csv
print(ani_data_frame['Title'])
# advanced strings 7.1
anime_list = str(ani_data_frame['Title']).replace("  ", "").split('\n')
# gets rid of last uncessary element
anime_list.pop()
print(anime_list)


# finds percentage of amount of watching shows watched.
find_watching_episodes = []
find_total_episodes = []
find_episode_title = []
for entry in range(len(ani_data_frame)):
    if ani_data_frame['Watch Status'][entry] == "Watching":
        find_watching_episodes.append(int(ani_data_frame['Watched Episodes'][entry]))
        find_total_episodes.append(int(ani_data_frame['Episodes'][entry]))
        find_episode_title.append(ani_data_frame['Title'][entry])
# numpy 8.1   
result_vector = (numpy.array(find_watching_episodes) / numpy.array(find_total_episodes))*100
# print(result_vector)
for i in range(len(find_episode_title)):
    print(f"You've watched: {round(float(result_vector[i]), 2)}% of {find_episode_title[i]}")

# prints shows bassed on the 3 watch status
sort = input("What do you want so sort by? (Completed, Plan to Watch, Dropped): ")
if find_anime_watch_status(ani_data_frame, sort) == -1:
    print("Unknown Status")
else: 
    find_anime_watch_status(ani_data_frame, sort)

# finds seasons of a Boku no Hero Academia
# 7.4/7.5
boku_title = """"""
all_seasons = r"Boku no Hero Academia +\w+\w +\w+\w"
for i in range(len(ani_data_frame)):
    boku_title += ani_data_frame['Title'][i] + "\n"
print(find_season_show(all_seasons, boku_title))

# create new temporary csv
add = True
# 5.15
add_anime = {}
while add:
    title = input("Title of Anime: ").title()
    ani_type = input("Type of media (TV, Movie, etc): ")
    ep_count = input("Episode count: ")
    ep_watched = input("Episodes watched: ")
    start_date = input("Date started: ")
    end_date = input("Date finished: ")
    # advanced strings 7.3
    ani_score = input(r"Score (-\10) will look like this:(5\10): ")
    add_anime[title] = [ani_type, f'EP: {ep_watched}/{ep_count}', f'START: {start_date}', f'FINISHED: {end_date}', f'RATING: {ani_score}\\10']
    print("Added Successfully!")
    # advanced strings 7.2
    prompt = input("Add more Animes? (y\\n): ").lower()
    if prompt != 'y':
        add = False
add_anime_csv = pandas.DataFrame(add_anime)
add_anime_csv = pandas.DataFrame.to_csv(add_anime_csv)
print(add_anime_csv)