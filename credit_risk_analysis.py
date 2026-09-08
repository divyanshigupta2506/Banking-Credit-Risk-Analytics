
import pandas as pd
import numpy as np
accepted = pd.read_csv("C:\\Users\\divya\\Downloads\\accepted_2007_to_2018Q4.csv")
rejected = pd.read_csv("C:\\Users\\divya\\Downloads\\rejected_2007_to_2018Q4.csv")
df = accepted

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.isnull().mean()*100)
print("Column names:",df.columns)
df.info()
print(df.duplicated(subset="id").sum())
print(df["loan_status"].unique())
a=df["loan_amnt"].mean()
b=df["loan_amnt"].median()
c=df["loan_amnt"].min()
d=df["loan_amnt"].max()
print(a)
print(b)
print(c)
print(d)
loanstatus = df["loan_status"].value_counts()
print(loanstatus)

print(df.isnull().sum().sort_values(ascending=False).head(5))
print((df.isnull().mean()*100).sort_values(ascending=False).head(10))
print(df.duplicated(subset="id").sum())

print(df["grade"].unique())
Grade = df["grade"].value_counts()
print(Grade)

print(df["purpose"].unique())
loanstatus = df["loan_status"].value_counts(normalize=True) * 100
print(loanstatus)

a=df["int_rate"].mean()
b=df["int_rate"].median()
c=df["int_rate"].min()
d=df["int_rate"].max()
print(a)
print(b)
print(c)
print(d)

a=df["annual_inc"].mean()
b=df["annual_inc"].median()
c=df["annual_inc"].min()
d=df["annual_inc"].max()
print(a)
print(b)
print(c)
print(d)

Default = df.groupby(["grade", "loan_status"])["loan_status"].count().sort_values(ascending=False)
print(Default)

# Default rate by Grade
matured_loans = df[
    df["loan_status"].isin(["Fully Paid", "Charged Off", "Default"])]
default_loans = matured_loans[
    matured_loans["loan_status"].isin(["Charged Off", "Default"])]
default_by_grade = default_loans.groupby("grade")["loan_status"].count()
total_by_grade = matured_loans.groupby("grade")["loan_status"].count()
default_rate = (default_by_grade / total_by_grade) * 100
print(default_rate.sort_values(ascending=False))


#Average Interest Rate by Grade
avg=df.groupby("grade")["int_rate"].mean()
print(avg)

#Average Loan Amount by Grade
avg = df.groupby("grade")["loan_amnt"].mean()
print(avg)

#Loan Count by Purpose
purpose_count = df["purpose"].value_counts()
print(purpose_count)

#Default Rate by Purpose
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_by_purpose = default_loans.groupby("purpose")["purpose"].count()
total_by_purpose = df.groupby("purpose")["purpose"].count()
default_rate = (default_by_purpose / total_by_purpose) * 100
default_rate = default_rate.sort_values(ascending=False)
print(default_rate)

#Average Income by Loan Grade
avg=df.groupby("grade")["annual_inc"].mean()
print(avg)

#Loan Status by Home Ownership
loan_status_by_home = df.groupby(
    ["home_ownership", "loan_status"]
)["loan_status"].count()
print(loan_status_by_home)

#Default Rate by Home Ownership
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_by_status = default_loans.groupby("home_ownership")["loan_status"].count()
total_by_status = df.groupby("home_ownership")["loan_status"].count()
default_rate = (default_by_status / total_by_status) * 100
default_rate = default_rate.sort_values(ascending=False)
print(default_rate)

#Interest Rate vs Default

df["risk_status"] = np.where(
    df["loan_status"].isin(["Charged Off", "Default"]),
   "Non-Default"
)
avg_interest = df.groupby("risk_status")["int_rate"].mean()
print(avg_interest)

#Loan Term vs Default Rate
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_loans_status=default_loans.groupby("term")["loan_status"].count()
total_by_status = df.groupby("term")["loan_status"].count()
rate=(default_loans_status/total_by_status)*100
print(rate)

#Loan Amount vs Default
condition = [
    df["loan_amnt"] <= 5000,
    (df["loan_amnt"] > 5000) & (df["loan_amnt"] <= 12000),
    df["loan_amnt"] > 12000
]
choices = ["Low", "Medium", "High"]
df["loan_group"] = np.select(condition, choices, default="Unknown")
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_by_group = default_loans.groupby("loan_group")["loan_status"].count()
total_by_group = df.groupby("loan_group")["loan_status"].count()
default_rate = (default_by_group / total_by_group) * 100
default_rate = default_rate.sort_values(ascending=False)
print(default_rate)

#Annual Income vs Default
condition = [
    df["annual_inc"] < 50000,
    (df["annual_inc"] >= 50000) & (df["annual_inc"] <= 100000),
    df["annual_inc"] > 100000
]
choices = ["Low Income", "Medium Income", "High Income"]
df["income_group"] = np.select(condition, choices,default="Unknown")
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_by_group = default_loans.groupby("income_group")["loan_status"].count()
total_by_group = df.groupby("income_group")["loan_status"].count()
default_rate = (default_by_group / total_by_group) * 100
default_rate = default_rate.sort_values(ascending=False)
print(default_rate)

#Employment Length vs Default
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]

default_by_group = default_loans.groupby("emp_length")["loan_status"].count()

total_by_group = df.groupby("emp_length")["loan_status"].count()

default_rate = (default_by_group / total_by_group) * 100

default_rate = default_rate.sort_values(ascending=False)

print(default_rate)

#Verification Status vs Default
default_loan = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_group = default_loan.groupby("verification_status")["loan_status"].count()
total = df.groupby("verification_status")["loan_status"].count()
rate = (default_group / total) * 100
rate = rate.sort_values(ascending=False)
print(rate)

#Installment Analysis

avg_Installment=df["installment"].mean()
min_Installment=df["installment"].min()
max_Installment=df["installment"].max()
median_Installment=df["installment"].median()
print(avg_Installment)
print(min_Installment)
print(max_Installment)
print(median_Installment)

#Loan Amount vs Interest Rate

condition = [
    df["loan_amnt"] <= 5000,
    (df["loan_amnt"] > 5000) & (df["loan_amnt"] <= 12000),
    df["loan_amnt"] > 12000
]
choices = ["Low", "Medium", "High"]
df["loan_group"] = np.select(condition, choices, default="Unknown")
loan = df.groupby("loan_group")["int_rate"].mean().sort_values()
print(loan)

#Interest Rate by Loan Purpose
purpose = df.groupby("purpose")["int_rate"].mean().sort_values(ascending=False)
print(purpose)


#Grade + Term Risk Analysis
loan_status = df[df["loan_status"].isin(["Charged Off", "Default"])]
loan_group = loan_status.groupby(["grade", "term"])["loan_status"].count()
b = df.groupby(["grade", "term"])["loan_status"].count()
rate = (loan_group / b) * 100
default_rate = rate.sort_values(ascending=False)
print(default_rate)


#Identify High-Risk Loan Segment
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
default_by_segment = default_loans.groupby(
    ["grade", "purpose", "term"]
)["loan_status"].count()
total_by_segment = df.groupby(
    ["grade", "purpose", "term"]
)["loan_status"].count()
default_rate = (default_by_segment / total_by_segment) * 100
default_rate = default_rate[total_by_segment >= 100]
default_rate = default_rate.sort_values(ascending=False)
print(default_rate.head(10))


#Loans by Year
df["issue_d"] = pd.to_datetime(df["issue_d"])
df["issue_year"] = df["issue_d"].dt.year
loans_by_year = df.groupby("issue_year")["id"].count()
print(loans_by_year)

#Loan Amount by Year
df["issue_d"] = pd.to_datetime(df["issue_d"])
df["issue_year"] = df["issue_d"].dt.year
loans_by_year = df.groupby("issue_year")["loan_amnt"].sum()
print(loans_by_year)
highest_year = loans_by_year.idxmax()
highest_amount = loans_by_year.max()
print("Year with highest loan volume:", highest_year)
print("Total loan amount:", highest_amount)

#Default Rate by Year
df["issue_d"] = pd.to_datetime(df["issue_d"])
df["issue_year"] = df["issue_d"].dt.year
default_loans = df[df["loan_status"].isin(["Charged Off", "Default"])]
year = default_loans.groupby("issue_year")["loan_status"].count()
years = df.groupby("issue_year")["loan_status"].count()
rate = (year / years) * 100
print(rate)


#Average Interest Rate by Year
df["issue_d"] = pd.to_datetime(df["issue_d"])
df["issue_year"] = df["issue_d"].dt.year
Interest_Rate_year = df.groupby("issue_year")["int_rate"].mean()
print(Interest_Rate_year)


# Loan Grade Composition Over Time
df["issue_d"] = pd.to_datetime(df["issue_d"])
df["issue_year"] = df["issue_d"].dt.year
grade_over_time = df.groupby(
    ["issue_year", "grade"]
)["loan_status"].count().unstack()
print(grade_over_time)


#Rejected Application Count
print("Total Rejected Applications:", rejected.shape[0])

#Rejected Applications by State
state_count = rejected["State"].value_counts()
print(state_count)

#Rejected Applications by Employment Length
state_count = rejected["Employment Length"].value_counts()
print(state_count)


#Rejected Applications by Risk Score
condition = [
    rejected["Risk_Score"] < 600,
    (rejected["Risk_Score"] >= 600) & (rejected["Risk_Score"] < 700),
    (rejected["Risk_Score"] >= 700) & (rejected["Risk_Score"] < 800),
    rejected["Risk_Score"] >= 800
]
choices = ["0-599","600-699","700-799","800+"]
rejected["risk_score_group"] = np.select(condition,choices,default="Unknown")
risk_score_count = rejected["risk_score_group"].value_counts()
print(risk_score_count)

print(accepted.columns)
print(rejected.columns)

#Accepted vs Rejected Applicant Profile
print(accepted.columns)
print(rejected.columns)

# Accepted vs Rejected Applicant Profile

# Accepted applications
accepted_profile = {
    "Total Applications": len(accepted),
    "Average Loan Amount": accepted["loan_amnt"].mean(),
    "Average DTI": accepted["dti"].mean(),
    "Most Common State": accepted["addr_state"].mode()[0],
    "Most Common Employment Length": accepted["emp_length"].mode()[0]
}

# Rejected applications
rejected_profile = {
    "Total Applications": len(rejected),
    "Average Amount Requested": rejected["Amount Requested"].mean(),
    "Average DTI": rejected["Debt-To-Income Ratio"].str.replace("%", "").astype(float).mean(),
    "Most Common State": rejected["State"].mode()[0],
    "Most Common Employment Length": rejected["Employment Length"].mode()[0]
}

print("ACCEPTED APPLICATIONS")
print(accepted_profile)

print("\nREJECTED APPLICATIONS")
print(rejected_profile)


# Matured / Known-Outcome Loan Default Rate
matured_loans = accepted[accepted["loan_status"].isin(
    ["Fully Paid", "Charged Off", "Default"]
)]

default_loans = matured_loans[
    matured_loans["loan_status"].isin(["Charged Off", "Default"])
]

default_rate = (
    len(default_loans) / len(matured_loans)
) * 100

print("Known-Outcome Loans:", len(matured_loans))
print("Default Loans:", len(default_loans))
print("Matured Loan Default Rate:", default_rate, "%")


