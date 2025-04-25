import json, datetime

data = []
line_num = 1

#Opens the log file with read permissions
with open("logs.json", "r") as logs:
    for line in logs:
        #Check if each line is valid JSON and add to the Data list
        try:
            json_line = json.loads(line)
            data.append(json_line)

        #If line is not valid JSON, log the line number where the error occors
        except:
            print(f"Invalid JSON format, review file on line {str(line_num)}")

        line_num += 1


#Count severity of logs and store in dictionary
severity = {}

for log in data:

    if log["severity"] in severity:
        severity[log["severity"]] += 1

    else:
        severity[log["severity"]] = 1

print("Number of logs by severity: ")
print(severity)

#Sort logs by user in alphabetical order
users = []
user_sort = sorted(data, key=lambda x: x["actor"]["displayName"])
print("\nLogs sorted by user display name in alphabetical order: ")
print(user_sort)

for log in user_sort:
    users.append(log["actor"]["displayName"])

print("\nList of users alphabetically: ")
print(users)

#Find logs where authentication occurred after 5pm

late_auth = {}

for log in data:
    datetime_str = log["debugContext"]["debugData"]["authTime"]
    time_str = datetime_str[datetime_str.index("T")+1:-1]

    time = datetime.datetime.strptime(time_str, "%H:%M:%S")

    if time.hour > 17:
        late_auth[log["actor"]["displayName"]] = datetime_str
print("\nLogs where authentication occured after hours: ")
print(late_auth)

