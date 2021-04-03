import os
import csv

csv_electiondata = os.path.join('Resources','PyPoll_Resources_election_data.csv')

candidates =[]
candidate_votes=[]
vote_count=0



with open(csv_electiondata, newline='',encoding='utf-8') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=",")
	
	csv_header=next(csvreader)

	for row in csvreader:
		#count #  of votas
		vote_count+=1
		
		#candidate name
		candidate=row[2]


		if candidate in candidates:
			candidate_index=candidates.index(candidate)
			candidate_votes[candidate_index]=candidate_votes[candidate_index]+1
		else:
			candidates.append(candidate)
			candidate_votes.append(1)




#print election analysis results to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print(f"{candidates}: ({candidate_votes})")


