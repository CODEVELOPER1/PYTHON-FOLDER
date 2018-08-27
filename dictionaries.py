#special structure which allows us to store info in KEY VALUE PAIR
#KEY VALUE PAIRS access info inside of dictionary can be referred to by it's KEY
# word & definition
#Word is the KEY
#Value is the Definition
#3 digit Month Name to Full Month Name
#always use { }

monthconversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    }

#print(monthconversions["Mar"])
print(monthconversions.get("liu", "Note a valid Key"))
#specify default value that i want to use if this ke is not found, defualt Key after comma