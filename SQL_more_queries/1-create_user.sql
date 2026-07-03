-- Creates the MYSQL user user_0d_1 and user_0d_2
CREATE user IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grants user all privileges 
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applies changes
FLUSH PRIVILEGES;

