#import dependencies
import os
import csv

#read csv file
csv_budgetdata = os.path.join('Resources','budget_data.csv')

#Variable definitions
months=[]
monthly_changes=[]

#set variables to zero
count_months=0
net_profit=0
previous_profit=0
current_profit=0
MoM_change=0
total_change=0

#for loop to get variable amounts for analysis calculations:
with open(csv_budgetdata, newline='',encoding='utf-8') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=",")
	
	csv_header=next(csvreader)

	for row in csvreader:
		#Count months
		count_months+=1
		current_profit=int(row[1])
		net_profit+=int(row[1])

		if count_months==1:
			previous_profit=current_profit
		else:
			#calculate Month over Month(MoM) change
			
			MoM_change=current_profit-previous_profit

			#add each month to month list
			months.append(row[0])

			#append to monthly changes list
			monthly_changes.append(MoM_change)

						
			#Reset previous month profit for next loop
			previous_profit = current_profit

	#calculate total changes over time period
	total_change=sum(monthly_changes)
	
	#calculate average changes over period, minus 1 month for first month
	average_change=round(total_change/(count_months-1),2)
	
	#find max increase/decrease in monthly changes
	max_increase = max(monthly_changes)
	min_increase = min(monthly_changes)

	#create index for max increase/decrease
	high_month_index = monthly_changes.index(max_increase)	
	low_month_index = monthly_changes.index(min_increase)

	#find month of max increase/decreaes
	best_month=months[high_month_index]
	worst_month=months[low_month_index]

#print analysis to terminal:	
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {best_month}  ${max_increase}")
print(f"Greatest Decrease in Profits: {worst_month} ${min_increase}")

#export analysis to text file:
save_path = os.path.join('Analysis','PyBank_Analysis.txt')

#filename = 'PyBank_Analysis.txt'

with open (save_path,'w') as file_object:
	file_object = csv.writer(file_object)
	
	file_object.writerow(["Financial Analysis"])
	file_object.writerow(["---------------------"])
	file_object.writerow([f"Total Months: {count_months}"])
	file_object.writerow([f"Total: ${net_profit}"])
	file_object.writerow([f"Average Change: ${average_change}"])
	file_object.writerow([f"Greatest Increase in Profits: {best_month}  ${max_increase}"])
	file_object.writerow([f"Greatest Decrease in Profits: {worst_month} ${min_increase}"])

