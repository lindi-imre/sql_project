/*UPDATE Customers
SET ContactName='Alfred Schmidt', City='Hamburg'
WHERE CustomerName='Alfreds Futterkiste';*/

UPDATE meetups
SET Location = 'Miskolc, Codecool',Description = 'About most comfortable android,IOS,windows phone tools'
WHERE Id='4';

UPDATE meetups
SET Description = 'About most comfortable android,IOS,windows phone tools'
WHERE Id='1';

UPDATE users
SET Introduction='Counter-strike father'
WHERE Id='5';

UPDATE statuses
SET Val='Going'
WHERE Id = '2';