CREATE TABLE IF NOT EXISTS "faculty" (
	"id"	INTEGER NOT NULL,
	"name"	varchar(255) NOT NULL,
	"stats"	tinyint(1) DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT)
);