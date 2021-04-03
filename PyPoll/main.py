import os
import csv

csv_electiondata = os.path.join('Resources','PyPoll_Resources_election_data.csv')

candidates =[]
candidate_votes=[]
total_count=0
candidate_percentage=0


with open(csv_electiondata, newline='',encoding='utf-8') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=",")
	
	csv_header=next(csvreader)

	for row in csvreader:
		#count #  of votas
		total_count+=1
		
		#candidate name
		candidate=row[2]

		if candidate in candidates:
			candidate_index=candidates.index(candidate)
			candidate_votes[candidate_index]=candidate_votes[candidate_index]+1
		else:
			candidates.append(candidate)
			candidate_votes.append(1)

percentages=[]
max_votes=candidate_votes
max_index=0

#find candidate percentages
for candidate in candidates:
	candidate_percentage=round(candidate_votes[candidate_index]/total_count*100,2)
	percentages.append(candidate_percentage)
	
	#find election winner
	if candidate_votes > max_votes:
			max_votes = candidate_votes
			max_index=count
winner=candidates[max_index]

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_count}")
print("----------------------------")
print(f"{candidates}: {percentages}% ({candidate_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")