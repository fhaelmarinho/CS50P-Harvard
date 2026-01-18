def main():
    now_time = input("What time's it? ").strip()

    # call function
    time = convert(now_time)

    # breakfast 7:00 and 8:00
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    # lunch 12:00 and 13:00
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    #dinner 18:00 and 19:00
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    # Get hour and minute

    hours, minutes = time.split(":")

    # Avoid minutes > 59 and convert time into a float number
    minutes = int(minutes)
    if 0 <= minutes <= 59:
        time = float(hours)+float(minutes)/60

    # Return the result
    return time

if __name__ == "__main__":
    main()
