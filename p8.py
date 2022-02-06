from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
 
iris_dataset = load_iris()
print("iris features \ target names \n", iris_dataset.target_names)
 
for i in range(len(iris_dataset.target_names)):
    print('[{0}]:[{1}]'.format(i, iris_dataset.target_names[i]))
 
print("Iris data: \n", iris_dataset["data"])
 
x_train, x_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state = 0)
 
print("\nTarget \n", iris_dataset["target"])
print("\n xTrain \n", x_train)
print("\n xtest \n", x_test)
print("\n y_train \n", y_train)
print("\n y_test \n", y_test)
 
kn = KNeighborsClassifier(n_neighbors = 5)
kn.fit(x_train, y_train)
x_new = np.array([[5, 2.9, 1, 0.2]])
print("\nX_new \n", x_new)
prediction = kn.predict(x_new)
 
print("\nPredicted Feature : {}\n".format(prediction))
print("\nPredicted Feature Name: {}\n".format(iris_dataset['target_names'][prediction]))
 
i = 1
x = x_test[i]
x_new = np.array([x])
print("\nX_new \n", x_new)
 
for i in range(len(x_test)):
    x = x_test[i]
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    print("actual : {0} {1}, pred : {2}{3}".format(y_test[i], iris_dataset["target_names"][y_test[i]], prediction, iris_dataset["target_names"][prediction]))
print("test score[accuracy]: {:.2F}\n".format(kn.score(x_test, y_test)))