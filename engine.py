# engine.py

import pandas as pd
import os

class Engine:
	def __init__(self, data):
		self.data = data
		
		self.subjects = ['Math', 'English', 'Kiswahili', 'Science']
		
	def grade(self, mean_score):
		'''Classifies subject and student mean score:
		Range   Grade
		≥ 85    A
		70–84   B
		50–69   C
		< 50    F
		returns --> str'''
		if mean_score >= 85:
			return 'A'
		elif mean_score >= 70:
			return 'B'
		elif mean_score >= 50:
			return 'C'
		else:
			return 'F'

	def summary(self):
		'''Calculates summary metrics ordered by rank
		returns --> list of dicts'''
		
		df = pd.DataFrame(self.data)
		
		subject_headers = ''.join([f'{sub:<11}' for sub in self.subjects])
		
		df['Total'] = df[self.subjects].sum(axis=1)
		df['Mean'] = df[self.subjects].mean(axis=1).round(2)     
		df['Grade'] = df['Mean'].apply(self.grade)
		
		rank = df['Total'].rank(ascending=False, method='min').astype(int)
		df.insert(0, 'Rank', rank)
		 
		df = df.sort_values(by='Rank', ascending=True)
		
		self.summary_df = df
		
		summary_report = []
		output = f"{'Rank':<6} {'ID':<8} {'Name':<22} {subject_headers} {'Total':<8} {'Mean':<8} {'Grade':<8} {'School'}"
		
		for inx, row in df.iterrows():
			scores = ''.join([f'{row[sub]:<11}' for sub in self.subjects])
			report = {
				'rank': row['Rank'],
				'id': row['ID'],
				'name': row['Name'],
				'scores': scores,
				'total': int(row['Total']),
				'mean': row['Mean'],
				'grade': row['Grade'],
				'school': row['School']
			}
			summary_report.append(report)   
			
		return output, summary_report
		
	def save_summary(self):
		if not hasattr(self, 'summary_df'):
			print('[ERROR] Error when parsing Summary DataFrame.')
			return 
		
		report_name = input('Enter report name: ').strip()
		folder = f'reports/{report_name}'
		os.makedirs(folder, exist_ok=True)
		
		self.summary_df.to_csv(f'{folder}/summary.csv', index=False)
		self.summary_df.to_excel(f'{folder}/summary.xlsx', index=False)
		self.summary_df.to_json(f'{folder}/summary.json', orient='records', indent=4)
		
		print(f'[SUCESS] Created \'{report_name}\' summary report')
			
if __name__ == '__main__':
	from data_loader import DataLoader

	dl = DataLoader()
	data = dl.load_data()

	if data is not None:
		e = Engine(data)
		
		output, report = e.summary()
		 
		print('\n' + '\t'*5 + 'SUMMARY REPORT')
		print('=' * 315)
		print(output)
		print('-'*135)
		
		for student in report:
			print(f"{student['rank']:<6} {student['id']:<8} {student['name']:<22} {student['scores']:<44} {student['total']:<8} {student['mean']:<8} {student['grade']:<8} {student['school']}")
		print("=" * 135)
   
	e.save_summary()
	
