def display_game_settings(**settings):
    print("Game Settings: ")
    for key, value in settings.items():
            print(f"{key}: {value}")
    print(f"Setting Count: {len(settings)}")
            
display_game_settings(difficulty = "easy", sound = "True", lives = 3)
