CREATE TABLE "blog_posts"
(
	"id" serial NOT NULL UNIQUE PRIMARY KEY,
	"content" text NOT NULL,
    "image" bytea,
	"slug" varchar(30) NOT NULL,
	"desc" text NOT NULL,
	"date" date NOT NULL,
	"category_id" serial,
	"created_at" TIMESTAMP NOT NULL,
	"updated_at" TIMESTAMP
)

ALTER TABLE "blog_posts"
  ADD CONSTRAINT "blog_post_category"
    FOREIGN KEY ("category_id")
    REFERENCES "blog_posts" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "blog_post_category_id" ON "blog_posts" ("category_id");
