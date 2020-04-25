USE master;
GO

CREATE DATABASE SampleDB;
GO

USE SampleDB;
GO

CREATE TABLE dbo.MyTable (id bigint IDENTITY(1,1) PRIMARY KEY, name varchar(500) null);
GO

INSERT INTO dbo.MyTable (name) VALUES ('Random text');
GO

RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/wwi.bak"

RESTORE DATABASE WideWorldImporters 
FROM DISK = "/var/opt/mssql/backup/wwi.bak" 
WITH MOVE "WWI_Primary" TO "/var/opt/mssql/data/WideWorldImporters.mdf", 
MOVE "WWI_UserData" TO "/var/opt/mssql/data/WideWorldImporters_userdata.ndf", 
MOVE "WWI_Log" TO "/var/opt/mssql/data/WideWorldImporters.ldf", 
MOVE "WWI_InMemory_Data_1" TO "/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1"