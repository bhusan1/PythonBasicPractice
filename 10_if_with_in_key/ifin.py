movies_watched={"Raw", "Saw", "Shark"}
user_movie = input("Enter a movie you watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too")
else:
    print("I haven't watched that yet.")
    
