import pandas as pd

# Assuming the CSV file "ad_clicks.csv" is available in the current directory

# Load the data
ad_clicks = pd.read_csv("/mnt/data/ad_clicks.csv")

# 1. Examine the first few rows of ad_clicks
ad_clicks_head = ad_clicks.head()

# 2. Count views from each utm_source
views_by_source = ad_clicks.groupby('utm_source').user_id.count()

# 3. Create is_click column
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

# 4. Count clicks by source and click status
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# 5. Pivot data
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

# 6. Calculate percent clicked
clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])) * 100

# 7. Check if same number of people shown both ads
group_counts = ad_clicks.groupby('experimental_group').user_id.count()

# 8. Check which ad got more clicks
clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
clicks_pivot_group = clicks_by_group.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
clicks_pivot_group['percent_clicked'] = (clicks_pivot_group[True] / (clicks_pivot_group[True] + clicks_pivot_group[False])) * 100

# 9. Create separate DataFrames for A and B groups
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# 10. Calculate percent clicked by day for each group
a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_clicks_pivot = a_clicks_by_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
a_clicks_pivot['percent_clicked'] = (a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])) * 100

b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks_pivot = b_clicks_by_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
b_clicks_pivot['percent_clicked'] = (b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])) * 100

import ace_tools as tools; tools.display_dataframe_to_user(name="Ad Clicks Initial Rows", dataframe=ad_clicks_head)
tools.display_dataframe_to_user(name="Views by Source", dataframe=views_by_source)
tools.display_dataframe_to_user(name="Clicks by Source", dataframe=clicks_by_source)
tools.display_dataframe_to_user(name="Clicks Pivot", dataframe=clicks_pivot)
tools.display_dataframe_to_user(name="Group Counts", dataframe=group_counts)
tools.display_dataframe_to_user(name="Clicks Pivot Group", dataframe=clicks_pivot_group)
tools.display_dataframe_to_user(name="A Clicks Pivot by Day", dataframe=a_clicks_pivot)
tools.display_dataframe_to_user(name="B Clicks Pivot by Day", dataframe=b_clicks_pivot)
