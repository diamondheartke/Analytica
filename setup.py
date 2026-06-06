import pandas as pd

# Math, English, Kiswahili, Computer
data = [
	{"ID": "S001", "Name": "Ava Heart", "School": "Nairobi High School", "Score": [80, 75, 54, 92]},
	{"ID": "S002", "Name": "Amina Hope", "School": "Nairobi High School", "Score": [74, 84, 64, 54]},
	{"ID": "S003", "Name": "Dennis Kosgei", "School": "Nairobi High School", "Score": [94, 54, 66, 84]},
]
 
df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

df.to_excel("students.xlsx", index=False)
