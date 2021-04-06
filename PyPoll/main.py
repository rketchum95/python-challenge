import os
import csv

csv_electiondata = os.path.join('Resources','PyPoll_Resources_election_data.csv')

candidates =[]
candidate_votes=[]
total_count=0

#open csv:
with open(csv_electiondata, newline='',encoding='utf-8') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=",")

#read and skip header row:	
	csv_header=next(csvreader)

#for loop to find # of votes for total & each candidate
	for row in csvreader:
		#count #  of votes
		total_count+=1
		
		#candidate name
		candidate=row[2]

#assign vote count to each candidate:
		if candidate in candidates:
			candidate_index=candidates.index(candidate)
			candidate_votes[candidate_index]=candidate_votes[candidate_index]+1
		else:
			candidates.append(candidate)
			candidate_votes.append(1)

percentages=[]
max_votes=candidate_votes
max_votes=0

#calculate candidate percentages
for votes in range(len(candidates)):
	candidate_percentage=round((candidate_votes[votes])/total_count*100,4)
	percentages.append(candidate_percentage)
	
	#calcuate election winner
	if candidate_votes[votes]> max_votes:
			max_votes = candidate_votes[votes]
			max_index=votes
winner=candidates[max_index]

#print analysis to terminal:
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_count}")
print("----------------------------")
for votes in range(len(candidates)):
	print(f"{candidates[votes]}: {percentages[votes]}% ({candidate_votes[votes]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# save analysis to text file:
save_path = os.path.join('Analysis','PyPoll_Analysis.txt')

#filename = 'PyPoll_Analysis.txt'

with open (save_path,'w',newline='') as file_object:
	file_object=csv.writer(file_object)
	file_object.writerow(["Election Results"])
	file_object.writerow(["----------------------------"])
	file_object.writerow([f"Total Votes: {total_count}"])
	file_object.writerow(["----------------------------"])
	for votes in range(len(candidates)):
		file_object.writerow([f"{candidates[votes]}: {percentages[votes]}% ({candidate_votes[votes]})"])
	file_object.writerow(["----------------------------"])
	file_object.writerow([f"Winner: {winner}"])
	file_object.writerow(["----------------------------"])
