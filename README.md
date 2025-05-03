# 📊 Feature Adoption Tracker

A lightweight Streamlit dashboard that analyzes product usage logs and generates AI-powered summaries for product and operations teams.

---

## 💡 What It Does

- 📥 Takes in CSV logs of product feature usage
- 📈 Visualizes feature adoption trends
- 🧠 Uses OpenAI GPT to summarize key insights, trends, and drop-offs
- 💬 Helps PMs and product ops quickly understand what’s working (and what’s not)

---

## 🎯 Why I Built This

Product and ops teams often have access to usage data—but it's messy and time-consuming to interpret.  
I built this tool to simulate what many internal teams need: a fast, digestible way to monitor product engagement and communicate findings.

---

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas
- OpenAI API
- CSV logs (simulated)

---

## ⚙️ How It Works

1. Upload a CSV log of user feature interactions  
2. The dashboard shows a bar chart of usage by feature  
3. Click a button to generate a GPT summary of adoption trends  

---

## 🗂 Sample Data Format

```csv
user_id,event_name,feature,timestamp
u1,click,UploadPhoto,2025-05-01 09:15:23
u2,click,UploadPhoto,2025-05-01 10:05:11
...
