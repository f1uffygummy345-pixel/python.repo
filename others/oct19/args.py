def display_snacks(*snacks):
    if len(snacks) == 0:
        print("no snacks packed")
    else:
        for snack in snacks:
            print(f"-{snack}")
        print(f"Snack count: {len(snacks)}")
            
display_snacks()