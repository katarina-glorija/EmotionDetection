import pandas as pd
import json

df = pd.read_excel("Real_events.xlsx")

events_info = pd.DataFrame(columns=['event_timestamp', 'event_description', 'hint_requested', 'hint_order',
                                    'correct_answer', 'correctness_percentage', 'reattempt_count', 'submission_type',
                                    'knowledge_component_code', 'learner_id'])

for event_json in df["DomainEvent"]:
    event = json.loads(event_json)

    index = len(events_info)
    events_info.loc[index, 'event_timestamp'] = event['TimeStamp']
    events_info.loc[index, 'learner_id'] = event['LearnerId']
    events_info.loc[index, 'event_description'] = event['$discriminator']
    events_info.loc[index, 'knowledge_component_code'] = event['KnowledgeComponentId']

    hint_order = -1
    correct_answer = -1
    correctness_percentage = -1
    reattempt_count = -1
    submission_type = -1

    if 'Submission' in event:
        feedback = event['Feedback']
        submission = event['Submission']

        hint_order = feedback['Hint']['Order'] if feedback['Hint'] else -1
        correct_answer = feedback['Evaluation']['Correct']
        correctness_percentage = feedback['Evaluation']['CorrectnessLevel']
        reattempt_count = submission['ReattemptCount']
        submission_type = submission['$discriminator']

    events_info.loc[
        index, ['hint_order', 'correct_answer', 'correctness_percentage', 'reattempt_count', 'submission_type']] = [
        hint_order, correct_answer, correctness_percentage, reattempt_count, submission_type]

events_info.to_excel("events_info.xlsx")