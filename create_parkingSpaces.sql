CREATE TABLE "parkingSpaces" (
	"entry"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Identifier"	INTEGER,
	"available_spaces" INTEGER,
	"update_time" TEXT,
	"entry_time" TEXT,	
	FOREIGN KEY("Identifier") REFERENCES CarParks("Identifier")	
);
