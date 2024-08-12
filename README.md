# Recruitment Voting Automation System

This recruitment automation system is designed to streamline the evaluation process of over 800 candidates by replacing the traditional numerical ranking system with a more robust and descriptive tag-based system. This custom coding solution processes scores, applies filters, and organizes data into a new Excel sheet, eliminating over 6 hours of manual sorting daily.

# Old Method
Process: 3-4 chapter members would vote on each candidate using a numerical ranking system.

Challenges: Voters have varying standards, leading to inconsistent scores. For example, some voters might give a high rating to all candidates unless there is a strong dislike, resulting in skewed data.

Manual Sorting: The recruitment committee had to manually sort through large numbers of candidates (800 initially, narrowing down to 100) which was time-consuming and inefficient.


# Problems Identified with Old Method
Inconsistent Voting: Variations in voting standards among chapter members led to unreliable rankings.

Descriptive Inadequacy: Numerical scores did not provide enough context for decisions.

Time-Consuming Process: Extensive manual effort was required to sort and rank candidates.

# Solution
The code automates the sorting and evaluation process by focusing on a tag-based voting system rather than numerical scores. This method enhances the accuracy and efficiency of the recruitment process by addressing the issues inherent in the old ranking system.

# Features
Tag-Based Evaluation: Candidates are evaluated using specific tags such as 'Dream Girl', 'Yes Please', 'Maybe', and 'Major Concern', each providing clear and actionable insights.

Detailed Commentary: Each tag is accompanied by a comment section allowing voters to explain their choice, adding depth to the evaluation.

Flagging System: Special attention tags like 'Dream Girl' and 'Major Concern' are flagged in separate columns for immediate action.

Disagreement Handling: The system identifies if the votes are unanimous or if there's a disagreement, displaying the vote split for further review by the recruitment team.

# Code Creation: 
Code filters through all of the tags, and takes the most frequent used tag by the group that voted on the candidate to rank. If there was a Dream Girl or Major Concern Tag, that would be flagged in a seperate column on the excel sheet. 

# Key Functions of the Code:
Tag Filtering: The code scans all votes for each candidate and identifies the most frequently chosen tag as the primary criterion for ranking.

Flagging Special Tags: Tags that carry significant weight, such as 'Dream Girl' and 'Major Concern,' are highlighted in separate columns within the Excel sheet. This allows for quick identification and action from the recruitment team.

Vote Disagreement: The code detects whether the votes for a candidate are unanimous or if there's a disagreement among the voters. In cases of disagreement, the exact split of votes is displayed in an adjacent column.

Handling Even Splits: For cases where there is an even split in votes (e.g., an equal number of 'Yes' and 'No' votes), the split is detailed in the Excel sheet. This is the only aspect of the process that requires manual intervention, as the recruitment team must review the split and make a decision based on the detailed vote distribution.

# Output:
The system automatically generates a new Excel sheet, titled Sorted_Recruitment_Data.xlsx, which organizes candidates based on the derived rankings from the tags and displays all relevant voting details for further review.

# Features
The enhanced features of this system are designed to provide a comprehensive overview of candidate evaluations while addressing the shortcomings of the previous method:

# Tag-Based Evaluation
Descriptive Accuracy: Unlike numerical scores, tags provide a qualitative measure of a candidate's fit, reducing the impact of voter bias and varying standards.

Comprehensive Details: Each tag is accompanied by voter comments, offering insights into the reasons behind each tag, which aids in understanding the context of each vote.

# Special Attention to Critical Tags
Immediate Flagging: Tags that signify a candidate as a 'Dream Girl' or a 'Major Concern' are immediately flagged for quick identification. This feature ensures that candidates requiring special attention are not overlooked.

# Resolution of Voting Discrepancies
Unanimous vs. Disagreement: The system clearly indicates whether a candidate's evaluation is unanimous or if there is a disagreement, enabling the recruitment team to quickly identify areas that may need closer scrutiny.

Even Split Handling: In cases of an even split, detailed information is provided to assist the recruitment team in making informed decisions. This manual intervention ensures that each candidate is fairly evaluated, considering the diverse perspectives of the voters.

# Technical and Usage Details
Implementation Language: Python, utilizing the Pandas library for efficient data manipulation and Excel operations.

Data Privacy: Given the sensitivity of recruitment data, a test file is used for demonstration purposes on platforms like GitHub, ensuring that no confidential information is publicly shared.


