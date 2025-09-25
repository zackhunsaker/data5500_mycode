import cloudscraper # pip install cloudscraper
import json




state_code = "ut"
#creating the scraper
scraper = cloudscraper.create_scraper()

url = "https://api.covidtracking.com/v1/states/ut/daily.json"
#getting the data
response = scraper.get(url)
data = response.json()

with open(state_code + ".json","w") as f: # opens a file on my computer and names it ut + json extension. It is in write mode so it creates or overides
    json.dump(data,f,indent=2)#indent = 2 makes the JSON pretty print with 2 spaces per indentation level(easier to read)


daily_cases = [] # create an empty list to store the data
for day in data:
    daily_cases.append(day["positiveIncrease"]) #adds each days new cases 
    
#calculate the average for the state of new cases

averagedailycases = sum(daily_cases) / len(daily_cases)  #this calculates the sum of the cases divided by the length of the list aka the denominator

print("Covid confirmed cases statistics")
print("State name:", state_code.upper())
print("Average number of new daily confirmed cases:", round(averagedailycases, 2))


#helper function
def get_cases(day):
    return day["positiveIncrease"]

#max day
max_day = max(data,key=get_cases)

print("Date with the highest new number of covid cases:", 
      max_day["date"], 
      "with", 
      max_day["positiveIncrease"], 
      "cases")

# function to check for zero cases
def is_zero_case(day):
    return day["positiveIncrease"] == 0  #this returns True if a day has zero new cases, False otherwise. 

most_recent_zero = None  #since the API gives utahs data by newest date first we have it give us the first match it finds. 

for day in data:
    if is_zero_case(day):
        most_recent_zero = day
        break #stop at the first one
if most_recent_zero:
    print("Most recent date with no new covid cases:", most_recent_zero["date"])
else:
    print("No days with zero new cases found")

#build the monthly totals dictionary

monthly_totals = {}

for day in data:
    date_str = str(day["date"])  #str() converts number to string so you can slice it
    year = date_str[0:4] # first 4 characters
    month = date_str[4:6]
    day_of_month = date_str[6:8]
    key = (year,month) 
    
    if key not in monthly_totals:  #basically saying if this month doesnt exist in the dict yet create it and start at 0
        monthly_totals[key] = 0
    monthly_totals[key] +=day["positiveIncrease"]
    
#helper function
def get_total(item):
    return item[1] # item = ((year,month),total)

# convert the dict to list of pairs
monthly_list = list(monthly_totals.items())

#find max and min month

max_month = max(monthly_list, key=get_total)
min_month = min(monthly_list,key=get_total)

print("Month/Year with highest new cases:", max_month[0][0], "-", max_month[0][1], "with", max_month[1], "cases")
print("Month/Year with lowest new cases:", min_month[0][0], "-", min_month[0][1], "with", min_month[1], "cases")


