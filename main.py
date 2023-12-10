import pandas
import numpy
from functions import find_anime_watch_status

with open("animelist_csv.csv") as data_file:
    ani_data = pandas.read_csv(data_file)
    ani_data_frame = pandas.DataFrame(ani_data)
    # print(ani_data_frame)

ani_data_frame = ani_data_frame.set_axis(['ID', 'Title', 'Type', 'Episodes', 'Watched Episodes',
                          'Start Date', 'End Date', 'My Rating', 'Watch Status',
                          'Times Completed', 'Watch Priority', 'Tags'],
                         axis='columns') 

for i in range(len(ani_data_frame)):
    if ani_data_frame['Start Date'][i] == "0000-00-00": 
        ani_data_frame['Start Date'][i] = 'N/A'
    if ani_data_frame['End Date'][i] == "0000-00-00":
        ani_data_frame['End Date'][i] = 'N/A'

print(ani_data_frame)
find_watching_episodes = []
find_total_episodes = []
find_episode_title = []
for entry in range(len(ani_data_frame)):
    if ani_data_frame['Watch Status'][entry] == "Watching":
        find_watching_episodes.append(int(ani_data_frame['Watched Episodes'][entry]))
        find_total_episodes.append(int(ani_data_frame['Episodes'][entry]))
        find_episode_title.append(ani_data_frame['Title'][entry])
    
result_vector = (numpy.array(find_watching_episodes) / numpy.array(find_total_episodes))*100
# print(result_vector)
for i in range(len(find_episode_title)):
    print(f"You've watched: {round(float(result_vector[i]), 2)}% of {find_episode_title[i]}")


sort = input("What do you want so sort by? (Completed, Plan to Watch, Dropped): ")
if find_anime_watch_status(ani_data_frame, sort) == -1:
    print("Unknown Status")
else: 
    find_anime_watch_status(ani_data_frame, sort)

add = True
add_anime = {}
while add:
    title = input("Title of Anime: ").title()
    ani_type = input("Type of media (TV, Movie, etc): ")
    ep_count = input("Episode count: ")
    ep_watched = input("Episodes watched: ")
    start_date = input("Date started: ")
    end_date = input("Date finished: ")
    ani_score = input("Score (-/10):")
    add_anime[title] = [ani_type, f'EP: {ep_watched}/{ep_count}', f'START: {start_date}', f'FINISHED: {end_date}', f'RATING: {ani_score}/10']
    print("Added Successfully!")
    prompt = input("Add more Animes? (y/n): ").lower()
    if prompt != 'y':
        add = False
add_anime_csv = pandas.DataFrame(add_anime)
add_anime_csv = pandas.DataFrame.to_csv(add_anime_csv)
print(add_anime_csv)