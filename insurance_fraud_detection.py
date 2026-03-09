'''this program uses a decision tree machine learning 
model to detect insurance fraud.'''


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Training dataset
data = {
    'claim_amount':[5000,20000,15000,3000,25000,4000,18000,7000],
    'customer_age':[25,45,35,22,50,28,40,30],
    'previous_claims':[0,2,1,0,3,0,2,1],
    'vehicle_age':[3,8,5,2,10,4,7,3],
    'fraud':[0,1,0,0,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[['claim_amount','customer_age','previous_claims','vehicle_age']]
y = df['fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Accuracy check
pred = model.predict(X_test)
accuracy = accuracy_score(y_test,pred)

print("Model Accuracy:",accuracy)

print("\n------ Insurance Fraud Detection ------")

# User input
claim_amount = int(input("Enter Claim Amount: "))
customer_age = int(input("Enter Customer Age: "))
previous_claims = int(input("Enter Previous Claims: "))
vehicle_age = int(input("Enter Vehicle Age: "))

result = model.predict([[claim_amount,customer_age,previous_claims,vehicle_age]])

if result[0]==1:
    print("⚠ Fraudulent Claim Detected")
else:
    print("✅ Genuine Claim")