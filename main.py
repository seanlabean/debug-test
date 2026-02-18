from models import DataEnricher
from utils.utils import calculate_metrics

def run_pipeline():
    print("Starting pipeline...")
    
    # 1. Test Inheritance & Call Stack
    enricher = DataEnricher("Alpha-Alpha")
    final_string = enricher.process("Raw Data")
    print(final_string)

    # 2. Test Logic & Error Handling
    # The '0' will trigger a ZeroDivisionError
    data_points = [10, 20, 30, 1, 50]
    score = calculate_metrics(data_points)
    
    print(f"Final Score: {score}")

if __name__ == "__main__":
    run_pipeline()