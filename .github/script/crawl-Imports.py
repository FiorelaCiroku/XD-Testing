# To install SPARQLWrapper use: pip install SPARQLWrapper in the command line

# Import the SPARQLWrapper package
from SPARQLWrapper import SPARQLWrapper, JSON

# Declare the wrapper
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

# Insert query that is to be executed

sparql.setQuery("""
    SELECT ?ImportedModule
    WHERE { 
       ?module a owl:Ontology .
       ?ImportedModule a owl:Ontology .
       ?module owl:imports ?ImportedModule .
       
    }
""")
# Set return format of the results
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# Print the results
for result in results["results"]["bindings"]:
    print(result["label"]["value"])
