# Write your MySQL query statement below
SELECT w1.machine_id, round(avg(w2.timestamp - w1.timestamp),3) as processing_time
FROM Activity w1
JOIN Activity w2 ON w1.process_id = w2.process_id AND w1.machine_id = w2.machine_id AND w1.timestamp < w2.timestamp
GROUP BY w1.machine_id, w2.machine_id

