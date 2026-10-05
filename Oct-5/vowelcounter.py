#word = input("Enter a word for us to count vowels: ")
#a_count = 0
#e_count = 0
#i_count = 0
#o_count = 0
#u_count = 0
#total = 0

#for character in word:
   # if character == "a":
   #     a_count += 1
  #  elif character == "e":
  #      e_count += 1
   # elif character == "i":
   #     i_count += 1
    #elif character == "o":
   #     o_count += 1
    #elif character == "u":
      #  u_count += 1

##total = a_count + e_count + i_count + o_count + u_count

#print(f"a: {a_count}")
#print(f"e: {e_count}")
#print(f"i: {i_count}")
#print(f"o: {o_count}")

#print(f"u: {u_count}")
#print(f"Total vowels: {total}")

word = input("Enter a word for us to count the vowels: ").lower()

vowel_counts = []

for vowel in "aeiou":
    count = 0
    for character in word:
        if character == vowel:
            count += 1
    vowel_counts.append((vowel,count))
    
print(vowel_counts)