# Task 1 Artist Lineup Compilation

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set(artist_names)
print(unique_artists)
'''
This output saves the artists_names in set where there are no duplicates using the built in set function. We print this and will later use this as confirmation 
our set comprehension worked in an if statement.
'''

unique_artists_v2 = {artist_name for artist_name in artist_names}
print(unique_artists_v2)
'''
Here we try out more sophisticated set comprehension method to build the same set we built earlier.
'''

if unique_artists_v2 == unique_artists:
    duplicate_playlist = True
    print(f"Duplicate Playlists Found: {duplicate_playlist}")
else:
    print("Set comprehension does not match the built in method. Incorrect code.")

'''
Here I use an if statement to compare the two sets built from the two methods: built in set function and set comprehension.
If the two sets are the same the new variable duplicate_playlists will be defined as a True boolean and an f-string will be printed where this True result for the two sets being duplicats will be shown in the terminal.
I also included an else statement in case there was a mistake in the code, saying that the set comprehension does not match the built-in method, however as I know the code is correct, this else statement will not be ran. 
'''