CREATE TABLE public.blog
(
	"id" serial NOT NULL UNIQUE PRIMARY KEY,
	"content" text NOT NULL,
    "image" bytea,
	"slug" varchar(30) NOT NULL,
	"category_id" serial REFERENCES public.categories (id),
	"desc" text NOT NULL,
	"date" date NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	"updated_at" TIMESTAMP
)