# setup.py

import pandas as pd
import os

print(f"{'='*50}\nInitializing Analytica sample datasets\n{'='*50}")

directories = [
    "data/nairobi", 
    "data/tambach",
    "data/singore",
    "data/alliance"
    ]

for path in directories:
    os.makedirs(path, exist_ok=True) 
    
print("Directory check complete!\n\n")

print("Creating sample datasets......\n\n")

# Sample datasets
nairobi_data = [
    {"ID": "S001", "Name": "Ava Heart", "School": "Nairobi High School", "Score": [80, 75, 54, 92]},
    {"ID": "S002", "Name": "Amina Hope", "School": "Nairobi High School", "Score": [74, 84, 64, 54]},
    {"ID": "S003", "Name": "Dennis Kosgei", "School": "Nairobi High School", "Score": [94, 54, 66, 84]},
    {"ID": "S004", "Name": "Chantal Ineza", "School": "Nairobi High School", "Score": [45, 60, 52, 48]},
    {"ID": "S005", "Name": "Kamau Mwangi", "School": "Nairobi High School", "Score": [85, 78, 90, 88]},
    {"ID": "S006", "Name": "Grace Mutua", "School": "Nairobi High School", "Score": [68, 72, 70, 65]},
    {"ID": "S007", "Name": "Josphat Kiprono", "School": "Nairobi High School", "Score": [55, 49, 61, 50]},
    {"ID": "S008", "Name": "Mary Atieno", "School": "Nairobi High School", "Score": [92, 88, 85, 95]},
    {"ID": "S009", "Name": "Alex Otieno", "School": "Nairobi High School", "Score": [41, 53, 48, 38]},
    {"ID": "S010", "Name": "Zainab Juma", "School": "Nairobi High School", "Score": [79, 81, 77, 83]},
    {"ID": "S011", "Name": "Kevin Omwamba", "School": "Nairobi High School", "Score": [63, 67, 58, 72]},
    {"ID": "S012", "Name": "Esther Waweru", "School": "Nairobi High School", "Score": [87, 84, 89, 91]},
    {"ID": "S013", "Name": "Michael Silas", "School": "Nairobi High School", "Score": [70, 75, 73, 68]},
    {"ID": "S014", "Name": "Sarah Nafula", "School": "Nairobi High School", "Score": [58, 62, 65, 59]},
    {"ID": "S015", "Name": "Emmanuel Kiprop", "School": "Nairobi High School", "Score": [76, 70, 82, 78]},
    {"ID": "S016", "Name": "Mercy Chepkorir", "School": "Nairobi High School", "Score": [89, 91, 87, 93]},
    {"ID": "S017", "Name": "Anthony Ndwiga", "School": "Nairobi High School", "Score": [47, 51, 50, 46]},
    {"ID": "S018", "Name": "Faith Muthoni", "School": "Nairobi High School", "Score": [82, 79, 85, 80]},
    {"ID": "S019", "Name": "Peter Omondi", "School": "Nairobi High School", "Score": [66, 60, 64, 70]},
    {"ID": "S020", "Name": "Lucy Njeri", "School": "Nairobi High School", "Score": [73, 76, 71, 74]},
    {"ID": "S021", "Name": "Caleb Bett", "School": "Nairobi High School", "Score": [90, 85, 88, 87]},
    {"ID": "S022", "Name": "Aisha Mohamed", "School": "Nairobi High School", "Score": [52, 57, 54, 61]},
    {"ID": "S023", "Name": "Daniel Gakuru", "School": "Nairobi High School", "Score": [81, 83, 80, 85]},
    {"ID": "S024", "Name": "Priscah Chemutai", "School": "Nairobi High School", "Score": [60, 64, 62, 58]}
]

alliance_data = [
    {"ID": "A001", "Name": "Brian Mwangi", "School": "Alliance High School", "Score": [88, 90, 78, 85]},
    {"ID": "A002", "Name": "George Njoroge", "School": "Alliance High School", "Score": [55, 48, 60, 67]},
    {"ID": "A003", "Name": "Ian Maina", "School": "Alliance High School", "Score": [91, 85, 88, 92]},
    {"ID": "A004", "Name": "David Kimani", "School": "Alliance High School", "Score": [72, 76, 80, 69]},
    {"ID": "A005", "Name": "Samuel Karanja", "School": "Alliance High School", "Score": [64, 59, 71, 63]},
    {"ID": "A006", "Name": "Victor Kipkemboi", "School": "Alliance High School", "Score": [83, 87, 79, 88]},
    {"ID": "A007", "Name": "John Kamau", "School": "Alliance High School", "Score": [49, 55, 52, 46]},
    {"ID": "A008", "Name": "Patrick Omwamba", "School": "Alliance High School", "Score": [77, 81, 74, 85]},
    {"ID": "A009", "Name": "Moses Otieno", "School": "Alliance High School", "Score": [95, 93, 89, 96]},
    {"ID": "A010", "Name": "Collins Bett", "School": "Alliance High School", "Score": [68, 70, 65, 72]},
    {"ID": "A011", "Name": "Erick Wanjala", "School": "Alliance High School", "Score": [58, 62, 60, 54]},
    {"ID": "A012", "Name": "James Ndung'u", "School": "Alliance High School", "Score": [86, 84, 91, 89]},
    {"ID": "A013", "Name": "Andrew Kibet", "School": "Alliance High School", "Score": [73, 79, 75, 81]},
    {"ID": "A014", "Name": "Peter Nyongesa", "School": "Alliance High School", "Score": [42, 50, 47, 45]},
    {"ID": "A015", "Name": "Simon Gathecha", "School": "Alliance High School", "Score": [80, 82, 85, 78]},
    {"ID": "A016", "Name": "Evans Kipruto", "School": "Alliance High School", "Score": [69, 73, 71, 66]},
    {"ID": "A017", "Name": "Philip Mutiso", "School": "Alliance High School", "Score": [92, 88, 94, 90]},
    {"ID": "A018", "Name": "Mathew Kuria", "School": "Alliance High School", "Score": [61, 58, 64, 60]},
    {"ID": "A019", "Name": "Paul Mwangangi", "School": "Alliance High School", "Score": [75, 78, 72, 83]},
    {"ID": "A020", "Name": "Joseph Maingi", "School": "Alliance High School", "Score": [84, 86, 81, 87]},
    {"ID": "A021", "Name": "Charles Wamalwa", "School": "Alliance High School", "Score": [53, 47, 55, 51]},
    {"ID": "A022", "Name": "Stephen Kiptoo", "School": "Alliance High School", "Score": [79, 83, 80, 82]},
    {"ID": "A023", "Name": "Timothy Ochieng", "School": "Alliance High School", "Score": [87, 89, 86, 91]},
    {"ID": "A024", "Name": "Francis Kariuki", "School": "Alliance High School", "Score": [66, 68, 70, 64]}
]

tambach_data = [
    {"ID": "T001", "Name": "Kipchumba Kiprop", "School": "Tambach High School", "Score": [85, 76, 80, 88]},
    {"ID": "T002", "Name": "Emmanuel Kiptoo", "School": "Tambach High School", "Score": [68, 70, 65, 72]},
    {"ID": "T003", "Name": "Silas Kemboi", "School": "Tambach High School", "Score": [91, 84, 86, 89]},
    {"ID": "T004", "Name": "Cornelius Rotich", "School": "Tambach High School", "Score": [54, 60, 58, 63]},
    {"ID": "T005", "Name": "Gideon Biwott", "School": "Tambach High School", "Score": [77, 81, 79, 85]},
    {"ID": "T006", "Name": "Titus Cheboi", "School": "Tambach High School", "Score": [63, 59, 67, 60]},
    {"ID": "T007", "Name": "Vincent Lagat", "School": "Tambach High School", "Score": [48, 52, 50, 47]},
    {"ID": "T008", "Name": "Kipruto Koech", "School": "Tambach High School", "Score": [89, 92, 88, 91]},
    {"ID": "T009", "Name": "Collins Kibet", "School": "Tambach High School", "Score": [73, 75, 71, 78]},
    {"ID": "T010", "Name": "Geoffrey Cheruiyot", "School": "Tambach High School", "Score": [66, 68, 64, 62]},
    {"ID": "T011", "Name": "Evans Kipkemboi", "School": "Tambach High School", "Score": [82, 85, 80, 84]},
    {"ID": "T012", "Name": "Dennis Kwemoi", "School": "Tambach High School", "Score": [59, 62, 60, 55]},
    {"ID": "T013", "Name": "Kelvin Tanui", "School": "Tambach High School", "Score": [70, 74, 72, 69]},
    {"ID": "T014", "Name": "Robert Komen", "School": "Tambach High School", "Score": [42, 49, 45, 51]},
    {"ID": "T015", "Name": "Moses Kipruto", "School": "Tambach High School", "Score": [94, 88, 90, 93]},
    {"ID": "T016", "Name": "Amos Chepkwony", "School": "Tambach High School", "Score": [79, 83, 81, 80]},
    {"ID": "T017", "Name": "Bernard Kangogo", "School": "Tambach High School", "Score": [61, 57, 63, 58]},
    {"ID": "T018", "Name": "Peter Kipchumba", "School": "Tambach High School", "Score": [86, 90, 87, 89]},
    {"ID": "T019", "Name": "Meshack Rono", "School": "Tambach High School", "Score": [67, 71, 69, 70]},
    {"ID": "T020", "Name": "Brian Kipsang", "School": "Tambach High School", "Score": [52, 55, 53, 49]},
    {"ID": "T021", "Name": "Duncan Kibor", "School": "Tambach High School", "Score": [80, 78, 83, 82]},
    {"ID": "T022", "Name": "Fredrick Kipkeu", "School": "Tambach High School", "Score": [75, 77, 74, 76]},
    {"ID": "T023", "Name": "Hilary Maiyo", "School": "Tambach High School", "Score": [90, 86, 89, 92]},
    {"ID": "T024", "Name": "Wilson Kiptum", "School": "Tambach High School", "Score": [58, 64, 61, 57]}
]

singore_data = [
    {"ID": "SG001", "Name": "Mercy Chepkorir", "School": "Singo're Girls", "Score": [89, 91, 87, 93]},
    {"ID": "SG002", "Name": "Priscah Chemutai", "School": "Singo're Girls", "Score": [60, 64, 62, 58]},
    {"ID": "SG003", "Name": "Linah Chebet", "School": "Singo're Girls", "Score": [84, 88, 85, 82]},
    {"ID": "SG004", "Name": "Faith Kiprop", "School": "Singo're Girls", "Score": [73, 76, 71, 79]},
    {"ID": "SG005", "Name": "Gladys Jerotich", "School": "Singo're Girls", "Score": [52, 58, 55, 61]},
    {"ID": "SG006", "Name": "Sharon Kiptoo", "School": "Singo're Girls", "Score": [91, 89, 94, 92]},
    {"ID": "SG007", "Name": "Brenda Chepkemoi", "School": "Singo're Girls", "Score": [66, 70, 68, 65]},
    {"ID": "SG008", "Name": "Nancy Jepchirchir", "School": "Singo're Girls", "Score": [45, 52, 48, 50]},
    {"ID": "SG009", "Name": "Diana Chelagat", "School": "Singo're Girls", "Score": [82, 85, 81, 87]},
    {"ID": "SG010", "Name": "Vivian Jelagat", "School": "Singo're Girls", "Score": [70, 74, 72, 69]},
    {"ID": "SG011", "Name": "Ruth Jepkoech", "School": "Singo're Girls", "Score": [58, 61, 59, 56]},
    {"ID": "SG012", "Name": "Caroline Chepkoech", "School": "Singo're Girls", "Score": [95, 92, 90, 96]},
    {"ID": "SG013", "Name": "Naomi Jematia", "School": "Singo're Girls", "Score": [77, 80, 78, 83]},
    {"ID": "SG014", "Name": "Emily Jepkemoi", "School": "Singo're Girls", "Score": [63, 67, 65, 60]},
    {"ID": "SG015", "Name": "Jackline Chepkosgei", "School": "Singo're Girls", "Score": [41, 48, 44, 46]},
    {"ID": "SG016", "Name": "Stacy Chepkurui", "School": "Singo're Girls", "Score": [88, 86, 89, 91]},
    {"ID": "SG017", "Name": "Daisy Jepchumba", "School": "Singo're Girls", "Score": [71, 75, 73, 70]},
    {"ID": "SG018", "Name": "Mercy Jelimo", "School": "Singo're Girls", "Score": [54, 57, 60, 53]},
    {"ID": "SG019", "Name": "Joy Cheptoo", "School": "Singo're Girls", "Score": [86, 90, 88, 85]},
    {"ID": "SG020", "Name": "Phyllis Jepkorir", "School": "Singo're Girls", "Score": [68, 72, 70, 66]},
    {"ID": "SG021", "Name": "Anita Chebet", "School": "Singo're Girls", "Score": [49, 53, 51, 47]},
    {"ID": "SG022", "Name": "Hellen Juma", "School": "Singo're Girls", "Score": [80, 83, 82, 84]},
    {"ID": "SG023", "Name": "Lydia Chemutai", "School": "Singo're Girls", "Score": [75, 78, 76, 77]},
    {"ID": "SG024", "Name": "Rachael Jepleting", "School": "Singo're Girls", "Score": [93, 91, 95, 89]}
]


# Data refractor 
def save_data(raw_data, folder_name):
    """
    Converts list of dicts to DataFrame, expands the Score list into separate 
    subject columns, drops the old 'Score' column, and exports to disk.
    """
    df = pd.DataFrame(raw_data)
    
    subjects = ['Math', 'English', 'Kiswahili', 'Science']
    df[subjects] = pd.DataFrame(df['Score'].tolist(), index=df.index)
    
    # Drops the score column into subjects
    df = df.drop(columns=['Score'])
    
    file_path = f"data/{folder_name}/all_students"
    df.to_csv(f"{file_path}.csv", index=False)
    df.to_excel(f"{file_path}.xlsx", index=False)
    df.to_json(f"{file_path}.json", orient="records", indent=4)
    
    print(f"[SUCCESS] Created {folder_name} data!")
    return df


n_df = save_data(nairobi_data, "nairobi")
a_df = save_data(alliance_data, "alliance")
t_df = save_data(tambach_data, "tambach")
s_df = save_data(singore_data, "singore")


# Full Master List
full_df = pd.concat([n_df, a_df, t_df, s_df], ignore_index=True)

full_df.to_csv("data/all_students.csv", index=False)
full_df.to_excel("data/all_students.xlsx", index=False)
full_df.to_json("data/all_students.json", orient="records", indent=4)

print(f"\n\n[SUCCESS] Master dataset created with {len(full_df)} total students.")
