# Welcome to eXtreme Design Testing

XDTesting is a test automation tool for the [eXtreme Design](https://extremedesign.info) ontology modelling methodology. This website provides material, instructions and examples for the XDTesting 1st Session, whose purpose is to test the tool, provide feedback and collect requirements from ontology engineers. 

## eXtreme Design and Conceptual Components

eXtreme Design (XD) is an ontology design methodology that puts the reuse of [Ontology Design Patterns (ODPs)](http://ontologydesignpatterns.org/wiki/Main_Page) at its core both as a principle and as an explicit activity. The main characterising principles of the method are intensive use of:

- ODPs
- Modular Design
- Test-driven approach.

## eXtreme Design, a test-driven ontology modelling mothodology

One of the most important steps of each ontology modelling methodology, including eXtreme Design, is the testing of the ontology. The testing in XD includes the following tests:

- **Competency Question Verification** allows to verify if the ontology can answer the competency questions that have been collected during the requirement collection.
- **Inference Verification** allows to verify that the inference mechanisms are in place, to ensure the correct fulfillment of the inference requirement.
- **Error Provocation** allows to verify how the ontology acts when it is fed random or incorrect data. 

## Guidelines on using the XDTesting tool 

1. Create a repository of your own in GitHub. You can include a README.md file if you prefer. 
2. Copy the files XDTesting.yml and Directory.yml from the [FiorelaCiroku/XDTesting](https://github.com/FiorelaCiroku/XD-Testing/blob/main/.github/workflows/) GitHub repository and add them to a directory named .github/workflows in your repository (same as in the original repository).
3. Create a directory named **ontology-network** which will have as subfolders the ontology modules. 
4. Create a directory named **musical-performance** in the **ontology-network** directory. 
5. Add a README.md file and a file named UserInput.txt under the **musical-performance** directory.
6. In the UserInput.txt file write the name of the new ontology fragment that you want to test, for example **RecordingProcess**.
7. Wait a couple of second for the first automation to be completed. This automation will create a Pull request that you can find in the horizontal menu of GitHub. The Pull request consists on the creation of a directory structure for the testing of the ontology fragment. The structure should be as shown below.<img width="300" alt="image" src="https://user-images.githubusercontent.com/12375920/154559169-734e28f7-ef02-43cf-8439-2d4d30d1d6a4.png">
8. Merge the Pull request to the master branch of the repository. Quickly, you can see in the **musical-performance** folder that a new folder was created with the name of the ontology fragment. If you browse in the inside of the folder, you can verify that the structure shown above is the same as the one that you merged. 
9. In the newly created folder, you should populate the input files. In the CompetencyQuestions.txt, add `CQ01: Which recording is produced by a session?`. 
10. In the SPARQLQueries.txt, add `SQCQ01: PREFIX mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> SELECT DISTINCT ?recording WHERE {?session mp:isSessionOf ?recordingProcess . ?recordingProcess mp:producesRecording ?recording }` and `SQIV01: PREFIX mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> PREFIX td: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/InferenceVerificationTest/IVDataSet/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ASK { td:Session01 a mp:Session }" ; owlunit:hasExpectedResult true ; owlunit:hasReasoner owlunit:HermiT ; owlunit:testsOntology mp: .`.
11. In the ExpectedResults.txt file, add `ER01: {  \"head\": {  \"vars\": [  \"recording\" ] } ,  \"results\": {  \"bindings\": [ {  \"recording\": {  \"type\":  \"uri\" ,  \"value\":  \”https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/SPARQLUnitTest/CQDataSet/ComeWithMe\" } } ] } `.
12. In the GeneralConstraints.txt file, add `IV01: Session01 is a Session. ` and `ER01: RecordingProcess120  is a recording process and not a recording. `.
13. Add the ontology in the RecordingProcess.owl file. The ontology can be found in this [link](https://drive.google.com/file/d/1yHWstifYpPlByf1esQ_J9vGEvE4gZx1f/view?usp=sharing). 
14. Lastly, add the test data as follows. The first toy dataset is for the competency question verification test, the second for the inference verification test and the third for error provocation test. 

```
@prefix td: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/SPARQLUnitTest/CQDataSet/>. @prefix tc: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/SPARQLUnitTest/CQTestCase/>.
@prefix mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> .

td:Session01 mp:isSessionOf td:RecordingProcess120 . 
td:RecordingProcess120 mp:producesRecording td:ComeWithMe .

```
```
@prefix mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> .
@prefix td: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/InferenceVerificationTest/IVDataSet/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

td:Session01 a mp:Session .

```

```
@prefix mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> .
@prefix td: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/ErrorProvocationTest/EPDataSet/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

td:RecordingProcess120 a mp:RecordingProcess .
td:RecordingProcess120 a mp:Recording .

```

If you like to create your own test cases, make sure to use this format for competency question verification or else named SPARQL unit test, you should use the following template. The namespaces of the prefixes are: 1) om for ontology module, 2)td for toy dataset and 3) tc for testcase. 

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

- If you want to add your own testcases and toydatasets, be aware to add the ontology owl file.  
- After you have created the test cases, the automation is triggered again. The actions that take place in the background are: 1) Input cross-check where we verify that all the necessary information for the running of the test is available, 2) Test environment setup, where the action downloads java and the OWLUnit jar, 3) Test run, and 4) Test documentation, where we report about the result of the test. 

## Sharing feedback

- Pay attention to all problems that you encounter during the session. We have created [GitHub issue templates](https://github.com/FiorelaCiroku/XD-Testing/issues) to make it easier for you to describe the problems. There is one template for bugs and one for features that you would like to have. 

- We have also opened several discussion boards [here](https://github.com/FiorelaCiroku/XD-Testing/discussions) to light up conversations regarding features, bugs, documentation and general feedback. We would really appreciate if you could participate in the dicussion boards. 

- Another way to share your feedback is on my channel on Discord. 

## Features under development

- Construct and run integration tests
- Integrate tested ontology fragments to module
- Adapt the tool to work with ontologies that are not structured in the same way


