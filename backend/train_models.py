import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

# This is to load the dataset 
df = pd.read_csv("pipeline_data.csv")

# These are the features and targets
X = df[["pressure", "flow_rate", "temperature", "vibration",]]
y_score = df["risk_score"]
y_issue = df["issue_type"]
y_issue = y_issue.fillna("None") 

# Encode the issue type 
label_encoder = LabelEncoder()
y_issue_encoded = label_encoder.fit_transform(y_issue)

print(label_encoder.classes_)

# Now scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the dataset into training and testing sets
X_train, X_test, y_score_train, y_score_test = train_test_split(X_scaled, y_score, test_size=0.2, random_state=42)
_, _, y_issue_train, y_issue_test = train_test_split(X_scaled, y_issue_encoded, test_size=0.2, random_state=42)

# Train the models now 
reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
reg_model.fit(X_train, y_score_train)

clf_model = RandomForestClassifier(n_estimators=100, random_state=42)
clf_model.fit(X_train, y_issue_train)

# Save the models and scaler
joblib.dump(reg_model, "risk_score_model.joblib")
joblib.dump(clf_model, "issue_classifier.joblib")
joblib.dump(scaler, "scaler.joblib")
joblib.dump(label_encoder, "label_encoder.joblib")

# Print the model training completion message
print("Models trained and saved successfully.")
# This code trains two models: one for predicting risk scores and another for classifying issue types.

'''
| File                            | Purpose                               |
| ------------------------------- | ------------------------------------- |
| `risk_score_model.joblib`       | Predicts risk score (regression)      |
| `issue_classifier_model.joblib` | Predicts issue type (classification)  |
| `scaler.joblib`                 | Normalizes sensor input               |
| `label_encoder.joblib`          | Converts class labels to/from numbers |

'''