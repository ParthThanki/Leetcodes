# Write your MySQL query statement below

SELECT Visits.customer_id, COUNT(ISNULL(Transactions.transaction_id)) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Transactions.visit_id = Visits.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id