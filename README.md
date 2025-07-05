# 🕵️ Fraudulent Transactions Detection

This project is a machine learning-based solution to detect fraudulent financial transactions using models like **Random Forest**, **Logistic Regression** and **XGBoost**. It includes preprocessing, scaling, model training, and a basic web interface to test predictions on transaction data.

---

## 📂 Project Structure

```
Fraudulent-Transactions-Detection/
├── static/
│   └── style.css                         
├── Templates/
│   ├── index.html
│   ├── input.html
│   └── output.html                  
├── Train_data/                      
│   ├── fraudTrain.csv
│   └── fraudTest.csv
├── app.py                            
├── fraud.ipynb                           
├── model.pkl
├── scaler.pkl
```

---

## 🧠 Models Used

- **Logistic Regression**
- **XGBoost Classifier**
- **Random Forest**

These models are trained on labeled transaction data to distinguish between legitimate and fraudulent transactions.

---

## 🗃️ Dataset

The dataset is stored in the `Train_data/` folder:
- `fraudTrain.csv` – training data
- `fraudTest.csv` – testing/validation data

Each dataset includes transaction features such as amount, category, merchant info, and a label indicating fraud (1) or not (0).

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Flask (for web deployment)
- HTML/CSS (used in Templates and static folders)

---

## 🚀 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/JayanthSrinivas06/Fraudulent-Transactions-Detection.git
cd Fraudulent-Transactions-Detection
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Flask app**
```bash
python app
```

4. **Visit the web interface**

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## 📈 Results

Both models are evaluated using metrics like:
- Accuracy
- Precision & Recall
- Confusion Matrix

XGBoost generally provides better accuracy and recall for fraud detection tasks.

---

## 📬 Contact

Developed by **Jayanth Srinivas Bommisetty**  
For questions or suggestions, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/jayanth-srinivas-b-0b7911269/)

---

⭐ Star this repo if you found it useful!
