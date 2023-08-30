from datetime import datetime

date_string = "28 November, 2018"
print(date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
