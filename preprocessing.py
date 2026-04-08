from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def load_and_split_data():
    data = load_iris()
    X = data.data
    y = data.target
    return train_test_split(X, y, test_size=0.2, random_state=42)
