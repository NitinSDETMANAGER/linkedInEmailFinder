# 🔎 LinkedIn Email Finder using Apollo API

Author: Nitin Choudhary

## 📌 Description
A simple Python script to fetch **verified email addresses** from **LinkedIn profile URLs** using [Apollo.io](https://apollo.io)'s public API.

## 🚀 How to Use

1. ✨ Go to [https://apollo.io](https://apollo.io)
2. 🔐 Create a free account
3. ⚙️ Go to your [API Dashboard](https://docs.apollo.io/reference/people-enrichment) and generate your free API key
4. 🧠 Paste the key inside `emailFetch.py` → `API_KEY = "..."`

### Run the script

```bash
pip install -r requirements.txt
python emailFetch.py
```

Enter any LinkedIn URL when prompted and the system will return an email (if found).

## 📁 Project Structure

```
linkedInEmailFinder/
├── emailFetch.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📄 License
Free to use for educational or research purposes.

---
Made with 💻 by Nitin Choudhary
