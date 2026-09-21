movie = input("Enter movie: ")
if movie.upper() == "HARRY POTTER" or movie.upper() == "ROTTMNT THE MOVIE":
    print("Awesome!!")
elif movie.upper() == "MATILDA":
    print("Cool")
elif movie.upper() == "ALIEN":
    print("Never watched it but cool and scary")
else:
    print("Unknown movie")

#Matchcase

match movie.upper():
    case "HARRY POTTER" | "ROTTMNT THE MOVIE":
        print("One of my favourites!!")
    case "MATILDA":
        print("Cool, I guess")
    case "ALIEN":
        print("Never watched it but it's scary.")    
    case _: #case else
        print("Unknown Movie")