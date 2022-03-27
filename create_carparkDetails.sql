CREATE TABLE IF NOT EXISTS "carPark_details" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"identifier"	INTEGER UNIQUE,
	"carpark_name"	TEXT NOT NULL UNIQUE,
	"total_spaces"	INTEGER,
	"latitude"	REAL,
	"longitude"	REAL,
	"price"	TEXT,
	"heightRestriction_metres"	REAL,
	"Monday_Open" TEXT,   
	"Monday_Close" TEXT,  
	"Tuesday_Open" TEXT,   
	"Tuesday_Close" TEXT,  
	"Wednesday_Open" TEXT,   
	"Wednesday_Close" TEXT,  
	"Thursday_Open" TEXT,   
	"Thursday_Close" TEXT,  
	"Friday_Open" TEXT,   
	"Friday_Close" TEXT,  
	"Saturday_Open" TEXT,   
	"Saturday_Close" TEXT,  
	"Sunday_Open" TEXT,   
	"Sunday_Close" TEXT 
);

INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('1', 'Paul Street', '749', '51.900542', '-8.475415', '€2.30 per hour; Flat rate €3.50 from 18.30-24.00', '2', '07:30:00', '23:59:00', '07:30:00', '23:59:00', '07:30:00', '23:59:00', '07:30:00', '23:59:00', '07:30:00', '23:59:00', '07:30:00', '23:59:00', '11:30:00', '23:59:00');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('2', 'North Main Street', '330', '51.901008', '-8.477804', '€1.70 per hour; Flat rate €2.00 from 18.30-21.30', '2', '07:30:00', '21:30:00', '07:30:00', '21:30:00', '07:30:00', '21:30:00', '07:30:00', '21:30:00', '07:30:00', '21:30:00', '07:30:00', '21:30:00', '11:30:00', '21:30:00');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('9', 'Black Ash Park & Ride', '935', '51.878279', '-8.466956', '€5 per day', '2.1', '06:45:00', '20:00:00', '06:45:00', '20:00:00', '06:45:00', '20:00:00', '06:45:00', '20:00:00', '06:45:00', '20:00:00', '06:45:00', '20:00:00', 'Closed', 'Closed');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('103', 'City Hall - Eglington Street', '436', '51.896579', '-8.464302', '€2.90 per hour, max. €13 per day', '2', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('102', 'Carrolls Quay', '376', '51.901788', '-8.472013', '€2.80 per hour', '2', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('101', 'Grand Parade', '352', '51.896562', '-8.474557', '€3 per hour', '1.85', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('108', 'Merchants Quay', '710', '51.8995765', '-8.4686481', '€3 per hour', '1.98', '08:00:00', '19:00:00', '08:00:00', '19:00:00', '08:00:00', '19:00:00', '08:00:00', '19:00:00', '08:00:00', '21:00:00', '08:00:00', '19:00:00', '12:00:00', '18:00:00');
INSERT INTO carPark_details ('identifier', 'carpark_name', 'total_spaces', 'latitude', 'longitude', 'price', 'heightRestriction_metres', 'Monday_Open', 'Monday_Close', 'Tuesday_Open', 'Tuesday_Close', 'Wednesday_Open', 'Wednesday_Close', 'Thursday_Open', 'Thursday_Close', 'Friday_Open', 'Friday_Close', 'Saturday_Open', 'Saturday_Close', 'Sunday_Open', 'Sunday_Close') VALUES ('104', "Saint Finbarr's", '350', '51.896723', '-8.482056', '€2.80 per hour', '2', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never', 'Always', 'Never');

