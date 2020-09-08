import time
import datetime
import json
import os

file_path = "time.txt"
config_path = "config.json"


def main():
    time_format = "%H:%M:%S"
    if os.path.exists(config_path):
        with open("config.json") as f:
            j = json.load(f)
            time_format = j.get("time_format", "%H:%M:%S")
            print("Loaded {} - set time format to: '{}'".format(config_path, time_format))
    else:
        print("{} file could not be found. Setting default format to '{}'".format(config_path, time_format))
        # Write default config file
        with open(config_path, "w") as f:
            json.dump({"time_format": time_format}, f)

    formatted_time = ""
    while 1:
        my_time = datetime.datetime.now()
        # print(my_time)

        # Format time https://www.w3schools.com/python/python_datetime.asp
        time_string = my_time.strftime(time_format)
        if formatted_time != time_string:
            formatted_time = time_string
            with open(file_path, "w") as f:
                f.write(formatted_time)
            # print(time_string)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
