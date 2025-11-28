-- Root user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGIES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGIES;
