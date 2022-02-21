# Wordle
Wordle solving algorithm

The algorithm gives the user a very good initial guess that would return a lot of feedback information.
The algorithm uses the feedback clues from the game (user has to enter them into the algorithm) to give the most likely solution. The algorithm initially starts with a set containing all five-letter words. With every clue it  eliminates words that don't meet the constraints obatined from the feedback. 
For example: you start with the initial guess of "inlay"
and the wordle of the day is "resit".
The game would tell the user that the wordle doesn't have the letters n,l,a,y. In addition, it has the letter "i" in a position otherthan the fourth.
The algorithm would then eliminates the words that don't meet these conditions from the initial set of five-letter words.
From the remaining words in the set, the algorithm chooses the best Discriminative word that would return the most feedback information. Choosing that word is based on Entropy (information theory). The idea is that a good guessing word would have distinct letters that are used the most. For example, a guessing word of the letter 'Z' wouldn't be very good as that letter is not in a lot of words, and hence wouldn't cover as much in searching.
