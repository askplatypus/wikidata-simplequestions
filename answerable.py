from SPARQLWrapper import SPARQLWrapper, JSON
import time

endpoint = "https://query.wikidata.org/sparql"

sparql = SPARQLWrapper(endpoint)

f = open("annotated_wd_data_test.txt",'r')
F = open("annotated_wd_data_test_answerable2.txt","w")
out = f.readlines() # will append in the list out
i = 0
for line in out:
    i+=1
    print(i)
    arguments = line.split("\t")
    if (arguments[1].startswith("P")):
        query = "ASK where { <http://www.wikidata.org/entity/"+arguments[0]+"> <http://www.wikidata.org/prop/direct/"+arguments[1]+"> <http://www.wikidata.org/entity/"+arguments[2]+">}"
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        print(result['boolean'])
        if (str(result['boolean'])=='True'):
            print("This is true")
            F.write(line)
    if (arguments[1].startswith("R")):
        query = "ASK where { <http://www.wikidata.org/entity/"+arguments[2]+"> <http://www.wikidata.org/prop/direct/"+arguments[1].replace("R","P")+"> <http://www.wikidata.org/entity/"+arguments[0]+">}"
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        print(result['boolean'])
        if (str(result['boolean'])=='True'):
            print("This is true")
            F.write(line)
F.close()