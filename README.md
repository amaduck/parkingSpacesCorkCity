# parkingSpacesCorkCity
app to show spaces available in Cork City car parks

* Link to data has changed, format seems the same, but change doesn't seem to be complete - no update since yesterday - need to update when complete

This is developed with three python learning goals in mind:
1) Pulling data from internet sources
2) Executing sqlite commands from code
3) Improving GUI skills

The application uses a dataset from data.corkcity.ie to show how many available spaces Cork city car parks currently have

In reality this would be more useful as a mobile app, but the purpose is to get better with python

A database isn't really necessary for this - adding one mainly for the experience. Should allow addition of trends (filling, emptying, steady)

Currently:
- App checks if database tables exists, creates them if not
- Pulls the current data CSV from the url http://data.corkcity.ie/datastore/dump/6cc1028e-7388-4bc5-95b7-667a59aa76dc. Exits if it can't access
- Checks the CSV file has the expected format and info
- Added pop up warnings if stored car park data (price, opening hours, total spaces) changes
- Populates a GUI screen with available spaces, and time of data
- Checks whether or not car park is currently open, displays on GUI
- Updates every 5 minutes (hardcoded value)


# Issue with daylight savings time
The CSV files come with a datetime value for the data - we rolled into summer time last night, but only one of the times has definitely updated (Black Ash), and one potentially (Merchant's Quay). The others are still on old time - need to consider how to handle. Presumably other times will update during the week. Will affect "updated at" - an update could be from 5 mins ago, but showing as 1:05 ago

# Goals:
1) Currently updates every x seconds, interval hardcoded - want to provide option to set interval in GUI, and preserve it across runs
2) Want to provide the option to only update when clicked on either
3) Improve GUI
4) Add percentage - 66% full, etc
5) Add a trend - filling up, emptying out
6) Change Updated at to eg updated 5 mins ago, 10 mins ago, 1 hour ago, ( >12 hours add a warning, stale data)

