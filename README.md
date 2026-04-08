Pr 2 : STEP 1: Clone Repo
git clone https://github.com/rohit-7620/Car.git
cd Car
📁 STEP 2: Create ML Project Structure
mkdir data models
touch main.py model.py preprocessing.py
🧠 STEP 3: Add RUNNABLE ML CODE
✅ preprocessing.py
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def load_and_split_data():
    data = load_iris()
    X = data.data
    y = data.target
    return train_test_split(X, y, test_size=0.2, random_state=42)
✅ model.py
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
✅ main.py
from preprocessing import load_and_split_data
from model import train_model
from sklearn.metrics import accuracy_score

def main():
    X_train, X_test, y_train, y_test = load_and_split_data()
    model = train_model(X_train, y_train)

    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)

    print("Accuracy:", acc)

if __name__ == "__main__":
    main()
▶️ STEP 4: Run Project
pip install scikit-learn
python main.py
✅ STEP 5: Initial Commit (Main Branch)
git add .
git commit -m "Initial ML project setup"
git push origin main
🌿 STEP 6: Create Feature Branch 1 (Preprocessing Team)
git checkout -b feature-preprocessing

👉 Update preprocessing.py:

from sklearn.preprocessing import StandardScaler

def load_and_split_data():
    data = load_iris()
    X = data.data
    y = data.target

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return train_test_split(X, y, test_size=0.2, random_state=42)
git add .
git commit -m "Added scaling in preprocessing"
git push -u origin feature-preprocessing
🌿 STEP 7: Create Feature Branch 2 (Model Team)
git checkout main
git checkout -b feature-model

👉 Update model.py:

from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model
git add .
git commit -m "Changed model to Logistic Regression"
git push -u origin feature-model
🔀 STEP 8: Merge Feature Branch 1
git checkout main
git pull origin main
git merge feature-preprocessing
git push origin main
⚠️ STEP 9: Merge Feature Branch 2 (Conflict)
git merge feature-model

👉 Conflict in model.py:

<<<<<<< HEAD
model = RandomForestClassifier()
=======
model = LogisticRegression(max_iter=200)
>>>>>>> feature-model
🛠️ STEP 10: Resolve Conflict

👉 Final model.py:

from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    return model
git add model.py
git commit -m "Resolved conflict and finalized model"
🚀 STEP 11: Push Final Code
git push origin main
🧹 STEP 12: Delete Feature Branches
git branch -d feature-preprocessing
git branch -d feature-model

git push origin --delete feature-preprocessing
git push origin --delete feature-model
🎯 FINAL OUTPUT (WHAT YOU ACHIEVED)

✔ Created ML project from scratch
✔ Created separate feature branches
✔ Worked like multiple team members
✔ Merged branches into main
✔ Handled merge conflict professionally

🔥 BONUS (VERY IMPORTANT FOR YOUR PROFILE)
Add .gitignore
touch .gitignore
__pycache__/
*.pkl
*.csv
.env
git add .gitignore
git commit -m "Added gitignore"
git push origin main
