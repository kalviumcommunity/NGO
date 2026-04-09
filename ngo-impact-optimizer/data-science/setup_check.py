import sys

def check_environment():
    print("Python Version:", sys.version)
    
    try:
        import pandas
        print("Pandas is installed")
    except ImportError:
        print("Pandas is NOT installed")

    try:
        import numpy
        print("NumPy is installed")
    except ImportError:
        print("NumPy is NOT installed")

if __name__ == "__main__":
    check_environment()