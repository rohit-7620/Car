

from sklearn.preprocessing import StandardScaler

def load_and_split_data():
    data = load_iris()
    X = data.data
    y = data.target

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return train_test_split(X, y, test_size=0.2, random_state=42)
