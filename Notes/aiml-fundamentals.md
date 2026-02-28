Below are your notes **cleaned, corrected, and formatted** so you can directly paste into `notes/aiml-fundamentals.md` on GitHub.

---

# 🤖 AI vs ML vs DL Notes

---

## 📌 Artificial Intelligence (AI)

Artificial Intelligence (AI) is the process of creating machines or systems that behave like human beings by mimicking human intelligence and abilities.

These machines are designed to perform tasks that typically require human thinking, such as:

* Understanding language
* Recognizing images
* Solving problems
* Learning from experience
* Making decisions

---

## 🔹 Types of AI

### 1️⃣ Narrow AI (Weak AI)

Narrow AI refers to AI systems that are specialized to perform one specific task or a narrow range of tasks. They are highly efficient at those particular tasks but cannot perform outside their designed scope.

**Examples:**

* Siri or Alexa (voice assistants designed for voice commands)
* Recommendation algorithms on platforms like Netflix or Amazon
* Facial recognition software
* ChatGPT (designed primarily for conversational tasks)

✅ Most AI systems today are Narrow AI.

---

### 2️⃣ General AI (Strong AI)

General AI is a theoretical form of artificial intelligence that has the ability to understand, learn, and perform any intellectual task that a human being can.

**Key characteristics:**

* Ability to reason and plan
* Solve problems across domains
* Transfer learning between unrelated tasks
* Adapt to new environments without retraining

📌 Example (hypothetical):
A General AI could drive a car, diagnose diseases, design systems, and hold conversations — all like a human.

🚨 **Important:** General AI does NOT currently exist.

---

# 📌 Machine Learning (ML)

Machine Learning is the study of algorithms that learn from data and make predictions on unseen data.

👉 In simple words: **Machine learns from data instead of being explicitly programmed.**

Machine Learning is a **subset of AI**.

⚠️ ML models can become outdated when real-world data changes (concept drift).

---

## 🔄 Traditional Programming vs Machine Learning

**Traditional Programming**

```
Data + Rules → Output
```

**Machine Learning**

```
Data + Output → Model learns Rules
```

---

# 📌 Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from large amounts of data.

**Common use cases:**

* Computer Vision
* Natural Language Processing
* Speech Recognition
* Generative AI

---

## 🧠 Relationship Hierarchy

```
Artificial Intelligence
    └── Machine Learning
            └── Deep Learning
```

---

# 📊 Data Mining

Data mining is the process of using AI, machine learning, and statistics to analyze large datasets and uncover hidden patterns, trends, and correlations for business insights and predictive analysis.

---

# 📚 ML Algorithms

### 🔹 Classification

Used to predict **categorical values**
Example: spam vs not spam

### 🔹 Regression

Used to predict **continuous values**
Example: house price prediction

### 🔹 Clustering

Used to find logical groups in data
Example: customer segmentation

---

# 🧪 Types of Machine Learning

---

## 1️⃣ Supervised Learning

Supervised learning is a type of learning where the model is trained using labeled data.

### How it works

* Feed input–output pairs (X, y)
* Compute loss (difference between predicted ŷ and actual y)
* Update parameters using optimization (e.g., Gradient Descent)
* Repeat until loss is minimized

### Types

* **Classification** → target is categorical
* **Regression** → target is numerical

---

## 2️⃣ Unsupervised Learning

Unsupervised learning is a type of ML where the model is trained on unlabeled data. It is used to discover hidden patterns or group similar data.

### How it works

* Provide input data X (no labels)
* Model finds similarities and patterns
* Organizes data into groups or reduces dimensions

**Example:**
Grouping customers by buying habits.

### Types

* Clustering
* Dimensionality Reduction
* Anomaly Detection

---

## 3️⃣ Semi-Supervised Learning

Semi-supervised learning uses both labeled and unlabeled data.

👉 Usually:

* Small amount of labeled data
* Large amount of unlabeled data

Used when labeling is expensive.

---

## 4️⃣ Reinforcement Learning

Reinforcement learning is a type of ML where an agent learns by interacting with an environment and receiving rewards or penalties.

**Example:**
Self-driving car improves driving based on rewards for safe actions.

### How it works

1. Agent observes state
2. Agent takes action
3. Environment gives reward/penalty
4. Agent updates policy
5. Repeat until optimal strategy is learned

---

# ⚙️ ML Training Approaches

---

## 🔹 Batch Machine Learning

* Model is trained using the entire dataset at once
* Training happens offline
* Model is not updated continuously
* Needs retraining when new data arrives

**Disadvantages**

* Hardware limitations
* High memory usage
* Not suitable for streaming data

---

## 🔹 Online Machine Learning

Online ML is a learning approach where the model is trained incrementally as new data arrives.

**Key points**

* Continuous learning
* Updates in small steps
* Best when data changes frequently

📌 Online ML is ideal for real-time systems.

---

# 🧠 Instance-Based vs Model-Based Learning

## Instance-Based Learning

* Stores training examples
* Prediction made by comparing with stored data
* Uses similarity measures

**Pros**

* Flexible
* Adapts quickly

**Cons**

* Memory intensive
* Slow prediction

---

## Model-Based Learning

* Learns a generalized model
* Uses parameters or rules
* Does not store all training data

**Pros**

* Fast prediction
* Less memory

**Cons**

* Training can be expensive
* May require retraining

---

# 🔄 ML Development Cycle (MLDC)

1. Framing the problem
2. Gathering data
3. Data preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature engineering and selection
6. Model training and evaluation
7. Model deployment
8. Testing
9. Optimization

---

# 👩‍💻 Role of ML Engineer

ML Engineers are responsible for:

* Deploying ML models to production
* Scaling and optimizing models
* Monitoring model performance
* Maintaining and retraining models

---

# 🧮 Tensors in Practical ML

Tensors are multi-dimensional data structures used to store data in ML and DL.

👉 Number of axes = rank = dimension

---

## 🔹 0D Tensor (Scalar)

* Single value
* No axes

**Example**

```
3
```

---

## 🔹 1D Tensor (Vector)

* One axis
* Shape example: (4)

**Example**

```
[3, 4, 5, 6]
```

---

## 🔹 2D Tensor (Matrix)

* Two axes (rows and columns)

**Example**

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

---

## 🔹 3D Tensor

* Three axes
* Stack of matrices

**Examples**

* RGB images → (height × width × channels)
* Time-series batches

---

# 📦 Applications of ML

* Retail
* Banking and Finance
* Transport
* Manufacturing
* Consumer Internet
