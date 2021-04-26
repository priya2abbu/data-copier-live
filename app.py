import sys;
from config import DB_DETAILS;
def main():
    env = sys.argv[1]
    DBdetails = DB_DETAILS[env]
    for arg in sys.argv:
        print(arg)

if __name__ == '__main__':
    main()