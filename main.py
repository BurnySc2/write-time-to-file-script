import time
import datetime

file_path = "time.txt"


def main():
    formatted_time = ""
    while 1:
        my_time = datetime.datetime.now()
        # Remove microseconds part
        my_time = my_time - datetime.timedelta(microseconds=my_time.microsecond)
        # print(my_time)

        # Format time https://www.w3schools.com/python/python_datetime.asp
        time_string = my_time.strftime("%H:%M:%S")
        if formatted_time != time_string:
            formatted_time = time_string
            with open(file_path, "w") as f:
                f.write(formatted_time)
            # print(time_string)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
