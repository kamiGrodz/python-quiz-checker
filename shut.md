import os

def main():
    selected_time = input("Enter the number of seconds to shutdown: ")
    prepared_command = "shutdown /s /f /t " + selected_time
    os.system(prepared_command)
    print("System will shutdown in:", selected_time)

if __name__ == "__main__":
    main()
