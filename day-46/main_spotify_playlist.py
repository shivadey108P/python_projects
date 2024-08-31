from billboard import Bill_Board_Songs

date = input('Which year would you like to travel to? Type the date in this format (YYYY-MM-DD): ')
billboard_songs = Bill_Board_Songs(date)

songs_list =  billboard_songs.get_top_100_songs()

