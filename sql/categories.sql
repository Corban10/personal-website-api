CREATE TABLE "categories"
(
	"id" serial NOT NULL UNIQUE PRIMARY KEY,
	"name" text NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	"updated_at" TIMESTAMP
)