CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "email" varchar,
  "phone_number" varchar(12),
  "role" varchar
);

CREATE TABLE "masters" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "email" varchar,
  "phone_number" varchar(12),
  "work_schedule" bit(31),
  "content_id" integer

);

CREATE TABLE "services" (
  "name" varchar(50) PRIMARY KEY,
  "type" varchar(20),
  "cost" integer,
  "content_id" integer
);

CREATE TABLE "appointments" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "master_id" integer,
  "service_name" varchar(20),
  "date_time" datetime,
  "extra" text
);

CREATE TABLE "content" (
  "id" integer PRIMARY KEY,
  "target_name" varcher,
  "page" varchar,
  "type" varchar,
  "extra" text
);

CREATE TABLE "mastersService" (
  "master_id" integer,
  "service_name" varchar(20),
  PRIMARY KEY ("master_id", "service_name")
);

COMMENT ON COLUMN "users"."role" IS 'client or admin';

COMMENT ON COLUMN "appointments"."extra" IS 'additional customer requests';

COMMENT ON COLUMN "content"."target_name" IS 'service name or master email';

COMMENT ON COLUMN "content"."type" IS 'text or img';

COMMENT ON COLUMN "content"."extra" IS 'conent text or img link';

ALTER TABLE "appointments" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "appointments" ADD FOREIGN KEY ("master_id") REFERENCES "masters" ("id");

ALTER TABLE "appointments" ADD FOREIGN KEY ("service_name") REFERENCES "services" ("name");

ALTER TABLE "content" ADD FOREIGN KEY ("target_name") REFERENCES "masters" ("name");

ALTER TABLE "content" ADD FOREIGN KEY ("target_name") REFERENCES "services" ("name");

ALTER TABLE "mastersService" ADD FOREIGN KEY ("master_id") REFERENCES "masters" ("id");

ALTER TABLE "mastersService" ADD FOREIGN KEY ("service_name") REFERENCES "services" ("name");
