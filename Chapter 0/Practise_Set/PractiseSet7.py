#Printing date using fstring and datetime modules
import datetime
today = datetime.datetime.today()
print(f"{today: %B %dm %Y}")

##Inside f-string ‘today’ assigned the current date and %B, %d, and %Y represents the full month, day of month, and year respectively.