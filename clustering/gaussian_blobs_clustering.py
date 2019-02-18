from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=60, centers=4, n_features=5, random_state=0, center_box=(1,10))

print(X)
print(y)
