from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "reviewtype" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(30) NOT NULL UNIQUE
);;
        ALTER TABLE "reviews" ADD "type_id" INT NOT NULL;
        ALTER TABLE "reviews" DROP COLUMN "type";
        ALTER TABLE "reviews" ADD CONSTRAINT "fk_reviews_reviewty_51a730cd" FOREIGN KEY ("type_id") REFERENCES "reviewtype" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "reviews" DROP CONSTRAINT "fk_reviews_reviewty_51a730cd";
        ALTER TABLE "reviews" ADD "type" VARCHAR(30);
        ALTER TABLE "reviews" DROP COLUMN "type_id";
        DROP TABLE IF EXISTS "reviewtype";"""
