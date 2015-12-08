/*SELECT column_name,column_name
FROM table_name
WHERE column_name operator value;*/

SELECT * FROM meetups WHERE StartTime > '2015/12/01 10:00:00';
SELECT Id,StartTime,Location,Description FROM meetups WHERE Topic LIKE '%bile%';
SELECT * FROM users WHERE Avatar='valve';
SELECT * FROM statuses WHERE Val='Going';
SELECT StatusId,MeetupsId,UsersId FROM meetupregistrations WHERE Id IS NOT NULL;
