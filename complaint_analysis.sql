-- 1. Total Complaints
SELECT COUNT(*) AS Total_Complaints
FROM Complaints;


-- 2. Complaints by Issue Category
SELECT Issue_Category,
       COUNT(*) AS Complaint_Count
FROM Complaints
GROUP BY Issue_Category
ORDER BY Complaint_Count DESC;


-- 3. Complaints by Priority
SELECT Priority_Level,
       COUNT(*) AS Complaint_Count
FROM Complaints
GROUP BY Priority_Level
ORDER BY Complaint_Count DESC;


-- 4. Average Resolution Time by Category
SELECT Issue_Category,
       ROUND(AVG(Resolution_Time_Hours), 2) AS Avg_Resolution_Hours
FROM Complaints
GROUP BY Issue_Category
ORDER BY Avg_Resolution_Hours DESC;


-- 5. Average Satisfaction by Category
SELECT Issue_Category,
       ROUND(AVG(Satisfaction_Score), 2) AS Avg_Satisfaction
FROM Complaints
GROUP BY Issue_Category
ORDER BY Avg_Satisfaction DESC;


-- 6. Complaints by Channel
SELECT Ticket_Channel,
       COUNT(*) AS Complaint_Count
FROM Complaints
GROUP BY Ticket_Channel
ORDER BY Complaint_Count DESC;


-- 7. Sentiment by Issue Category
SELECT Issue_Category,
       NLP_Sentiment,
       COUNT(*) AS Complaint_Count
FROM Complaints
GROUP BY Issue_Category, NLP_Sentiment
ORDER BY Issue_Category, Complaint_Count DESC;