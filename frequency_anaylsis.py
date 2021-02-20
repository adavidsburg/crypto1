#
# Project 1, Frequency Analysis
#
import random
import os
import json



string_in="awesomeness hearkened aloneness beheld courtship swoops memphis attentional pintsized rustics hermeneutics dismissive delimiting proposes between postilion repress racecourse matures directions pressed miserabilia indelicacy faultlessly chuted shorelines irony intuitiveness cadgy ferries catcher wobbly protruded combusting unconvertible successors footfalls bursary myrtle photocompose";
def count_characters(string_in, to_sort):
    character_frequency = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,
    "l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0," ":0}
    i=0;
    string_in = string_in.lower();
    string_length = len(string_in)
    while i<len(string_in):
        character_frequency[string_in[i]]+=1
        i+=1
    if to_sort==1:
        character_frequency = dict(reversed(sorted(character_frequency.items(), key=lambda item: item[1])));

    for value in character_frequency:
        character_frequency[value] = character_frequency[value]/string_length
        print(value+':'+str(character_frequency[value]));
        pass
    return character_frequency

count_characters(string_in, 1)
