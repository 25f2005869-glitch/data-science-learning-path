-- ==================================================
-- Author      : Saloni Tiwari
-- Program     : IITM BS in Data Science and Applications
-- Topic       : Transactions
-- Day         : 24
-- Description : BEGIN, COMMIT and ROLLBACK
-- ==================================================

DROP TABLE IF EXISTS accounts;

-- ==========================================
-- Create Accounts Table
-- ==========================================

CREATE TABLE accounts (
    account_id INTEGER,
    account_holder TEXT,
    balance INTEGER
);

INSERT INTO accounts VALUES (1,'Saloni',10000);
INSERT INTO accounts VALUES (2,'Rahul',5000);

-- ==========================================
-- Check Initial Data
-- ==========================================

SELECT * FROM accounts;

-- ==========================================
-- Transaction Example
-- Money Transfer
-- ==========================================

BEGIN TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 2;

COMMIT;

-- ==========================================
-- Check Updated Data
-- ==========================================

SELECT * FROM accounts;