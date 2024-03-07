import pandas as pd
import json
import difflib

df_conversations = pd.read_excel("data/Conversations.xlsx")
# df_events = pd.read_csv("events_data.csv", sep = ';')
df_events = pd.read_excel('events_info.xlsx')

df_conversations['DateTime'] = pd.to_datetime(df_conversations['DateTime'])
df_events['DateTime'] = pd.to_datetime(df_events['DateTime'])

df_conversations['TimeWindow'] = df_conversations['DateTime'].dt.floor('20T')
df_events['TimeWindow'] = df_events['DateTime'].dt.floor('20T')

# Merge based on 'LearnerId' and 'TimeWindow'
merged_table = pd.merge(df_conversations, df_events, on=['LearnerId', 'TimeWindow'], how='left')
merged_table['TimeWindow'] = merged_table['TimeWindow'].dt.tz_localize(None)
merged_table['DateTime_x'] = merged_table['DateTime_x'].dt.tz_localize(None)
merged_table['DateTime_y'] = merged_table['DateTime_y'].dt.tz_localize(None)
# Save the merged table to a new Excel file
merged_table.to_excel("merged_table.xlsx", index=False)

# Merge tables on learner ID

# merged_df = pd.merge(df_conversations, df_events, on='LearnerId')
# # Convert timestamp columns to datetime objects
# merged_df['DateTime'] = pd.to_datetime(merged_df['DateTime'])
# merged_df['event_timestamp'] = pd.to_datetime(merged_df['event_timestamp'])
#
# # Define a time window (15 to 20 minutes)
# time_window = pd.to_timedelta('20 minutes')
#
# merged_df['rounded_label_timestamp'] = merged_df['DateTime'].dt.floor(time_window)
# merged_df['rounded_event_timestamp'] = merged_df['event_timestamp'].dt.floor(time_window)
#
# # Group by learner ID, label, and the rounded timestamp intervals, then count the occurrences
# # result_df = merged_df.groupby(['LearnerId', 'Emocija', pd.Grouper(key='rounded_event_timestamp', freq=time_window), 'Event']).size().unstack(fill_value=0)
#
# # result_df = merged_df.groupby(['LearnerId', 'Emocija', 'rounded_event_timestamp', 'Event']).size().reset_index(name='count')
# # result_pivot = result_df.pivot_table(index=['LearnerId', 'Emocija', 'rounded_event_timestamp'], columns='Event', values='count', fill_value=0).reset_index()
# #
# # # Calculate the standard deviation for each event type
# # std_df = result_pivot.groupby(['LearnerId', 'Emocija']).std().reset_index()
#
# # Reset the index to make the columns flat
# #result_df = result_df.reset_index()
#
# # Display the result
# # print(std_df)
#
# merged_df['rounded_event_timestamp'] = merged_df['rounded_event_timestamp'].dt.tz_localize(None)
#
# merged_df.to_excel("events_info_20_minutes.xlsx")