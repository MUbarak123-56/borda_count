# Borda Count Voting System

The first stage of the Borda Count Voting System collects each voter's ranked choice for a set of candidates and allocates points to each candidate based on their rank. The second stage calculates the final ranking by summing up each candidates' points across all the voters' rankings to determine the final order of the results

For example, if there are three candidates competing in an election: Josie, Brad and Charles, and three voters.
Voter 1 votes in the order of Brad, Josie and Charles. Brad gets 3, Josie gets 2 and Charles gets 1 for this voter. 
Voter 2 votes in the order of Charles, Brad and Josie. Charles gets 3, Brad gets 2 and Josie gets 1 for this voter.
Voter 3 votes in the order of Brad, Charles and Josie. Brad gets 3, Charles gets 2 and Josie gets 1 for this voter.

At the end of voting, Brad gets 8 points, Charles gets 6 points and Josie gets 4 points. Therefore, Brad gets 1st place, Charles 2nd place and Josie 3rd place.

For more information, you can check [here](https://en.wikipedia.org/wiki/Borda_count).
