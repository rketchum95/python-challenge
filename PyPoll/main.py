import os
import csv

csv_electiondata = os.path.join('Resources','PyPoll_Resources_election_data.csv')

candidates =[]

vote_count=0



with open(csv_electiondata, newline='',encoding='utf-8') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=",")
	
	csv_header=next(csvreader)

	for row in csvreader:
		#count #  of votas
		vote_count+=1
		print(vote_count)	
		





