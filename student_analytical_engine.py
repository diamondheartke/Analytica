# student_analytical_engine.py

# ====== Student Performance Analytics Engine ======

import numpy as np

class AnalyticEngine:
    def __init__(self, data):
        print(f"{'='*6} Student Performance Analytics Engine {'='*6}\n")
        # row = a student
        # column = a subject
        # Subjects: Math, English, Science, Computer
        self.scores = data

    def basic_stats(self):
        '''Computes:
            - Overall average score
            - Average per student
            - Average per subject
            - Highest and lowest score in dataset
           Returns --> dict'''
        print('---- Basic Stats ----')
        return {
            'average_score': np.mean(self.scores),
            'average_student': np.mean(self.scores, axis=1),
            'average_subject': np.mean(self.scores, axis=0),
            'highest': np.max(self.scores),
            'lowest': np.min(self.scores)
          }

    def student_rank(self):
        '''Ranks Students based on their total score
           Returns --> Sorted indices of students (best to worst)'''
        print('\n---- Student Ranking ----')
        total_scores = np.sum(self.scores, axis=1)
        return np.argsort(total_scores)[::-1]

    def performance_classify(self):
        ''' Classifies each score:
                Range   Grade

                ≥ 85    A
                70–84   B
                50–69   C
                < 50    F '''
        print('\n---- Performance Classification ----')
        def grade(x):
            if x >= 85:
                return 'A'
            elif x >= 70:
                return 'B'
            elif x >= 50:
                return 'C'
            else:
                return 'F'

        vectorized_grade = np.vectorize(grade)
        return vectorized_grade(self.scores)

    def normalization(self):
        '''Normalises subject scores: (value - mean) / std'''
        print('\n---- Normalization ----')
        mean = np.mean(self.scores, axis=0)
        std = np.std(self.scores, axis=0)

        return (self.scores - mean) / std

    def weak_students(self):
        '''Identifies weak students.
           A student is weak if their average < 60
           Returns --> list [indices of weak students, Their full score rows]'''
        print('\n---- Weak Students ----')
        student_avg = np.mean(self.scores, axis=1)

        weak_indices = np.where(student_avg < 60)[0]

        return {
            "weak_student_indices": weak_indices,
            "weak_student_scores": self.scores[weak_indices]
        }

    def bonus_marks(self):
        '''Adds a bonus +5 marks to every subject
            But max score = 100'''
        print('\n---- Bonus Marks ----')
        def add(x):
            if x < 100:
                x+=5
                if x > 100:
                    x=100
            return x

        vectorized = np.vectorize(add)
        return vectorized(self.scores)

        # A little sth i got from a little bird:
        np.clip(self.scores + 5, 0, 100)

    def insights(self):
        '''Gets:
                Top two students (full data)
                Bottom 2 students
                Scores of only students who scored > 90 in any subject'''
        print('---- Insights ----')

        total_scores = np.sum(self.scores, axis=1)
        ranked = np.argsort(total_scores)

        top_2_indices = ranked[-2:][::-1]
        bottom_2_indices = ranked[:2]

        above_90_indices = np.where(np.any(self.scores > 90, axis=1))[0]
        return {
            'top_2': self.scores[top_2_indices],
            'bottom_2': self.scores[bottom_2_indices],
            'above_90': self.scores[above_90_indices]
        }

    def restructure_data(self):
        '''converts dataset into:
            shape(subjects, students)'''
        print('\n---- Data Reconstruction ----')
        return self.scores.T

    def combine_data(self, new_data):
        '''Merges old dataset with new data'''
        print('\n---- Combined Data ----')
        return np.vstack((self.scores, new_data))


    def split_dataset(self):
        '''Splits dataset into:
            Train set (first 70%)
            Test set (remaining 30%)'''
        print('\n---- Split Dataset')
        
        split_index = int(len(self.scores) * 0.7)

        train_set = self.scores[:split_index]
        test_set = self.scores[split_index:]

        return {
            '70%': train_set,
            '30%': test_set
        }


if __name__ == '__main__':
    engine = AnalyticEngine()
    bs = engine.basic_stats()

    print('Overall Score:\n', bs['average_score'])
    print('Average Per Student:\n', bs['average_student'])
    print('Average Per Subject:\n', bs['average_subject'])
    print('Highest Score in dataset:\n', bs['highest'])
    print('Lowest Score in dataset:\n', bs['lowest'])

    print('Students Ranking:\n', engine.student_rank())

    print('Students Classification:\n', engine.performance_classify())

    print('Normalised Subject Data:\n', engine.normalization())

    print('Weak Students:\n', engine.weak_students())

    print('Bonus Marks:\n', engine.bonus_marks())

    print('Insights:\n', engine.insights())

    print('Reconstructed Data:\n', engine.restructure_data())

    new_scores = np.array([
        [60, 65, 70, 75],
        [95, 90, 93, 92]
    ])
    print('Combined Data:\n', engine.combine_data(new_scores))

    print('Split Dataset:\n', engine.split_dataset())
