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
