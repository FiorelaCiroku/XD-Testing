"""
SPARQL Queries be prepared (i.e parsed and translated to SPARQL algebra)
by the :meth:`rdflib.plugins.sparql.prepareQuery` method.

``initNs`` can be used instead of PREFIX values.

When executing, variables can be bound with the
``initBindings`` keyword parameter.
"""

import rdflib
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import FOAF
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from rdflib.namespace import DC
from rdflib.namespace import OWL
from rdflib.namespace import XSD

def SPARQLValidation(query):
    print("The variable is ", query)
    try:
        q = prepareQuery(query, initNs={"foaf": FOAF,"rdfs": RDFS, "rdf": RDF, "owl": OWL, "xsd": XSD},)
        print("Success!")
    
    except Exception as error:
        print("Error!")
                      
            
# query = "SELECT ?info ?name WHERE { ?person rdfs:seeAlso ?info . ?person foaf:homepage ?name .}"
# SPARQLValidation(query)
