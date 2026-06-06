from student_analytical_engine import AnalyticEngine
from data_loader import DataLoader
import numpy as np

class Analytica:
    def __init__(self):
        self.loader = DataLoader()
        self.engine = None

    def run(self):
        print("\n\t\tInitializing Analytica.....\n")

        data = self.loader.load_data()

        if data is None:
            print("[INFO] No data loaded.")
            return

        self.engine = AnalyticEngine(data)

        self.dashboard()

    def dashboard(self):
        print("\nANALYTICS DASHBOARD\n")

        print("Basic Stats:", self.engine.basic_stats())
        print("Ranking:", self.engine.student_rank())
        print("Weak Students:", self.engine.weak_students())
        print("Insights:", self.engine.insights())

if __name__ == "__main__":
    app = Analytica()
    app.run()
