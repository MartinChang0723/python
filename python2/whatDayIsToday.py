from datetime import datetime

def dow(dstr):
  dateArr = dstr.split('/')
  return datetime(int(dateArr[0]), int(dateArr[1]), int(dateArr[2])).weekday()

def main():
    dateStr = input("Please input a date (YYYY/MM/YY) -- ")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(weekdays[ dow(dateStr) ])
if __name__ == "__main__":
  main()