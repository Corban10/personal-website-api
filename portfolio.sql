BEGIN;
--
-- Create model Category
--
CREATE TABLE "portfolio_category" (
  "id" serial NOT NULL PRIMARY KEY, 
  "name" varchar(50) NOT NULL, 
  "created_at" timestamp with time zone NOT NULL, 
  "updated_at" timestamp with time zone NOT NULL
);
--
-- Create model Job
--
CREATE TABLE "portfolio_job" (
  "id" serial NOT NULL PRIMARY KEY, 
  "company" varchar(50) NOT NULL, 
  "position" varchar(50) NOT NULL, 
  "date_start" date NULL, 
  "date_end" date NULL, 
  "created_at" timestamp with time zone NOT NULL, 
  "updated_at" timestamp with time zone NOT NULL
);
--
-- Create model Project
--
CREATE TABLE "portfolio_project" (
  "id" serial NOT NULL PRIMARY KEY, 
  "description" text NOT NULL, 
  "image" bytea NULL, 
  "github" varchar(50) NOT NULL, 
  "url" varchar(50) NOT NULL, 
  "featured" boolean NOT NULL, 
  "date" date NULL, 
  "created_at" timestamp with time zone NOT NULL, 
  "updated_at" timestamp with time zone NOT NULL
);
--
-- Create model BlogPost
--
CREATE TABLE "portfolio_blogpost" (
  "id" serial NOT NULL PRIMARY KEY, 
  "content" text NOT NULL, 
  "image" bytea NULL, 
  "slug" varchar(50) NOT NULL, 
  "desc" text NOT NULL, 
  "date" date NOT NULL, 
  "created_at" timestamp with time zone NOT NULL, 
  "updated_at" timestamp with time zone NOT NULL, 
  "category_id" integer NOT NULL
);
ALTER TABLE 
  "portfolio_blogpost" 
ADD 
  CONSTRAINT "portfolio_blogpost_category_id_ac329b0b_fk_portfolio" FOREIGN KEY ("category_id") REFERENCES "portfolio_category" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "portfolio_blogpost_category_id_ac329b0b" ON "portfolio_blogpost" ("category_id");
COMMIT;
