from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "movies" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(225) NOT NULL,
    "overview" TEXT,
    "runtime" INT,
    "release_date" TIMESTAMPTZ,
    "genres" JSONB,
    "poster_path" VARCHAR(300),
    "backdrop_path" VARCHAR(300)
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "password" VARCHAR(128),
    "points" INT NOT NULL  DEFAULT 0,
    "yellow_cards" INT   DEFAULT 0,
    "red_cards" INT   DEFAULT 0,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "moviereviews" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "score" INT NOT NULL,
    "comment" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "author_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "movie_id" INT NOT NULL REFERENCES "movies" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "reviews" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(225) NOT NULL,
    "content" TEXT NOT NULL,
    "type" VARCHAR(30),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "author_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
