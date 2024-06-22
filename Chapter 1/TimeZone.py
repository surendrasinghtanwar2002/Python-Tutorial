from datetime import datetime

#define the epoch date
starting_Date=datetime(2002,6,2,0,0,0)

#define today date
current_Date = datetime(2024,6,22,0,0,0)

Solution = (current_Date - starting_Date)
print("Your total second is", Solution.total_seconds())