'''
Mad libs Generator
---------------------------------------
'''
#loop back to this point once code finish
loop = 1
while loop < 10:
    #all the ques user may ask...
    noun = input("choose a noun:   ")
    p_noun = input ("choose a plural noun:   ")
    noun_two = input ("chouse noun:  ")
    place = input ("name a place:  ")
    adjective = input ("choose adjective (Describing word):   ")
    noun_three = input ("choose a noun:  ")
# display the story based on the users input...
    print("------------------------")
    print("Be kind to your",noun,"-footed",p_noun)
    print("For a duck may be somebody's", noun_two, ",")
    print("Be kind to your", noun, "-footed", place)
    print("Where the weather is always", adjective, ".")
    print()
    print("You may think that is this the",noun_three, ",")
    print("Well it is.")
    print("------------------------------------------")
#Loop back to"loop = 1"
    loop = loop + 1