# Welcome to eXtreme Design Testing

XDTesting is a test automation tool for the [eXtreme Design](https://extremedesign.info) ontology modelling methodology. This website provides material, instructions and examples for the XDTesting 1st Session, whose purpose is to test the tool, provide feedback and collect requirement from ontology engineers. 

## eXtreme Design and Conceptual Components

eXtreme Design (XD) is an ontology design methodology that puts the reuse of [Ontology Design Patterns (ODPs)](http://ontologydesignpatterns.org/wiki/Main_Page) at its core both as a principle and as an explicit activity. The main characterising principles of the method are intensive use of:

- ODPs
- Modular Design
- Test-driven approach.

A conceptual component (CC) is a complex (cognitive) relational structure that a designer implements in an ontology by using classes, properties, axioms, etc [1]. Conceptual components are cognitive objects: they are the intensional counterparts of OWL implementations in semantic web ontologies. A CC may
be implemented by means of different ontology fragments, the
observed ontology design patterns (OODPs), across different ontologies.

## eXtreme Design, a test-driven ontology modelling mothodology

One of the most important steps of each ontology modelling methodology, including eXtreme Design, is the testing of the ontology. The testing in XD includes the following tests:

- **Competency Question Verification** allows to verify if the ontology can answer the competency questions that have been collected during the requirement collection.
- **Inference Verification** allows to verify that the inference mechanisms are in place, to ensure the correct fulfillment of the inference requirement.
- **Error Provocation** allows to verify how the ontology acts when it is fed random or incorrect data. 

## Guidelines on using the XDTesting tool 

1. Create a repository of your own in GitHub. You can include a README.md file if you like. 
2. Copy the file XDTesting.yml from the [FiorelaCiroku/XDTesting](https://github.com/FiorelaCiroku/XD-Testing/blob/main/.github/workflows/XDTesting.yml) repository under the .github/workflows directory to your own repository under the same directory and file name. 
3. Create a directory named **ontology-network** which will have as subfolders the ontology modules. 
4. Create a directory named **module1** in the **ontology-network** directory. 
5. Add a README.md file and a file named UserInput.txt.
6. In the UserInput.txt file write the name of the new Conceptual Component that you want to test, for example CC1.
7. Wait a couple of second for the first automation to be completed. This automation will create a Pull request that you can find in the horizontal menu of GitHub. The Pull request consists on the creation of a directory structure for the testing of the conceptual component. The structure should be as shown below.

![Screenshot 2021-12-29 at 06 50 29](https://user-images.githubusercontent.com/12375920/147631401-d4ab9ebd-1215-4356-a351-ca22bfacd13c.png)
8. Merge the Pull request to the master branch of the repository. Quickly, you can see in the **module1** folder that a new folder was created with the name of the conceptual component. If you browse in the inside of the folder, you can verify that the structure shown above is the same as the one that you merged. 
- In the newly created folder, you should populate the test case files with real test cases. For the creation of the test case for competency question verification or else named SPARQL unit test, you should use the following template. The namespaces of the prefixes are: 1) om for ontology module, 2)td for toy dataset and 3) tc for testcase. 

```
@prefix owlunit: <https://w3id.org/OWLunit/ontology/> . 
@prefix om: .
@prefix td: .
@prefix tc: .
 
tc:xx a owlunit:CompetencyQuestionVerification ; 
      owlunit:hasCompetencyQuestion " " ; 
      owlunit:hasSPARQLUnitTest " " ; 
      owlunit:hasInputData td:xx ; 
      owlunit:hasInputTestDataCategory owlunit:ToyDataset ; 
      owlunit:hasExpectedResult " "; 
      owlunit:testsOntology om: . 
```
For the creation of the test case for inference verification, you can use this template. 

```
@prefix owlunit: <https://w3id.org/OWLunit/ontology/> .  
@prefix om: .
@prefix tc: .
@prefix td: .
  
tc:xx a owlunit:InferenceVerification ; 
      owlunit:hasInputData td:xx ; 
      owlunit:hasSPARQLUnitTest " " ; 
      owlunit:hasReasoner owlunit:HermiT ; 
      owlunit:hasExpectedResult true/false ; 
      owlunit:testsOntology om: . 
```

And lastly, for the creation of a test case for the error provocation test, you can use this template. 

```
@prefix owlunit: <https://w3id.org/OWLunit/ontology/> .  
@prefix om: .
@prefix tc: .
@prefix td: .
  
tc:xx a owlunit:ErrorProvocation ; 
      owlunit:hasInputData td:xx ; 
      owlunit:testsOntology om: . 
      
```

- For the purpose of this test you can use the following test case example. Copy and paste it to the test case file in the CQTestCase folder.

```
@prefix owlunit: <https://w3id.org/OWLunit/ontology/> .
@prefix ex: <https://w3id.org/OWLunit/examples/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

ex:cq1.ttl a owlunit:CompetencyQuestionVerification ;
 	owlunit:hasCompetencyQuestion "What are the interests of a certain person?" ;
 	owlunit:hasSPARQLUnitTest "PREFIX foaf: <http://xmlns.com/foaf/0.1/>  SELECT DISTINCT ?interest {?person foaf:interest ?interest}" ;
	owlunit:hasInputData ex:datacq1.ttl ;
	owlunit:hasInputTestDataCategory owlunit:ToyDataset ;
	owlunit:hasExpectedResult "{  \"head\": {  \"vars\": [  \"interest\" ] } ,  \"results\": {  \"bindings\": [ {  \"interest\": {  \"type\":  \"uri\" ,  \"value\":  \"https://w3id.org/OWLunit/examples/Basketball\" } } ] } }";
	owlunit:testsOntology foaf: .

```
- For the purpose of this test you can use the following toy dataset example. Copy and paste the text below to the to the toy dataset file in the CQDataSet folder.

```
@prefix ex: <https://w3id.org/OWLunit/examples/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

ex:Luigi foaf:interest ex:Basketball .

```

- If you want to add your own testcases and toydatasets, be aware to add the ontology to the OWLFile.owl file.  
- After you have created the test cases, the automation is triggered again. The actions that take place in the background are: 1) Input cross-check where we verify that all the necessary information for the running of the test is available, 2) Test environment setup, where the action downloads java and the OWLUnit jar, 3) Test run, and 4) Test documentation, where we report about the result of the test. 
- We ask from you to look closely to all the issues that you encounter during the testing of a conceptual component. We have created templates to make it easier for you to create issues [here](https://github.com/FiorelaCiroku/XD-Testing/issues). There is one template for bugs and one for features that you would like to have. 
- We have also opened several discussion boards [here](https://github.com/FiorelaCiroku/XD-Testing/discussions) to light up conversations regarding features, bugs, documentation and general feedback. We would really appreciate if you could participate in the dicussion boards. 




[1] https://dl.acm.org/doi/pdf/10.1145/3460210.3493542
