# Credit Risk & Loan Portfolio Analysis

## 1. About the Project

This project focuses on analyzing loan applications and understanding credit risk.

I used Lending Club loan data to analyze loan amount, interest rate, income, loan grade, loan purpose, employment length and loan status.

The project was completed using Python, SQL and Power BI.

The main goal was to understand loan performance, identify patterns in loan defaults and find which types of loans or borrowers have higher risk.

## 2. Dataset

This project uses two datasets:

- Accepted Loans – contains information about approved loans and their loan status.
- Rejected Loans – contains information about loan applications that were rejected.

The accepted loan dataset contains data from 2007 to 2018.

Dataset Source: Lending Club Loan Data – Kaggle


## 3. Tools & Technologies

- Python
- Pandas
- NumPy
- SQL (MySQL)
- Power BI
- Power Query
- DAX


---

## 4. Project Workflow

I completed the project in three main stages:

### Step 1 – Python Analysis

First, I used Python to understand and explore the dataset.

I performed:

- Data size and structure analysis
- Data type checking
- Missing value analysis
- Duplicate checking
- Loan status analysis
- Loan amount analysis
- Interest rate analysis
- Income analysis
- Default rate analysis
- Loan grade analysis
- Loan purpose analysis
- Employment length analysis
- Loan term analysis
- Accepted vs rejected application analysis
- Year-wise loan analysis

Libraries used:

- Pandas
- NumPy

### Step 2 – SQL Analysis

After understanding the data using Python, I used MySQL to perform further analysis.

I used SQL to:

- Filter loan records
- Group loans by different categories
- Calculate loan and customer metrics
- Analyze default rates
- Compare loan grades
- Analyze loan purposes
- Analyze loan terms
- Analyze loan performance by year
- Find high-risk loan segments
- Use joins to combine related tables
- Use CTEs and subqueries for more complex analysis
- Use window functions for ranking and comparisons

The SQL analysis was mainly focused on answering business questions related to loan risk and portfolio performance.

### Step 3 – Power BI Dashboard

Finally, I used Power BI to present the analysis in an interactive dashboard.

I used:

- Power Query for data cleaning and transformation
- DAX for calculated measures
- Power BI visuals for analysis
- Slicers and filters for interactive analysis

The dashboard focuses on:

- Loan portfolio overview
- Loan applications
- Loan amount
- Loan status
- Default rate
- Interest rate
- Loan grade
- Loan purpose
- Loan term
- Risk analysis
- Year-wise loan trends


## 5. Key Business Questions

The project was built around questions such as:

- How many loan applications were accepted and rejected?
- What is the overall default rate?
- Which loan grades have higher default rates?
- Which loan purposes have higher risk?
- Does loan term affect default rate?
- Does loan amount affect default risk?
- How does income relate to loan defaults?
- Which employment groups have higher default rates?
- Which loan grades have higher interest rates?
- How has loan performance changed over the years?
- Which loan segments are high risk?
- How do accepted and rejected applicants differ?

## 6. Key Findings

Some important findings from the analysis include:

- Default rates vary across different loan grades.
- Interest rates are different across loan grades and loan purposes.
- Loan purpose has an impact on the observed default rate.
- Different loan amount groups show different levels of default risk.
- Loan term also shows differences in default rates.
- Borrower income and employment characteristics show different risk patterns.
- Loan portfolio size and loan amount changed over different years.
- Accepted and rejected applications have different applicant profiles.
- Some combinations of loan grade, purpose and term show higher risk than others.

## 7. SQL Concepts Used

The SQL part of the project includes:

- SELECT
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- CASE WHEN
- Aggregate functions
- Joins
- Subqueries
- CTEs
- Window functions
- Date functions
- String functions

## 8. Python Concepts Used

The Python analysis includes:

- Pandas DataFrames
- Reading CSV files
- Data type analysis
- Missing value analysis
- Duplicate checking
- Boolean filtering
- groupby()
- value_counts()
- mean()
- median()
- min()
- max()
- sort_values()
- isin()
- NumPy conditions
- np.where()
- np.select()
- Date conversion
- Year-wise analysis


## 9. Power BI Concepts Used

The Power BI part includes:

- Power Query
- Data cleaning
- Data transformation
- Data modeling
- Relationships
- DAX measures
- KPIs
- Charts
- Slicers
- Filters
- Interactive dashboard


## 10. What I Learned

Through this project, I learned how to work with a large real-world dataset and analyze it using different tools.

I practiced:

- Understanding a new dataset before starting analysis
- Checking data quality
- Working with missing values and duplicates
- Performing analysis using Python
- Writing SQL queries for business questions
- Creating calculated measures using DAX
- Building an interactive Power BI dashboard
- Finding patterns related to credit risk
- Turning data analysis into useful business insights

## 12. Conclusion

This project helped me understand how Python, SQL and Power BI can be used together for a complete data analytics project.

Python was used for initial data exploration and analysis, SQL was used for deeper data analysis and business questions, and Power BI was used to present the final analysis through an interactive dashboard.

