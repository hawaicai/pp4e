import pickle, glob
for filename in glob.glob('*.pkl'):  # 针对 bob， sue， tom
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])  # 获取sue的名字
