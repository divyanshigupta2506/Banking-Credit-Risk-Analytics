
#How many total loans are present in the dataset?
SELECT COUNT(*)
FROM banking.accepted;

#How many unique loan IDs are present in the dataset?
SELECT COUNT(DISTINCT id)
FROM banking.accepted;

#Display all unique loan statuses available in the dataset.
SELECT distinct(loan_status)
FROM banking.accepted;

#Find the number of loans for each loan status.
SELECT loan_status, COUNT(id)
FROM banking.accepted
GROUP BY loan_status;

#Find the total loan amount issued by the company.
SELECT SUM(loan_amnt)
FROM banking.accepted;

#Find the average loan amount.
SELECT avg(loan_amnt)
FROM banking.accepted;

#Find the minimum and maximum loan amount.
SELECT MIN(loan_amnt),MAX(loan_amnt)
FROM banking.accepted;

#Find the total number of loans for each loan grade.
SELECT grade, COUNT(id)
FROM banking.accepted
GROUP BY grade;

#Find the average interest rate for each loan grade.
SELECT grade, AVG(int_rate)
FROM banking.accepted
GROUP BY grade;

#Which loan grade has the highest average interest rate?
SELECT grade, AVG(int_rate) AS avgintrest_rate
FROM banking.accepted
GROUP BY grade
ORDER BY avgintrest_rate desc
LIMIT 1;

# Find the total loan amount for each loan grade.
SELECT SUM(loan_amnt) AS total_loan_amnt, grade
FROM banking.accepted
GROUP BY grade;

#Find the average annual income for each loan grade.
SELECT AVG(annual_inc) AS total_annual_inc, grade
FROM banking.accepted
GROUP BY grade;

#Find the number of loans for each loan purpose
SELECT  COUNT(id) AS loan_number, purpose
FROM banking.accepted
GROUP BY purpose;

#Find the average interest rate for each loan purpose.
SELECT  AVG(int_rate) AS intrest_rate, purpose
FROM banking.accepted
GROUP BY purpose;

#Find the total loan amount for each loan purpose.
SELECT  SUM(loan_amnt) AS loan_amnt, purpose
FROM banking.accepted
GROUP BY purpose;

#Find the number of loans for each home ownership category.
SELECT COUNT(id) AS total_loan , home_ownership
FROM banking.accepted
GROUP BY home_ownership;

#Find the average loan amount for each loan status.
SELECT loan_status, AVG(loan_amnt) AS avg_loan_amount
FROM banking.accepted
GROUP BY loan_status;

#Find the number of Charged Off and Default loans.
SELECT loan_status, COUNT(id) AS total_loans
FROM banking.accepted
WHERE loan_status IN ("Default", "Charged Off")
GROUP BY loan_status;


#Find the default rate across the entire portfolio.
SELECT 
    COUNT(
        CASE 
            WHEN loan_status IN ('Charged Off', 'Default')
            THEN 1
        END
    ) * 100.0 / COUNT(*) AS default_rate
FROM banking.accepted;

#Default Rate for Each Loan Grade
SELECT 
    grade,
    COUNT(
        CASE 
            WHEN loan_status IN ('Charged Off', 'Default')
            THEN 1
        END
    ) * 100.0 / COUNT(*) AS default_rate
FROM banking.accepted
GROUP BY grade
ORDER BY default_rate DESC;








#Default Rate by Loan Purpose
SELECT 
    purpose,
    COUNT(
        CASE 
            WHEN loan_status IN ('Charged Off', 'Default')
            THEN 1
        END
    ) * 100.0 / COUNT(*) AS default_rate
FROM banking.accepted
GROUP BY purpose
ORDER BY default_rate DESC;


#Default Rate by Home Ownership
SELECT 
    home_ownership,
    COUNT(
        CASE 
            WHEN loan_status IN ('Charged Off', 'Default')
            THEN 1
        END
    ) * 100.0 / COUNT(*) AS default_rate
FROM banking.accepted
GROUP BY home_ownership
ORDER BY default_rate DESC;

#High Interest Rate Loans
SELECT COUNT(*) AS high_interest_loans
FROM banking.accepted
WHERE int_rate > 15;


#Find the number of loans where loan_amnt is greater than 20,000.
SELECT  COUNT(*) AS numer_loan 
FROM banking.accepted
WHERE  loan_amnt > 20000;

#For each loan grade, find the number of loans where the interest rate is greater than 15%.
SELECT 
    grade,
    COUNT(*) AS high_interest_loans
FROM banking.accepted
WHERE int_rate > 15
GROUP BY grade;

#Find loan grades where average interest rate > 12%.
SELECT 
    grade,
    AVG(int_rate) AS avg_interest_rate
FROM banking.accepted
GROUP BY grade
HAVING AVG(int_rate) > 12
ORDER BY avg_interest_rate DESC;

#Find loan purposes having more than 10,000 loans.
SELECT 
    purpose,
    COUNT(*) AS loan_count
FROM banking.accepted
GROUP BY purpose
HAVING COUNT(*) > 10000
ORDER BY loan_count DESC;

#Find all loans where loan_amnt is greater than the overall average loan amount.  
SELECT 
    id,
    loan_amnt
FROM banking.accepted
WHERE loan_amnt > (
    SELECT AVG(loan_amnt)
    FROM banking.accepted
);

# loan grades whose average interest rate is higher than the overall average interest rate of the entire portfolio.
SELECT 
    grade,
    AVG(int_rate) AS avg_interest_rate
FROM banking.accepted
GROUP BY grade
HAVING AVG(int_rate) > (
    SELECT AVG(int_rate)
    FROM banking.accepted
)
ORDER BY avg_interest_rate DESC;

#Default Loans
WITH default_loan AS(
SELECT grade,loan_status
FROM  banking.accepted 
WHERE loan_status IN ('Charged Off', 'Default')
)
SELECT  grade ,COUNT(*) AS default_loans
FROM default_loan
GROUP BY grade;

#Rank loan grades based on their total loan amount.
SELECT 
    grade,
    SUM(loan_amnt) AS total_loan_amount,
    RANK() OVER (
        ORDER BY SUM(loan_amnt) DESC
    ) AS grade_rank
FROM banking.accepted
GROUP BY grade
ORDER BY grade_rank;

#Calculate the default rate for each loan purpose and rank the purposes from highest default rate to lowest.
WITH purpose_default AS (
    SELECT 
        purpose,
        COUNT(
            CASE 
                WHEN loan_status IN ('Charged Off', 'Default')
                THEN 1
            END
        ) * 100.0 / COUNT(*) AS default_rate
    FROM banking.accepted
    GROUP BY purpose
)
SELECT purpose, default_rate,
    RANK() OVER (ORDER BY default_rate DESC) AS risk_rank
FROM purpose_default
ORDER BY risk_rank;

# top 5 loan purposes based on total loan amount.
SELECT purpose, SUM(loan_amnt) AS total_loan_amount,
     RANK()OVER(ORDER BY  SUM(loan_amnt)  desc) AS loan_rank
FROM banking.accepted
group by purpose
ORDER BY loan_rank
LIMIT 5  ; 

#Top Loan Grade Within Each Purpose
WITH grade_amount AS (
    SELECT purpose,grade,
        SUM(loan_amnt) AS total_loan_amount,
        ROW_NUMBER() OVER (
            PARTITION BY purpose
            ORDER BY SUM(loan_amnt) DESC
        ) AS rnk
    FROM banking.accepted
    GROUP BY purpose, grade
)
SELECT purpose,grade,total_loan_amount
FROM grade_amount
WHERE rnk = 1
ORDER BY purpose;

#Running Total of Loan Amount
WITH yearly_loans AS (
    SELECT 
        RIGHT(TRIM(issue_d), 4) AS year,
        SUM(loan_amnt) AS yearly_loan_amount
    FROM banking.accepted
    WHERE issue_d IS NOT NULL
    GROUP BY RIGHT(TRIM(issue_d), 4)
)
SELECT year,yearly_loan_amount,
    SUM(yearly_loan_amount) OVER (ORDER BY year) AS running_total
FROM yearly_loans
ORDER BY year;

#Year-over-Year Loan Amount
WITH yearly_loans AS (
    SELECT 
        RIGHT(TRIM(issue_d), 4) AS year,
        SUM(loan_amnt) AS yearly_loan_amount
    FROM banking.accepted
    WHERE issue_d IS NOT NULL
    GROUP BY RIGHT(TRIM(issue_d), 4)
)
SELECT yearly_loan_amount,year,
LAG(yearly_loan_amount) OVER(order by year)  AS previous_year_amount
FROM yearly_loans
ORDER BY year;

#Year-over-Year Growth %
WITH yearly_loans AS (
    SELECT 
        RIGHT(TRIM(issue_d), 4) AS year,
        SUM(loan_amnt) AS yearly_loan_amount
    FROM banking.accepted
    WHERE issue_d IS NOT NULL
    GROUP BY RIGHT(TRIM(issue_d), 4)
),
yearly_comparison AS (
    SELECT
        year,
        yearly_loan_amount,
        LAG(yearly_loan_amount) OVER (
            ORDER BY year
        ) AS previous_year_amount
    FROM yearly_loans
)
SELECT
    year,
    yearly_loan_amount,
    previous_year_amount,
    (yearly_loan_amount - previous_year_amount)
        / previous_year_amount * 100 AS yoy_growth
FROM yearly_comparison
ORDER BY year;

#Highest Risk Grade
WITH grade_analysis AS (
    SELECT grade,
        COUNT(
            CASE
                WHEN loan_status IN ('Charged Off', 'Default') THEN 1 END ) AS default_loans,
        COUNT(*) AS total_known_outcome_loans
    FROM banking.accepted
    WHERE loan_status IN ('Fully Paid', 'Charged Off', 'Default')
    GROUP BY grade
)
SELECT
    grade, default_loans * 100.0 / total_known_outcome_loans AS default_rate
FROM grade_analysis
ORDER BY default_rate DESC
LIMIT 1;

#High-Risk Loan Segment
WITH High_risk AS (
    SELECT grade,purpose,term,COUNT(*) AS total_loans,
        COUNT(
            CASE 
                WHEN loan_status IN ('Charged Off', 'Default') THEN 1 END) AS default_loans
    FROM banking.accepted
    WHERE loan_status IN ('Fully Paid', 'Charged Off', 'Default')
    GROUP BY grade, purpose, term
)
SELECT grade,purpose,term,total_loans,default_loans,
    (default_loans * 100.0 / total_loans) AS default_rate
FROM High_risk 
WHERE total_loans >= 100
ORDER BY default_rate DESC
LIMIT 10;

#"Which loan grades should we consider highest risk based on both default rate and interest rate?"
WITH grade_analysis AS (
    SELECT 
        grade,
        AVG(int_rate) AS avg_interest_rate,
        COUNT(
            CASE
                WHEN loan_status IN ('Charged Off', 'Default') THEN 1
            END
        ) AS default_loans,
        COUNT(*) AS total_known_outcome_loans
    FROM banking.accepted
    WHERE loan_status IN ('Fully Paid', 'Charged Off', 'Default')
    GROUP BY grade
)
SELECT
    grade,
    default_loans * 100.0 / total_known_outcome_loans AS default_rate,
    avg_interest_rate
FROM grade_analysis
ORDER BY default_rate DESC, avg_interest_rate DESC
LIMIT 1;


