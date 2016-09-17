import cgi
import json
import gensim

form = cgi.FieldStorage()
spot = form.getvalue('id')

model = gensim.models.doc2vec.Doc2Vec.load("cgi-bin/model.txt")
simVecs = {}

for spot in model.docvecs.most_similar(int(spot)):
    simVecs[str(spot[0])] = spot[1]

print ("Content-type:application/json\n")
print(json.dumps(simVecs, indent = 2))

file = open("cgi-bin/output.json", "w")
json.dump(simVecs, file, indent = 2) 