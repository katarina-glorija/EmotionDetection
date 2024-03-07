import pandas as pd
from itertools import groupby
import matplotlib.pyplot as plt
import seaborn as sns
import json
#
df = pd.read_excel("Real_events.xlsx")
events_json = df["DomainEvent"]
events = []
#
for event_json in events_json:
    events.append(json.loads(event_json))
#
# # Assuming 'events' is a list of dictionaries with 'LearnerId', 'EventName', 'TimeStamp', etc.
student_id = 134
# events_without_feedback = []
#
# # Filter events for the selected student
student_events = [event for event in events if event['LearnerId'] == student_id]
# for event in events:
#     if "Feedback" not in event:
#         events_without_feedback.append(event)
#
#
# # Extract relevant information into a dictionary or list
event_data = {
    'EventName': [event['$discriminator'] for event in student_events],
    'TimeStamp': pd.to_datetime([event['TimeStamp'] for event in student_events]),  # Convert to datetime
    # Add more fields as needed
}
#
# # Create a DataFrame from the extracted data
df = pd.DataFrame(event_data)
#
# df.to_csv("Without_Feedback.csv")

# Check for constant values and drop corresponding columns
# non_constant_columns = df.columns[df.nunique() > 1]
# df = df[non_constant_columns]

pivot_table = df.pivot_table(index='EventName', columns='TimeStamp', aggfunc='size', fill_value=0)

# Transpose the pivot table and calculate the correlation matrix
correlation_matrix = pivot_table.T.corr()

print(correlation_matrix)

sns.set(style="white")  # Set the style of the visualization
plt.figure(figsize=(10, 8))  # Set the size of the plot

# Plot heatmap with correlation matrix
sns.heatmap(correlation_matrix, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5)

plt.title('Correlation Heatmap')
plt.show()

# print(df['TimeStamp'].isnull().any())
# print(df['TimeStamp'].unique())
# print(df['TimeStamp'].dtype)
# print(df['TimeStamp'].nunique())
#
# # Create a pivot table and calculate the correlation matrix
# correlation_matrix = df.pivot_table(index='EventName', columns='EventName', values='TimeStamp', aggfunc='mean').corr()
#
# print(correlation_matrix)

# Assuming your DataFrame is named 'df'
# Convert 'Timestamp' to datetime format
# df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])
#
# # Sort by 'Learner Id' and 'Timestamp'
# df.sort_values(by=['Learner Id', 'Time Stamp'], inplace=True)
#
# df_grouped = df.groupby('Learner Id')
#
# df_parted = df_grouped.head(20)
#
# 1. Individual Timeline Plot
# plt.figure(figsize=(30, 30))
# groups = groupby(sorted(events, key=lambda x: x['TimeStamp']), key=lambda x: x['LearnerId'])
# first_group = next(groups, (None, []))[1]
# print(first_group)
# for learner_id, data in groupby(sorted(events, key=lambda x: x['TimeStamp']), key=lambda x: x['LearnerId']):
#    data = list(groupby(sorted(events, key=lambda x: x['TimeStamp']), key=lambda x: x['LearnerId']))  # Convert groupby object to a list

# plt.plot([entry['TimeStamp'] for entry in data], [entry['$discriminator'] for entry in data], label=f'Learner {data["LearnerId"]}')
#
# plt.xlabel('Time Stamp')
# plt.ylabel('Event')
# plt.title('Individual Timeline Plot')
# plt.legend()
# plt.show()

# 2. Event Frequency Plot
# plt.figure(figsize=(30, 15))
# sns.countplot(x='Event', data=df)
# plt.xlabel('Event')
# plt.ylabel('Frequency')
# plt.title('Event Frequency Plot')
# plt.show()
#
# # 3. Event Sequence Heatmap
# event_sequence_matrix = pd.crosstab(df['Learner Id'], df['Event'])
# plt.figure(figsize=(30, 30))
# sns.heatmap(event_sequence_matrix, cmap='Blues', annot=True)
# plt.xlabel('Event')
# plt.ylabel('Learner Id')
# plt.title('Event Sequence Heatmap')
# plt.show()

# # 4. Transition Matrix
# df['Next_Event'] = df['Event'].shift(-1)
# transition_matrix = pd.crosstab(df['Event'], df['Next_Event'], dropna=False)
# transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)  # Normalize
# plt.figure(figsize=(12, 8))
# sns.heatmap(transition_matrix, cmap='Blues', annot=True, cbar_kws={'label': 'Probability'})
# plt.xlabel('Next Event')
# plt.ylabel('Current Event')
# plt.title('Transition Matrix')
# plt.show()

# df.plot(x='Learner Id', y='Event', kind='bar')
# plt.show()

# events = df["DomainEvent"]
# # event = events[0].split(",")
# learnerIds = []
# timeStamps = []
# eventNames = []
# knowledgeComponentIds = []
# for event in events:
#     json_object = json.loads(event)
#     # print(json_object)
#     # if "Feedback" in event or "Hint" in event:
#     #     continue
#     event = event.split(",")
#     # learnerId = (event[0].split(":")[1]).replace(" ", "")
#     learnerIds.append(json_object["LearnerId"])
#     # timeStamp = (event[1].split(":")[1]).replace("\"", "").replace(" ", "")
#     timeStamps.append(json_object["TimeStamp"])
#     # eventName = (event[2].split(":")[1]).replace("\"", "").replace(" ", "")
#     eventNames.append(json_object["$discriminator"])
#     # knowledgeComponentId = (event[3].split(":")[1]).replace("\"", "").replace("}", "").replace(" ", "")
#     knowledgeComponentIds.append(json_object["KnowledgeComponentId"])
#
# list_of_tuples = list(zip(learnerIds, timeStamps, eventNames, knowledgeComponentIds))
#
# # Assign data to tuples.
# list_of_tuples
#
# # Converting lists of tuples into
# # pandas Dataframe.
# newDf = pd.DataFrame(list_of_tuples,
#                   columns=['Learner Id', 'Time Stamp', 'Event', 'Knowledge Component Id'])
#
# # print(newDf)
#
# newDf.to_csv("events_data.csv")


# df_events = pd.read_csv("Events.csv")
# emotions = pd.read_excel("data/Anotiranje-sve.xlsx")
#
# real_events = pd.DataFrame(columns=df_events.columns)
#
#
# for index, event in df_events.iterrows():
#     event_json = json.loads(event["DomainEvent"])
#     if event_json["LearnerId"] in emotions["LearnerId"].values:
#         real_events.loc[index] = event
#
# real_events.to_excel("Real_events.xlsx")