# Election_Analysis

## Project Overviews
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of 
a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.66.2

## Summary 
<img width="380" alt="Screen Shot 2022-04-17 at 1 32 12 PM" src="https://user-images.githubusercontent.com/95447175/163731155-33ffe26d-c810-45d6-bf7f-222c38bedd52.png">

The analysis of the election shows that:
- There were 369,711 total votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
 - Charles Casper Stockham: 23.0% (85,213)
 - Diana DeGette: 73.8% (272,892)
 - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
 - Diana DeGette who received 73.8% of the votes and 272,892 votes 

## Challenge Overview
The election commission has requested some additional data to complete the audit:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Challenge Summary
<img width="391" alt="Screen Shot 2022-04-17 at 2 45 59 PM" src="https://user-images.githubusercontent.com/95447175/163733462-4d83c15f-a5ae-4179-8191-e284a84a5f24.png">

- Denver had the largest County turnout with 82.8% of the votes and 306,055 votes
- Jefferson county had 10.5% of the votes with 38,855 votes
- Arapahoe country had 6.7% of the votes with 24,801 votes

## Election Audit Suggestions
This script can be used for any election due to its use of macros; the file election_results.csv needs to be in the same place for access. The election_analysis.txt file should also be in the same location. 
- If the name or location of the csv file is modified, then line 7 of PyPoll_Challenge.py must be updated to reflect the updates.
 - file_to_load = os.path.join("Resources", "election_results.csv")
- If the name or location of the txt file is changed, then line 9 of PyPoll_Challenge.py needs to be modified. 
 - file_to_save = os.path.join("analysis", "election_analysis.txt")



