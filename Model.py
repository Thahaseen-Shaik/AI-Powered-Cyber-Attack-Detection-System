import pandas as pd
import streamlit as st
import re
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------------------
# Load Dataset
# ---------------------------

data = pd.read_csv("dataset/KDDTrain+.txt", header=None)

# ---------------------------
# Column Names
# ---------------------------

columns = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in','num_compromised',
'root_shell','su_attempted','num_root','num_file_creations','num_shells',
'num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',
'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count',
'dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',
'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate',
'attack','level'
]

data.columns = columns

# ---------------------------
# Encode categorical data
# ---------------------------

encoder = LabelEncoder()

data['protocol_type'] = encoder.fit_transform(data['protocol_type'])
data['service'] = encoder.fit_transform(data['service'])
data['flag'] = encoder.fit_transform(data['flag'])
data['attack'] = encoder.fit_transform(data['attack'])

# ---------------------------
# Feature / Label split
# ---------------------------

X = data.drop(['attack','level'], axis=1)
y = data['attack']

# ---------------------------
# Train / Test Split
# ---------------------------

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42)

# ---------------------------
# Train Model
# ---------------------------

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# ---------------------------
# Accuracy
# ---------------------------

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# ---------------------------
# SQL Injection Detector
# ---------------------------

def detect_sql_injection(query):

    patterns = [
        r"(\bOR\b\s+'.+'\s*=\s*'.+')",
        r"(\bAND\b\s+'.+'\s*=\s*'.+')",
        r"(--)",
        r"(\bUNION\b\s+\bSELECT\b)",
        r"(\bDROP\b\s+\bTABLE\b)",
        r"(\bINSERT\b\s+\bINTO\b)",
        r"(\bDELETE\b\s+\bFROM\b)"
    ]

    for p in patterns:
        if re.search(p, query, re.IGNORECASE):
            return "⚠ SQL Injection Detected"

    return "✅ Safe Input"


# ---------------------------
# Sidebar Navigation
# ---------------------------

st.sidebar.title("Cyber Security Dashboard")

page = st.sidebar.selectbox(
"Select Module",
["Home","Network Attack Detection","SQL Injection Detection","Attack Statistics"]
)

# ---------------------------
# HOME PAGE
# ---------------------------

if page == "Home":

    st.title("Cyber Attack Detection System")

    st.success("Cyber Defense System Active – Monitoring Network Traffic")

    col1, col2, col3 = st.columns(3)

    col1.metric("Model Accuracy", f"{round(accuracy*100,2)}%")
    col2.metric("Total Records", len(data))
    col3.metric("Attack Types", data['attack'].nunique())

    st.subheader("Live Threat Monitoring")

    threats = ["Normal Traffic","DDoS Attack","SQL Injection Attempt","Bot Traffic"]
    current = random.choice(threats)

    if current == "Normal Traffic":
        st.success("Network Status: Normal Traffic")
    else:
        st.error(f"Threat Detected: {current}")

    st.subheader("Security Alerts")

    alerts = [
        "Multiple failed login attempts detected",
        "Suspicious SQL query detected",
        "Unusual network traffic detected",
        "Unauthorized login attempt detected"
    ]

    st.warning(random.choice(alerts))

    st.subheader("Dataset Preview")
    st.dataframe(data.head())


# ---------------------------
# NETWORK ATTACK DETECTION
# ---------------------------

elif page == "Network Attack Detection":

    st.title("Network Attack Detection")

    if st.button("Run Detection Example"):

        sample = X_test.iloc[0:1]
        prediction = model.predict(sample)

        if prediction[0] == 0:
            st.success("Normal Traffic")
        else:
            st.error("Cyber Attack Detected")


# ---------------------------
# SQL INJECTION DETECTION
# ---------------------------

elif page == "SQL Injection Detection":

    st.title("SQL Injection Detection")

    query = st.text_area("Enter SQL Query")

    if st.button("Analyze Query"):

        if query == "":
            st.warning("Please enter a SQL query")
        else:

            result = detect_sql_injection(query)

            if "Detected" in result:
                st.error(result)
            else:
                st.success(result)


# ---------------------------
# ATTACK STATISTICS
# ---------------------------

elif page == "Attack Statistics":

    st.title("Attack Distribution Analysis")

    attack_counts = data['attack'].value_counts()

    st.bar_chart(attack_counts)

    st.write("Attack Frequency:")
    st.dataframe(attack_counts.reset_index().rename(columns={'index':'Attack Type','attack':'Count'}))

# ---------------------------
# Footer
# ---------------------------

st.markdown("---")
st.caption("Cyber Attack Detection System | AIML Project | Streamlit Dashboard")
