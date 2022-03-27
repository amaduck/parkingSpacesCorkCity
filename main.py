# App to show how many spaces free in city car parks - ideally updates regularly

# Based on this data:
# https://data.gov.ie/dataset/parking/resource/6cc1028e-7388-4bc5-95b7-667a59aa76dc
# http://data.corkcity.ie/datastore/dump/6cc1028e-7388-4bc5-95b7-667a59aa76dc
# CSV file gives following data:
# _id	identifier	name	spaces	free_spaces	opening_times	notes	latitude	longitude	date	price	height_restrictions

"""
To do

Make GUI
Add check for price change - display pop-up
Add check for opening hours change - display pop-up
Add not updating warning if update_time old

Is a database really necessary? - over a long period it would allow you to idenfity busy times?
Could use it to show trends? Filling up, emptying out? Steady if change in last 3 calls within +/-5, etc

"""

# Imports
import datetime
import sys
import time
import csv
import urllib.request
import sqlite3
from contextlib import closing
import tkinter
import tkinter.messagebox
from tkinter import *

# Values to check against
expected_headings = ['_id', 'identifier', 'name', 'spaces', 'free_spaces', 'opening_times', 'notes', 'latitude',
                     'longitude', 'date', 'price', 'height_restrictions']
expected_ids = ["1", "2", "9", "103", "102", "101", "108", "104"]
expected_opening = ["Monday - Saturday 07.30 -00.00, Sunday 11.30 - 00.00",
                    "Monday - Saturday 07.30 - 21.30, Sunday 11.30 - 21.30", "Monday - Saturday 06:45 - 20:00", "24/7",
                    "24/7", "24/7",
                    "Monday - Thursday and Saturday 08.00 - 19.00, Friday 08.00 - 21.00, Sunday 12.00 - 18.30", "24/7"]
expected_cost = ["€2.30 per hour; Flat rate €3.50 from 18.30-24.00", "€1.70 per hour; Flat rate €2.00 from 18.30-21.30",
                 "€5 per day", "€2.90 per hour, max. €13 per day", "€2.80 per hour", "€3 per hour", "€3 per hour",
                 "€2.80 per hour"]
expected_spaces = ["749", "330", "935", "436", "376", "352", "710", "350"]

# Constants
car_parks = ["Paul Street", "North Main Street", "Black Ash Park & Ride", "City Hall - Eglington Street",
             "Carrolls Quay", "Grand Parade", "Merchants Quay", "Saint Finbarr's"]
seconds_to_wait = 300
milliseconds_to_wait = seconds_to_wait * 1000
insert_command = "INSERT INTO parkingSpaces  ('identifier', 'available_spaces', 'update_time', 'entry_time' ) VALUES ("
day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
current_values = [["" for x in range(3)] for y in range(8)]  # 3 values per set, 8 sets

# TKInter elements
# Putting these outside functions so they can be accessed by all
appWindow = tkinter.Tk(screenName=None, baseName=None, className="Cork Car Parks", useTk=1)
appWindow.title("Cork Car Parks")
appWindow.geometry("600x400")
topFrame = Frame(appWindow)
buttons = Frame(appWindow)
topFrame.grid(row=0, column=0)
buttons.grid(row=30, column=0)


def check_tables():
    # connecting to database will create it if it doesn't exist
    # tables in db checked, and if not found, created by importing .sql script
    # Could also hardcode commands for table creation
    # In a system where people could edit the .sql, be a risk of executing malicious code
    db = sqlite3.connect('./corkCarParking.db')
    cursor = db.cursor()

    carPark_details_Found = False
    parkingSpaces_Found = False

    for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        row = row[0]
        if row == "parkingSpaces":
            print("parkingSpaces table exists")
            parkingSpaces_Found = True
        if row == "carPark_details":
            print("carPark_details table exists")
            carPark_details_Found = True

    if not carPark_details_Found:
        with open('create_carparkDetails.sql', 'r') as sql_file:
            print("creating and populating carPark_details table")
            sql_script = sql_file.read()
            cursor.executescript(sql_script)

    if not parkingSpaces_Found:
        with open('create_parkingSpaces.sql', 'r') as sql_file:
            print("creating parkingSpaces table")
            sql_script = sql_file.read()
            cursor.executescript(sql_script)

    db.commit()
    db.close()


def import_csv():
    # Pulls the CSV output from url mentioned
    # Calls check_csv_file to verify column headings, car park IDs, and number of car parks
    # If all in order, returns the csv data
    url = 'http://data.corkcity.ie/datastore/dump/6cc1028e-7388-4bc5-95b7-667a59aa76dc'
    try:
        CSV_data = urllib.request.urlopen(url)
    except:
        print("Can't access data source - check internet connection")
        tkinter.messagebox.showinfo("Error","Can't access data source - check internet connection")
        sys.exit()
    else:
        lines = [line.decode('utf-8') for line in CSV_data.readlines()]
        csv_rows = csv.reader(lines)

        if check_csv_file(csv.reader(lines))[0] != True:
            print("Oh shit")
            print(check_csv_file(csv.reader(lines))[1])
        else:
            return csv_rows


def check_csv_file(csv_rows):
    count = 0
    all_good = True
    message = ""
    for row in csv_rows:
        if count == 0:
            for heading in range(len(row)):
                if row[heading] != expected_headings[heading]:
                    all_good = False
                    message = message + "Headings don't match"
        else:
            # print(row[1], expected_ids[count - 1])
            if row[1] != expected_ids[count - 1]:
                all_good = False
                message = message + "\nIDs don't match"
            # Checks for changes to rates, total spaces, opening hours:
            if row[5] != expected_opening[count - 1]:
                print(row[2], "opening hours have changed", sep=" ")
            if row[10] != expected_cost[count - 1]:
                print(row[2], "cost has changed", sep=" ")
            if row[3] != expected_spaces[count - 1]:
                print(row[3], expected_spaces[count - 1])
                print(row[2], "total number of spaces has changed", sep=" ")
        count += 1

    if count > 9:
        all_good = False
        message = message + "\nMore car parks than expected"

    return (all_good, message)


def process_csv():
    csv_rows = import_csv()
    connection = sqlite3.connect("./corkCarParking.db")
    cursor = connection.cursor()

    count = 0
    for row in csv_rows:
        run_time = str(datetime.datetime.now())[0:19]
        if row[0] != '_id':
            carParkID = int(row[1])
            available_spaces = int(row[4])
            data_dateText = row[9]
            data_dateString = data_dateText[0:10] + " " + data_dateText[11:19]
            insert_string = insert_command + str(carParkID) + ", " + str(
                available_spaces) + ", '" + data_dateString + "', '" + run_time + "');"
            cursor.execute(insert_string)
            current_values[count - 1][0] = row[1]
            current_values[count - 1][1] = row[4]
            current_values[count - 1][2] = data_dateString
        count += 1

    connection.commit()
    print(connection.total_changes)

    with closing(sqlite3.connect("./corkCarParking.db")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
            print(rows)


def check_open():
    # Check if the car park is currently open
    # Either: Closed, open, closing within an hour
    day_today = datetime.datetime.now().isoweekday()
    day_name = day_names[day_today - 1]
    now_time = datetime.datetime.now().time()

    connection = sqlite3.connect("./corkCarParking.db")
    cursor = connection.cursor()
    for car_parks in range(8):
        req_opens_today = "Select " + day_name + "_Open from carPark_details where id = " + str(car_parks + 1)
        req_closes_today = "Select " + day_name + "_Close from carPark_details where id = " + str(car_parks + 1)
        opens_today = cursor.execute(req_opens_today).fetchone()[0]
        closes_today = cursor.execute(req_closes_today).fetchone()[0]
        open_now = ""
        if opens_today == "Always":
            open_now = "Open"
        elif opens_today == "Closed":
            open_now = "Closed"
        else:
            try:
                open_time = datetime.datetime.strptime(opens_today, '%H:%M:%S').time()
                close_time = datetime.datetime.strptime(closes_today, '%H:%M:%S').time()
                if open_time < now_time and close_time > now_time:
                    open_now = "Open"
                    time_until_close = datetime.datetime.combine(datetime.date.today(), close_time) - datetime.datetime.now()
                    if time_until_close.seconds < 3600:
                        open_now = "Closing Soon"
                else:
                    open_now="Closed"
            except:
                print("Unexpected time format")

        if open_now == "Open":
            bgColour = "#22f75e"
        elif open_now == "Closing Soon":
            bgColour = "#f78c22"
        else:
            bgColour = "Red"

        label = Label(topFrame, text=open_now, bg = bgColour, width=12, height=2).grid(row=car_parks+1, column=2)

    connection.close()


def draw_window():
    label = Label(topFrame, text="Car Park", width=23, height=2, anchor=W, relief=SUNKEN).grid(row=0, column=0)
    label = Label(topFrame, text="Available Spaces", width=15, height=2, relief=SUNKEN).grid(row=0, column=1)
    label = Label(topFrame, text="Open", width=12, height=2, relief=SUNKEN).grid(row=0, column=2)
    label = Label(topFrame, text="Updated at", width=18, height=2).grid(row=0, column=3)


    count = 0
    for car_park in car_parks:
        label = Label(topFrame, text=car_park, width=23, height=2, anchor=W, relief=SUNKEN).grid(row=count + 1, column=0)
        count += 1

    def update_details():
        # clock_label = Label(topFrame, text=time.strftime('%H:%M:%S'), width=10, height=2).grid(row=0, column=3)
        process_csv()
        check_open()
        for parks in range(8):
            label = Label(topFrame, text=current_values[parks][1], width=15, height=2, relief=SUNKEN).grid(row=parks + 1, column=1)
            label = Label(topFrame, text=current_values[parks][2], width=18, height=2, relief=SUNKEN).grid(row=parks + 1, column=3)
        # If I put the next command after an if(ms > 0):, it should run once
        topFrame.after(milliseconds_to_wait, update_details)


    checkNow_button = Button(buttons, text="Update Now", width=10, height=2).grid(row=1, column=1)
    interval_button = Button(buttons, text="Update at intervals", width=15, height=2).grid(row=1, column=10)
    exit_button = Button(buttons, text="Exit", width=10, height=2, command=sys.exit).grid(row=1, column=20)

    update_details()
    appWindow.mainloop()


def main():
    check_tables()
    process_csv()
    draw_window()


main()
