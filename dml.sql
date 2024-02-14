-- ACTIONS / domain

-- USER ACTIONS
 -- public
-- 1. Client registration
SELECT COUNT(*) FROM clients -- проверить существует ли уже email или телефон
WHERE
 email = 'jd@example.host'
OR
 phone = '+12345678';
INSERT INTO clients VALUES(
 1,
 'John Doe',
 '+12345678',
 'jd@example.host',
 '123456'
);
INSERT INTO clients VALUES(
 2,
 'Marry Poppins',
 '+98765432',
 'mp@example.host',
 '654321'
);
-- 2. Client authentication (login)
SELECT * FROM clients
WHERE
 email = 'jd@example.host'
AND
 password = '123456'
AND
 active = true;
 -- authenticated аутентифицированный
-- 3. Client logout
-- 4. Client changes contact data
UPDATE clients
SET phone = '+3456789'
WHERE email = 'jd@example.host'
AND password = '123456';
-- 5. Client changes address data
-- 6. Client changes his password
-- HM1: update the password using email and old password as confirmation
UPDATE clients
SET password = '234567'
WHERE email = 'jd@example.host'
AND password = '123456';
-- 7. Client profile removal
DELETE FROM clients
WHERE email = 'jd@example.host'
AND password = '123456';
 -- admin
-- 8. block client
UPDATE clients
set active = false
WHERE email = 'jd@example.host';
-- 9. block client
-- HM2: unblock the client
UPDATE clients
set active = true
WHERE email = 'jd@example.host';
-- 10. send mass notification email / sms
-- APLICATION LAYER ACTIONS