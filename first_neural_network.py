

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import numpy as np

# 1. Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Normalize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Build Neural Network
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),  # input + hidden layer
    Dense(8, activation='relu'),                     # hidden layer
    Dense(3, activation='softmax')                   # output layer
])

# 5. Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 6. Train model
model.fit(X_train, y_train, epochs=50, verbose=1)

# 7. Predictions
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# 8. Accuracy
accuracy = accuracy_score(y_test, y_pred_classes)

print("Model Accuracy:", accuracy)