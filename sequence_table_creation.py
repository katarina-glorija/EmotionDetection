from datetime import datetime, timedelta
import pandas as pd
import pytz

conversation_df = pd.read_excel('data/Conversations.xlsx')

conversation_df = conversation_df.sort_values(by=['LearnerId','DateTime'], ascending=[True, True])
merged_df = pd.read_excel('events_info.xlsx')

conversation_df['DateTime'] = pd.to_datetime(conversation_df['DateTime'])
merged_df['DateTime'] = pd.to_datetime(merged_df['DateTime'])

conversation_df['DateTime'] = conversation_df['DateTime'].dt.tz_convert(pytz.UTC)
merged_df['DateTime'] = merged_df['DateTime'].dt.tz_convert(pytz.UTC)

columns = merged_df.columns.tolist()
columns.append('Emotion')

result_df = pd.DataFrame(columns=columns)
for student_id, student_answers in conversation_df.groupby('LearnerId'):
    previous_timestamp = pd.to_datetime(datetime.now() - timedelta(days=36525))
    previous_timestamp = previous_timestamp.replace(tzinfo=pd.Timestamp(merged_df['DateTime'].iloc[0]).tzinfo)  # Use the timezone info from merged_df
    for conversation_id, conversation in student_answers.iterrows():
        print(conversation)
        answer_timestamp = pd.to_datetime(conversation['DateTime']).replace(tzinfo=pd.Timestamp(merged_df['DateTime'].iloc[0]).tzinfo)
        current_sequence = merged_df[(previous_timestamp <= merged_df['DateTime']) & (merged_df['DateTime'] <= answer_timestamp) & (merged_df['LearnerId'] == student_id)]
        current_sequence['Emotion'] = ''
        new_row_data = [0, conversation['DateTime'], 'emotion_detection', 0, 0,0, 0, 0, 0, student_id, conversation['Emocija']]
        current_sequence.loc[len(current_sequence.index)] = new_row_data
        result_df = pd.concat([result_df, current_sequence], ignore_index=True)  # Reassign the result back to result_df
        previous_timestamp = answer_timestamp

result_df['DateTime'] = result_df['DateTime'].astype(str)  # Convert to string
result_df.to_excel('sequences.xlsx', index=False)