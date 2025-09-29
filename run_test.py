import pytest
import datetime
import subprocess
import sys

def run_tests():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"test_results_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "test_string_utils.py", "-v"
        ], stdout=f, stderr=subprocess.STDOUT, text=True)
    
    print(f"Результаты тестов сохранены в файл: {filename}")

if __name__ == "__main__":
    run_tests()
