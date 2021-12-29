# Welcome to eXtreme Design Testing

This website is created to present the work regarding the test automation for the [eXtreme Design](https://extremedesign.info) ontology modelling methodology.

## eXtreme Design and Ontology Design Patterns

eXtreme Design (XD) is an ontology design methodology that puts the reuse of [Ontology Design Patterns (ODPs)](http://ontologydesignpatterns.org/wiki/Main_Page) at its core both as a principle and as an explicit activity. The main characterising principles of the method are intensive use of:

- ODPs
- Modular Design
- Test-driven approach.

ODPs provide solutions to recurrent modelling issues. ODPs are small ontologies that mediate between use cases (problem types) and design solutions. They are used as modelling components: ideally, an ontology results from a composition of ODPs, with appropriate dependencies between them, plus the necessary design expansion based on specific needs. If you are not familiar with ODPs, they can be found on catalogues, such as:

- The [catalogue](http://www.gong.manchester.ac.uk/odp/html/) maintained by the University of Manchester
- The [Ontology Design Pattern Portal](http://ontologydesignpatterns.org/wiki/Main_Page)
- The [Workshop on Ontology Design and Patterns series](http://ontologydesignpatterns.org/wiki/WOP:Main).


Modular design consists on eparating the representation of requirements into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired requirement.

## eXtreme Design, a test-driven ontology modelling mothodology

One of the most important steps of each ontology modelling methodology, including eXtreme Design, is the testing of the ontology. The testing in XD includes the following tests:

- **Competency Question Verification** allows to verify if the ontology can answer the competency questions that have been collected during the requirement collection.
- **Inference Verification** allows to verify that the inference mechanisms are in place, to ensure the correct fulfillment of the inference requirement.
- **Error Provocation** allows to verify how the ontology acts when it is fed random or incorrect data. 

# Guidelines on using the automation for the testing of the ontologies

The first thing that you have to do is it access the repository of the testing. The repository can be found in the link 
