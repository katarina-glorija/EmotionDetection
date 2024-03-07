import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Assuming your result_df DataFrame
df = pd.read_excel("events_std_2_minutes.xlsx")

# Extract relevant columns for correlation
correlation_df = df[['AssessmentItemAnswered', 'AssessmentItemSelected', 'HintsRequested',
                     'InstructionalItemsSelected', 'KnowledgeComponentCompleted', 'KnowledgeComponentPassed',
                     'KnowledgeComponentSatisfied', 'KnowledgeComponentStarted', 'SessionAbandoned',
                     'SessionContinued', 'SessionLaunched', 'SessionPaused', 'SessionTerminated', 'Emocija']]


label_encoder = LabelEncoder()
correlation_df.loc[:, 'Emocija'] = label_encoder.fit_transform(correlation_df['Emocija'])

# Calculate the correlation matrix
correlation_matrix = correlation_df.corr()

# Create a heatmap
plt.figure(figsize=(15, 15))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()