# 🎓 Placement Prediction Model

A simple end-to-end Machine Learning project that predicts student placement outcomes using the **placement.csv** dataset.

This project demonstrates the complete ML workflow from preprocessing to deployment.

---

## 🚀 Project Workflow

The following steps were performed:

### ✅ Step 0 — Preprocessing + EDA + Feature Selection

* Loaded dataset (`placement.csv`)
* Checked missing values
* Performed Exploratory Data Analysis (EDA)
* Selected relevant features for modeling

---

### ✅ Step 1 — Extract Input and Output Columns

* **Input features (X)** selected from dataset
* **Target variable (y)** extracted for prediction

Example:

```python
X = df[['cgpa']]
y = df['placement']
```

---

### ✅ Step 2 — Feature Scaling

* Applied scaling to normalize feature values
* Helps many ML algorithms perform better

```python
from sklearn.preprocessing import StandardScaler
```

---

### ✅ Step 3 — Train-Test Split

* Split dataset into training and testing sets
* Prevents overfitting
* Enables unbiased evaluation

```python
from sklearn.model_selection import train_test_split
```

---

### ✅ Step 4 — Model Training

* Trained ML model on training data
* Example models that may be used:

  * Logistic Regression
  * Decision Tree
  * Random Forest

---

### ✅ Step 5 — Model Evaluation / Selection

Model performance evaluated using appropriate metrics such as:

* Accuracy
* Confusion Matrix
* Precision / Recall

Best performing model selected.

---

### ✅ Step 6 — Model Deployment

* Final model saved using **pickle/joblib**
* Ready for inference or integration into applications

Example:

```python
import pickle
pickle.dump(model, open('model.pkl', 'wb'))
```

---

# 📊 Dataset

**File:** `placement.csv`

Typical features may include:

* CGPA
* IQ
* Placement status (target)

*(Update this section if your columns are different)*

