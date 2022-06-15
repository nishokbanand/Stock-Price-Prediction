import pickle
def initially(string):
    with open("model.pkl",'rb') as f:
        model=pickle.load(f)
        f.close()
    string=int(string)
    a= model.predict([[string]])
    return str(a[0])