import os
import csv
import enum

budget_data_csv = os.path.join("C:\\Users\\kmf18\\OneDrive\\Desktop\\python-challenge\\Instructions\\PyBank\\Resources\\budget_data.csv")


with open(budget_data_csv, 'r') as csvfile:
     csv_reader = csv.reader(budget_data_csv, delimiter=',')

     next(csv_reader)

     row_count = 0
for row in csv_reader:
        row_count += 1

print(f'Total Months: {row_count}')
    
sum = 0
for i, row in enumerate(csv_reader):
        if i : '1'
for value in row:
             sum += 1
             
print(f'Total: {sum}')
    
value = row
avg_chg = 0
for row in csv_reader:
        for value in row:
            avg_chg += float(value)

        print(f'Average Change: {avg_chg}')
    
        value = [1]
        date = ["month","day"]
        day_of_month = {"dd":['01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']}

        month_of_yr = {"mm":['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
        
for row in csv_reader:
        for value in row:
            value += max(float(value))
            day_of_month = min(str('dd'))
            month_of_yr = min(str('mm'))                       

        print(f'Greatest Increase In Profits: {day_of_month},{month_of_yr},{value}')
        


        
    
        value = [1]
        day_of_month = {"dd":['01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']}

        month_of_yr = {"mm":['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}


for row in csv_reader:
        value += min(float(value))
        day_of_month = min(str('dd'))
        month_of_yr = min(str('mm'))

        
        print(f'Greatest Decrease In Profits: {day_of_month},{month_of_yr},{value}')

