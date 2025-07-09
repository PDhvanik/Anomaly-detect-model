# Network Anomaly Detection Project

## Overview

This project provides a framework for simulating, detecting, and analyzing network traffic anomalies, including DDoS and other malicious activities. It includes tools for generating labeled network traffic data, training a machine learning model to detect anomalies, and scripts to simulate both normal and attack traffic.

## Features

- **Synthetic Data Generation:** Simulate normal, anomalous TCP, and UDP flood attack traffic.
- **Labeled Dataset:** Automatically generate a labeled CSV dataset for anomaly detection.
- **Model Training:** Train a Random Forest classifier to detect anomalous network packets.
- **Traffic Simulation:** Scripts to simulate anomalous and DDoS traffic for testing.

## Project Structure

```
Python_Model/
├── anomalous_traffic.py         # Simulate sending anomalous TCP packets
├── DDoS.py                     # Simulate a UDP flood (DDoS) attack
├── generate_Data.py            # Generate and label synthetic network traffic data
├── labeled_anomaly_dataset.csv # Labeled dataset of network packets
├── train_anomaly_model.py      # Train anomaly detection model
└── Model/
    ├── anomaly_model.pkl       # Trained Random Forest model
    ├── encoder.pkl             # OneHotEncoder for protocol feature
    └── scaler.pkl              # StandardScaler for feature normalization
```

## File Descriptions

- **generate_Data.py**: Generates synthetic network traffic (normal, anomalous TCP, UDP flood), labels it, and saves to `labeled_anomaly_dataset.csv`.
- **labeled_anomaly_dataset.csv**: Contains columns: Time, Source, Destination, Protocol, Length, Source Port, Destination Port, bad_packet (1=anomaly, 0=normal).
- **train_anomaly_model.py**: Trains a Random Forest classifier using the labeled dataset. Saves the model and preprocessing tools in the `Model/` directory.
- **anomalous_traffic.py**: Sends a burst of anomalous TCP packets to a target IP for testing.
- **DDoS.py**: Simulates a UDP flood attack to a target IP and port.
- **Model/**: Stores the trained model (`anomaly_model.pkl`), protocol encoder (`encoder.pkl`), and feature scaler (`scaler.pkl`).

## Setup Instructions

1. **Clone the repository** and navigate to the `Python_Model` directory.
2. **Install dependencies:**
   ```bash
   pip install pandas scikit-learn scapy joblib
   ```
3. **Generate Data:**
   ```bash
   python generate_Data.py
   ```
   This will create `labeled_anomaly_dataset.csv`.
4. **Train the Model:**
   ```bash
   python train_anomaly_model.py
   ```
   This will save the model and preprocessing tools in the `Model/` directory.

## Usage

- **Simulate Anomalous Traffic:**
  ```bash
  python anomalous_traffic.py
  ```
- **Simulate DDoS Attack:**
  ```bash
  python DDoS.py
  ```

## Dependencies

- pandas
- scikit-learn
- scapy
- joblib

Install all dependencies with:

```bash
pip install pandas scikit-learn scapy joblib
```

## Notes

- The scripts are for research and educational purposes only. Do not use attack scripts on networks without permission.
- The dataset and model are synthetic and may not generalize to real-world traffic without further tuning.
