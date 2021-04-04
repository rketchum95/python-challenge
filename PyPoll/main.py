import os
import csv

csv_electiondata = os.path.join('Resources','PyPoll_Resources_election_data.csv')

candidates =[]
candidate_votes=[]
total_count=0
#candidate_percentage=0


with open(csv_electiondata, newline='',encoding='utf-8') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=",")
	
	csv_header=next(csvreader)

	for row in csvreader:
		#count #  of votes
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
max_votes=0

#find candidate percentages
for votes in range(len(candidates)):
	candidate_percentage=round((candidate_votes[votes])/total_count*100,4)
	percentages.append(candidate_percentage)
	
	#find election winner
	if candidate_votes[votes]> max_votes:
			max_votes = candidate_votes[votes]
			max_index=votes
winner=candidates[max_index]

#terminal analysis:
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_count}")
print("----------------------------")
for votes in range(len(candidates)):
	print(f"{candidates[votes]}: {percentages[votes]}% ({candidate_votes[votes]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#text file:
filename = 'PyPoll_Analysis.txt'
with open (filename,'w') as file_object:
	file_object.write("Election Results\n")
	file_object.write("----------------------------\n")
	file_object.write(f"Total Votes: {total_count}\n")
	file_object.write("----------------------------\n")
	for votes in range(len(candidates)):
		file_object.write(f"{candidates[votes]}: {percentages[votes]}% ({candidate_votes[votes]})\n")
	file_object.write("----------------------------\n")
	file_object.write(f"Winner: {winner}\n")
	file_object.write("----------------------------\n")
