def find_anime_watch_status(database, watch_status):
    valid = ("completed", "dropped", "plan to watch")
    if watch_status.lower() not in valid:
        return -1
    for entry in range(len(database)):
        episodes = (database['Watched Episodes'][entry], database["Episodes"][entry])
        if database['Watch Status'][entry].lower() == watch_status.lower():
            print(f"{database['Title'][entry]}, {str(episodes).replace(',', '/').replace(' ', '')}")
    return 0