from SPARQLWrapper import SPARQLWrapper,JSON

cat1 = 'Branche du droit'


def reqWrapper(cat):
    sparql = SPARQLWrapper("http://fr.dbpedia.org/sparql")
    req = 'select ?label where {?cat rdfs:label "' + cat + '"@fr .?subcat skos:broader ?cat.?subcat rdfs:label ?label.} LIMIT 1000'
    sparql.setQuery(req)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def reqRecursion(myResults):
    #print(myResults)
    if myResults["results"]["bindings"] != []:
        for result in myResults["results"]["bindings"]:
            print(result['label']['value'])
            return reqRecursion(reqWrapper(result['label']['value']))
    else:
        return "--------cat fini------------"
            #print(result["label"]["value"])



sparql2 = SPARQLWrapper("http://fr.dbpedia.org/sparql")
sparql2.setQuery("""
    select ?label where {
   ?cat rdfs:label "Systeme de castes en Inde"@fr .
   ?subcat skos:broader ?cat.
   ?subcat rdfs:label ?label.
} LIMIT 1000
""")
print("#####################################")
sparql2.setReturnFormat(JSON)
results = sparql2.query().convert()
print(results)
if results["results"]["bindings"] == []:
    print(True)

#tree = parse(results)

results1 = reqWrapper(cat1)
#print(results1)
print(reqRecursion(results1))
