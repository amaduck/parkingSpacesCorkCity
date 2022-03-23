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
expected_spaces = ["749","330","935","436","376","352","710","350"]

# Constants
car_parks = ["Paul Street","North Main Street","Black Ash Park & Ride","City Hall - Eglington Street","Carrolls Quay","Grand Parade","Merchants Quay","Saint Finbarr's"]
seconds_to_wait = 300
insert_command = "INSERT INTO parkingSpaces  ('identifier', 'available_spaces', 'update_time', 'entry_time' ) VALUES ("
# current_values = [["" for x in range(8)] for y in range(3)]


def import_csv():
    # Pulls the CSV output from url mentioned
    # Calls check_csv_file to verify column headings, car park IDs, and number of car parks
    # If all in order, returns the csv data
    url = 'http://data.corkcity.ie/datastore/dump/6cc1028e-7388-4bc5-95b7-667a59aa76dc'
    CSV_data = urllib.request.urlopen(url)
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
                print(row[3], expected_spaces[count-1])
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

    for row in csv_rows:
        run_time = str(datetime.datetime.now())[0:19]
        if row[0] != '_id':
            carParkID = int(row[1])
            available_spaces = int(row[4])
            data_dateText = row[9]
            data_dateString = data_dateText[0:10] + " " + data_dateText[11:19]
            insert_string = insert_command + str(carParkID) + ", " + str(available_spaces) + ", '" + data_dateString + "', '" + run_time + "');"
            cursor.execute(insert_string)

    connection.commit()
    print(connection.total_changes)

    with closing(sqlite3.connect("./corkCarParking.db")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
            print(rows)


def draw_window():
    appWindow = tkinter.Tk(screenName=None, baseName=None, className="Cork Car Parks", useTk=1)
    appWindow.title("Cork Car Parks")
    appWindow.geometry("450x400")

    details = Frame(appWindow)
    count = 0
    for car_park in car_parks:
        label = Label(details, text=car_park, width = 25, height = 2 ).grid(row = count, column = 0, sticky=tkinter.W)
        count += 1
    count = 0
    for spaces in expected_spaces:
        label = Label(details, text=spaces, width=5, height=2).grid(row=count, column=1, sticky=tkinter.W)
        count += 1


    buttons = Frame(appWindow)
    checkNow_button = Button(buttons, text="Update Now", width = 10, height = 2).grid(row=1, column =1)
    interval_button = Button(buttons, text="Update at intervals", width=15, height=2).grid(row=1, column =10)
    exit_button = Button(buttons, text= "Exit", width=10, height=2 , command=sys.exit).grid(row=1, column =20)

    details.grid(row=1, column=1)
    buttons.grid(row=30, column=1)

    # checkNow_button.grid(row=1, column =1)
    # interval_button.grid(row=1, column =10)
    # exit_button.grid(row=1, column =20)

    # ent = Entry(numberEntry, width=5, justify=tkinter.CENTER)
    # ent.grid(row=rowPos, column=colPos)
    # # combining previous 2 lines into single line (ie ent=Entry().grid()) causes error - not added to entries array
    # entries.append(ent)
    # # print("x: ",x ,"row: ", rowPos," y: ",y, "Col: ", colPos)
    #
    # btn = Button(numberEntry, text="Solve", width=10, height=5, command=get_numbers)
    # btn.place(x=170, y=275)

    appWindow.mainloop()

def main():
    draw_window()
    while True:
        process_csv()
        time.sleep(seconds_to_wait)


main()



