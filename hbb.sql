CREATE DATABASE IF NOT EXISTS homelessBeatingBot;
-- create a database named "homelessBeatingBot if it hasn't exist"
USE homelessBeatingBot;
-- select and use the "homelessBeatingBot" database
SELECT DATABASE();
-- print the current database to make sure it is "homelessBeatingBot"
-- I don't know how to use IF in SQL yet so actually this is kinda pointless in actual running, but it is good for testing step by step

CREATE TABLE IF NOT EXISTS tb_user (discordID VARCHAR(100));
-- create the `user` table for storing basic user data
-- query for changing table name: ALTER TABLE tableName RENAME TO newTableName;
