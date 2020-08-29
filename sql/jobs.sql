CREATE TABLE "jobs"
(
	"id" serial NOT NULL UNIQUE PRIMARY KEY,
	"company" varchar(50) NOT NULL,
    "position" varchar(50) NOT NULL,
	"date" date NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	"updated_at" TIMESTAMP
)