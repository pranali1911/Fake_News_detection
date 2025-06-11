# Fake_News_detection

### 🧾 **Objective**:

The objective of this project is to build a web-based application that automatically classifies news articles as **real** or **fake** using natural language processing (NLP) and machine learning algorithms.

---

### 🧠 **Learning Outcomes**:

* Understanding of **text classification** using NLP.
* Implementation of **TF-IDF vectorization**.
* Training and evaluation of models like **Logistic Regression** and **Decision Tree Classifier**.
* Deployment of a user-friendly web application using **Streamlit**.

---

### 🗃️ **Dataset**:

* **Name**: Real and Fake News Dataset
* **Source**: [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
* **Features Used**: `text`, `label`
* **Labels**: `REAL` (1) and `FAKE` (0)

---

### ⚙️ **Tools and Technologies Used**:

* **Programming Language**: Python
* **Libraries**:

  * `scikit-learn` for machine learning models
  * `nltk` for text preprocessing
  * `joblib` for model saving/loading
  * `Streamlit` for web interface
* **Modeling Techniques**:

  * TF-IDF Vectorizer
  * Logistic Regression
  * Decision Tree Classifier

---

### 🔍 **Approach**:

1. **Data Cleaning & Preprocessing**:

   * Removed null and duplicate values.
   * Converted text to lowercase, removed punctuation, stopwords, etc.

2. **Feature Extraction**:

   * Used **TF-IDF Vectorization** to convert text into numerical features.

3. **Model Training**:

   * Trained two models: `Logistic Regression` and `Decision Tree`.
   * Evaluated models using `accuracy`, `precision`, `recall`, and `F1-score`.

4. **Web App Interface**:

   * Created a simple user interface using **Streamlit**.
   * Users input a news article, and the app classifies it as **Fake** or **Real**.

---

### 📊 **Results**:

* Both models performed well on test data.
* **Logistic Regression** gave slightly better performance compared to **Decision Tree**.
* Accuracy scores:

  * Logistic Regression: \~92%
  * Decision Tree Classifier: \~88%

---

### 🧪 **Sample Prediction**:

![image](https://github.com/user-attachments/assets/44c1b7b3-27e7-4b89-a793-ad04ccdedd01)




![image](https://github.com/user-attachments/assets/cca280d8-46c6-4626-8d29-a9f5f5e5bd55)


---

### 🌐 **Web App Functionality**:

* Input text box to paste news.
* "Check News" button for prediction.
* Model displays whether the news is **Real** or **Fake**.

---

### 📁 **Project Folder Structure**:

```
FakeNewsApp/
├── app.py                  # Streamlit app
├── vectorizer.jb           # TF-IDF vectorizer
├── lr_model.jb             # Logistic Regression model
├── DTC_model.jb            # Decision Tree model
├── style.css               # Optional custom styling
└── report.pdf              # Project report
```

---

### ✅ **Conclusion**:

This project demonstrates the effective use of **text analysis** and **machine learning** for the real-world problem of **fake news detection**. It provides an accessible tool that can assist in verifying the credibility of online content.

