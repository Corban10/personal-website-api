CREATE TABLE public.projects
(
	"id" serial NOT NULL UNIQUE PRIMARY KEY,
	"description" text NOT NULL,
    "image" bytea,
	"github" varchar(30) NOT NULL,
	"url" varchar(30) NOT NULL,
	"featured" boolean,
	"date" date NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	"updated_at" TIMESTAMP
)