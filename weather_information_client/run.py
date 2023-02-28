from process import *
from config import * 
def main():
    process = Process(server_ip)
    process.RunRecipe()
if __name__ == '__main__':
    main()