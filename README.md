# AI-Powered-Cyber-Attack-Detection-System

## Project Overview

The **Cyber Attack Detection System** is a machine learning–based cybersecurity application designed to detect malicious activities in network traffic and identify potential cyber threats.

The system analyzes network data using a trained machine learning model and also detects **SQL injection attacks** from user input.

It provides an interactive **Streamlit dashboard** that displays security metrics, attack detection results, and attack statistics.

---

# Objectives

The main objectives of this project are:

* Detect malicious network traffic using machine learning
* Identify cyber attacks such as **DDoS, bot traffic, and intrusion attempts**
* Detect **SQL injection attacks** in user queries
* Provide a visual dashboard for monitoring network security

---

# Technologies Used

| Technology                  | Purpose                              |
| --------------------------- | ------------------------------------ |
| Python                      | Programming language                 |
| Pandas                      | Data processing and dataset handling |
| Scikit-learn                | Machine learning algorithms          |
| Random Forest               | Attack classification model          |
| Streamlit                   | Interactive dashboard                |
| Regex (Regular Expressions) | SQL injection detection              |
| NSL-KDD Dataset             | Network intrusion dataset            |

---

# Dataset

The project uses the **NSL-KDD dataset**, which is widely used in intrusion detection research.

The dataset contains network traffic information such as:

* protocol type
* service
* packet size
* login attempts
* error rates
* connection duration

Each record is labeled as **normal traffic or a cyber attack**.

---

# Project Features

## 1. Machine Learning Based Attack Detection

The system uses a **Random Forest classifier** trained on the NSL-KDD dataset to detect network attacks.

Steps include:

* Data preprocessing
* Feature encoding
* Training the model
* Predicting network attacks

---

## 2. SQL Injection Detection

The system analyzes SQL queries entered by the user and detects suspicious patterns such as:

* `' OR '1'='1`
* `UNION SELECT`
* `DROP TABLE`
* `DELETE FROM`
* SQL comments `--`

If these patterns are detected, the system flags the query as **SQL Injection Detected**.

---

## 3. Streamlit Dashboard

The project includes a **Streamlit dashboard** that provides:

* System status monitoring
* Network attack detection module
* SQL injection detection module
* Attack statistics visualization
* Dataset preview

---

## 4. Attack Statistics Visualization

The system displays a **graph showing the distribution of attacks** in the dataset.
This helps users understand the frequency of different attack types.

---

## 5. Live Threat Monitoring

The dashboard simulates **real-time cyber threat monitoring** and displays alerts if suspicious activity is detected.

---

# Machine Learning Model

The system uses the **Random Forest Algorithm**.

Advantages:

* High accuracy
* Handles large datasets
* Reduces overfitting
* Suitable for classification problems

Dataset split:

* **80% Training Data**
* **20% Testing Data**

The model performance is evaluated using **accuracy score**.

---

# Example SQL Injection Attack

### Safe Query

```
SELECT * FROM users WHERE username='thassu'
```

Output:

```
Safe Input
```

### Injection Query

```
admin' OR '1'='1
```

Output:

```
SQL Injection Detected
```

---

# Installation

Install the required libraries:

```
pip install streamlit pandas scikit-learn matplotlib
```

---

# Run the Application

Start the Streamlit application:

```
streamlit run model.py
```

Open the browser and go to:

```
http://localhost:8501
```

---

# Project Structure

```
CyberProject
│
├── dataset
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
│
├── model.py
├── README.md
└── requirements.txt
```

---

# Future Improvements

Possible enhancements include:

* Real-time network traffic monitoring
* Deep learning–based attack detection
* Integration with web security systems
* Detection of additional attacks such as **XSS and CSRF**

---

# Conclusion

This project demonstrates how machine learning can be used to detect cyber attacks and protect network systems.

By combining **network attack detection and SQL injection analysis**, the system provides a basic cybersecurity monitoring solution with an interactive dashboard.

---

# Author

Thahaseen Gulam

