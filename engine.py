import numpy as np
import ast

class Engine:
    def __init__(self, data):
        self.data = data
        self.scores = np.array([ast.literal_eval(row[3]) for row in self.data])

    def rank(self):
        '''Ranks Students from the best to worst
        returns --> object'''
        total = np.sum(self.scores, axis=1) # Fixed to self.scores to match numerical ranking
        return np.argsort(total.astype(float))[::-1]

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
        ranked_indices = self.rank()
        summary_report = []

        for rank_pos, idx in enumerate(ranked_indices):
            student_row = self.data[idx]
            student_scores = self.scores[idx]

            # Calculations
            total_score = int(np.sum(student_scores))
            mean_score = float(np.mean(student_scores))
            letter_grade = self.grade(mean_score)

            student_summary = {
                "rank": rank_pos + 1,  # 1-based ranking
                "id": student_row[0],
                "name": student_row[1],
                "total": total_score,
                "mean": round(mean_score, 2),
                "grade": letter_grade
            }
            summary_report.append(student_summary)

        return summary_report


if __name__ == '__main__':
    from data_loader import DataLoader

    dl = DataLoader()
    data = dl.load_data()

    if data is not None:
        e = Engine(data=data)

        # Capture the returned list instead of printing inside the class
        report = e.summary()

        # Display the formatted report
        print(f"{'Rank':<6} {'ID':<6} {'Name':<15} {'Total':<6} {'Mean':<6} {'Grade':<5}")
        print("-" * 50)
        for student in report:
            print(f"{student['rank']:<6} {student['id']:<6} {student['name']:<15} {student['total']:<6} {student['mean']:<6} {student['grade']:<5}")
