# DecodeLabs - AI Internship 
# Project 2 - Data Classification Using AI
# Name: Chottu Mukati
# Algorithm: K-Nearest Neighbors (KNN)
# Dataset: Iris Dataset

# Import required libraries

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score

# Load Iris Dataset
iris = load_iris()

# Features (X)
X = iris.data

# Target (y)
y = iris.target

print("Dataset Loaded Successfully!")
print("Number of Samples:", len(X))
print("Number of Features:", X.shape[1])
print("Target Classes:", iris.target_names)

# Split the dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nDataset Split Successfully!")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Scale the features

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nFeature Scaling Completed!")

# Create the KNN model

model = KNeighborsClassifier(n_neighbors=5)

# Train the model

model.fit(X_train, y_train)

print("Model Trained Successfully!")

# Make predictions

y_pred = model.predict(X_test)

print("Prediction Completed!")

# Evaluate the model

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("F1 Score:", f1_score(y_test, y_pred, average="weighted"))