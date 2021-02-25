 import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

clicks = ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
columns = 'is_click',
index = 'utm_source',
values = 'user_id').reset_index()

print(clicks_pivot)

clicks_pivot['percent-clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

ad_clicks.groupby('experimental_group').user_id.count().reset_index()

numbers = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
number_pivot = numbers.pivot(
columns = 'is_click',
index = 'experimental_group',
values = 'user_id').reset_index()

print(number_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

print(a_clicks)

aa_clk = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_clicks_pivot = aa_clk.pivot(
columns = 'is_click',
index = 'day',
values = 'user_id').reset_index()

bb_clk = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_pivot = bb_clk.pivot(
columns = 'is_click',
index = 'day',
values = 'user_id').reset_index()

print(a_clicks_pivot)
print(b_clicks_pivot)

