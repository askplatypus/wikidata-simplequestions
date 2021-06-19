from SPARQLWrapper import SPARQLWrapper, JSON
import time
import json

endpoint = "https://query.wikidata.org/sparql"

sparql = SPARQLWrapper(endpoint)

locations = ['annotated_wd_data_test.txt','annotated_wd_data_test_answerable.txt','annotated_wd_data_valid.txt','annotated_wd_data_valid_answerable.txt','annotated_wd_data_train.txt','annotated_wd_data_train_answerable.txt']
for location in locations:
    f = open(location,'r')
    out = f.readlines()
    i = 0
    data = {}
    data['questions'] = []
    for line in out:
        i+=1
        print(i)
        arguments = line.split("\t")
        question = {}
        question['id'] = i
        question['knowledgebase'] = 'wikidata'

        q = []
        q_en = {}
        q_en['string'] = arguments[3]
        q_en['language'] = 'en'
        q.append(q_en)
        question['question'] = q
        query = {}
        query['answers'] = []

        if (arguments[1].startswith("P")):
            query['sparql'] =  "SELECT ?o1 WHERE { <http://www.wikidata.org/entity/"+arguments[0]+"> <http://www.wikidata.org/prop/direct/"+arguments[1]+"> ?o1 }"
            # sparql.setQuery(query['sparql'])
            # sparql.setReturnFormat(JSON)
            # result = sparql.query().convert()
            # query['answers'].append(result)
        if (arguments[1].startswith("R")):
            query['sparql']  = "SELECT ?s1 WHERE { ?s1 <http://www.wikidata.org/prop/direct/"+arguments[1].replace("R","P")+"> <http://www.wikidata.org/entity/"+arguments[0]+">}"
            # sparql.setQuery(query['sparql'])
            # sparql.setReturnFormat(JSON)
            # result = sparql.query().convert()
            # query['answers'].append(result)
        question['query'] = query
        data['questions'].append(question)
    with open('qald-format/'+location.replace('.txt','.json'), 'w') as outfile:
        json.dump(data, outfile, indent=4)