#python2

from SPARQLWrapper import SPARQLWrapper,JSON

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

def parcour(myResults):
    for n1 in myResults["results"]["bindings"]:
        print("\t", n1["label"]["value"])
        re2=reqWrapper(n1["label"]["value"])
        if re2["results"]["bindings"] != []:
            for n2 in re2["results"]["bindings"]:
                print("\t\t", n2['label']['value'])
                re3=reqWrapper(n2['label']['value'])
                if re3["results"]["bindings"] != []:
                    for n3 in re3["results"]["bindings"]:
                        print("\t\t\t", n3['label']['value'])
                        re4=reqWrapper(n3['label']['value'])
                        for n4 in re4["results"]["bindings"]:
                            print("\t\t\t\t", n4['label']['value'])

def main():
    cat1 = 'Branche du droit'
    cat2 = 'Organisation de la Justice'
    cat3 = 'Organisation juridique'
    cat4 = 'Métier du droit'
    cat5 = 'Personnalité du droit'
    results1 = reqWrapper(cat1)
    results2 = reqWrapper(cat2)
    results3 = reqWrapper(cat3)
    results4 = reqWrapper(cat4)
    results5 = reqWrapper(cat5)
    #print(results1)
    #print(reqRecursion(results1))

    print(cat1)
    parcour(results1)
    print(cat2)
    parcour(results2)
    print(cat3)
    parcour(results3)
    print(cat4)
    parcour(results4)
    print(cat5)
    parcour(results5)

    




if __name__ == '__main__':
    main()
