import joblib
model = joblib.load('salary.pk1')

exp = input("Enter exp for salary to predict : ")
predict = model.predict([[float(exp)]])

print(predict)