import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("labeled_anomaly_dataset.csv")

# Filter: Remove ARP and missing ports
df = df[df["Protocol"].isin(["TCP", "UDP"])]
df = df.dropna(subset=["Source Port", "Destination Port"])
df["Source Port"] = df["Source Port"].astype(int)
df["Destination Port"] = df["Destination Port"].astype(int)

# Encode protocol
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

protocol_encoded = encoder.fit_transform(df[["Protocol"]])
protocol_cols = [f"Protocol_{p}" for p in encoder.categories_[0]]

# Features
X = pd.concat([
    df[["Length", "Source Port", "Destination Port"]].reset_index(drop=True),
    pd.DataFrame(protocol_encoded, columns=protocol_cols)
], axis=1)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Target
y = df["bad_packet"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and preprocessing tools
joblib.dump(model, "anomaly_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoder, "encoder.pkl")

print("✅ Model and preprocessing tools saved.")