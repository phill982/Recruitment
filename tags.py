import pandas as pd

# Load the Excel file
data = pd.read_excel('tags_report.xlsx')

# Combine 'PNM First Name' and 'PNM Last Name' into a single 'Candidate Name'
data['Candidate Name'] = data['PNM First Name'].str.strip() + ' ' + data['PNM Last Name'].str.strip()

# Standardize tag names by stripping whitespace and setting to lowercase (if case-insensitive)
data['Tag Name'] = data['Tag Name'].str.strip().str.lower()

# Priority mapping for tags, lower number means higher priority
priority = {
    'dream girl': 1,
    'yes please': 2,
    'maybe yes': 3,
    'maybe no': 4,
    'no thanks': 5,
    'major concern': 6,
    'even split': 7  # Assign a lower priority for even splits
}

# Function to aggregate tags directly into a list of dictionaries
def aggregate_tags(df):
    result = []
    grouped = df.groupby(['PNM ID', 'Candidate Name'])
    for (id, name), group in grouped:
        tag_counts = group['Tag Name'].value_counts()
        top_tags = tag_counts[tag_counts == tag_counts.max()]
        most_frequent = 'even split' if len(top_tags) > 1 else top_tags.idxmax()
        dream_girl_votes = tag_counts.get('dream girl', 0)
        concern_votes = tag_counts.get('major concern', 0)

        result.append({
            'PNM ID': id,
            'First Name': name.split(' ')[0],
            'Last Name': ' '.join(name.split(' ')[1:]),
            'Most Frequent Tag': most_frequent.title(),  # Convert to title case for display
            'Tag Priority': priority.get(most_frequent, 8),  # Default priority if not listed
            'Dream Girl': 'Dream Girl' if dream_girl_votes > 0 else '',
            'Concern': 'Concern' if concern_votes > 0 else '',
            'Decision Type': 'Unanimous' if len(tag_counts) == 1 else 'Disagreement',
            'Split of Votes': ', '.join([f"{v} votes {k}" for k, v in tag_counts.items()])
        })

    return result

# Aggregate tags using the defined function
aggregated_data = aggregate_tags(data)

# Convert the list of dictionaries to a DataFrame for sorting and final output
final_data = pd.DataFrame(aggregated_data)
final_data.sort_values(by=['Tag Priority', 'PNM ID'], ascending=[True, True], inplace=True)

# Remove the 'Tag Priority' column before saving (it's just for sorting)
final_data.drop('Tag Priority', axis=1, inplace=True)

# Export the final sorted data to an Excel file with index
final_data.to_excel('Sorted_Recruitment_Data.xlsx', index=False, sheet_name='Sorted Data')

print("Data has been saved to 'Sorted_Recruitment_Data.xlsx'")
