# parkingSpacesCorkCity
app to show spaces available in Cork City car parks

This is developed with three python learning goals in mind:
1) Pulling data from internet sources
2) Executing sqlite commands from code
3) Improving GUI skills

The application uses a dataset from data.corkcity.ie to show how many available spaces Cork city car parks currently have

In reality this would be more useful as a mobile app, but the purpose is to get better with python

Currently:
- App checks if database tables exists, creates them if not
- Pulls the current data CSV from the url http://data.corkcity.ie/datastore/dump/6cc1028e-7388-4bc5-95b7-667a59aa76dc. Exits if it can't access
- Populates a GUI screen with available spaces, and time of data
- Updates every 5 minutes (hardcoded value)
- Checks whether or not car park is currently open, displays on GUI

Goals:
1) Currently updates every x seconds, interval hardcoded - want to provide option to set interval in GUI, and preserve it across runs
2) Want to provide the option to only update when clicked on either
3) Add pop up warnings if stored car park data (price, opening hours, height restriction) changes
4) Improve GUI
5) Add percentage - 66% full, etc
6) Add a trend - filling up, emptying out
7) Change Updated at to eg updated 5 mins ago, 10 mins ago, 1 hour ago, ( >12 hours add a warning, stale data)

