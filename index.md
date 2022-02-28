# XDTesting

XDTesting is a test automation tool for the [eXtreme Design](https://extremedesign.info) ontology modelling methodology. This website provides material, instructions and examples for the XDTesting 1st Session, whose purpose is to test the tool, provide feedback and collect requirements from ontology engineers. 

## eXtreme Design

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

1. For the purpose of this testing session, we have created a dummy repository that contains the basic environment for the XDTesting tool to work. Fork the [XDTestingSession](https://github.com/FiorelaCiroku/XDTestingSession) repository in your own repository. To do so, click on the link, then on the fork button and confirm. The repository that you just forked contains a .github/workflow folder where you will find three workflows. The **create-directory** workflow creates a directory structure that contains folders for all types of tests based on XD and for each type of test there are subfolders about the test cases and toy dataset. Within this workflow you can also see the structure of directories that have been created by the automation. The workflow creates a Pull Request containing the new directories that were created. The **XDTesting** workflow checks if all necessary input to construct a test case is provided by the user, validates the syntax of the input, constructs the test cases and creates a pull request for the ontology engineer to merge. The **run-test** workflow constructs the URLs of the testcases, runs the testcases and documents the result. While in the folder **ontology-network**, the ontology modules that are part of the network can be found. Inside each folder of a module, there is a UserInput.txt file where you can add the name of the ontology fragment of the module that you want to test. 
2. In the UserInput.txt file write the name of the new ontology fragment that you want to test, for example **RecordingProcess**. You can do this by clicking on the file, click the edit button and write the name. After writting the name, click the Submit button at the end of the page.
3. Wait a couple of second for the first automation to be completed. This automation will create a Pull request that you can find in the horizontal menu of GitHub. The Pull request consists on the creation of a directory structure for the testing of the ontology fragment. The structure should be as shown below.<img width="300" alt="image" src="https://user-images.githubusercontent.com/12375920/154559169-734e28f7-ef02-43cf-8439-2d4d30d1d6a4.png"> To check the structure of the directory that is created, you can go to the Actions tab, click on the Directory workflow and then click on the job. The step that you need to open to see the structure of the directory is display-directory-structure.
4. Merge the Pull request to the master branch of the repository. What you need to do is to click on Pull requests, click on the item that you find there, click the merge button and confirm. Quickly, you can see in the **musical-performance** folder that a new folder was created with the name of the ontology fragment. If you browse in the inside of the folder, you can verify that the structure shown above is the same as the one that you merged. 
5. In order for the system to construct the test cases and later on execute them, it needs information from you. You should populate the input files. In the CompetencyQuestions.txt, add ```CQ01: Which recording is produced by a session?``` 
6. In the SPARQLQueries.txt, add ```SQCQ01: PREFIX mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> SELECT DISTINCT ?recording WHERE {?session mp:isSessionOf ?recordingProcess . ?recordingProcess mp:producesRecording ?recording }``` and ```SQIV01: PREFIX mp: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/RecordingProcess.owl> PREFIX td: <https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/InferenceVerificationTest/IVDataSet/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ASK { td:Session01 a mp:Session }" ; owlunit:hasExpectedResult true ; owlunit:hasReasoner owlunit:HermiT ; owlunit:testsOntology mp: .``` 
7. In the ExpectedResults.txt file, add ```ER01: {  \"head\": {  \"vars\": [  \"recording\" ] } ,  \"results\": {  \"bindings\": [ {  \"recording\": {  \"type\":  \"uri\" ,  \"value\":  \"https://raw.githubusercontent.com/YourUsername/YourRepository/main/ontology-network/musical-performance/RecordingProcess/SPARQLUnitTest/CQDataSet/ComeWithMe\" } } ] } }```.
8. In the GeneralConstraints.txt file, add ```IV01: Session01 is a Session. ``` and ```ER01: RecordingProcess120  is a recording process and not a recording. ``` .
9. Add the ontology in the RecordingProcess.owl file. The ontology can be found in this [link](https://drive.google.com/file/d/1yHWstifYpPlByf1esQ_J9vGEvE4gZx1f/view?usp=sharing). 
10. Lastly, add the test data as follows. The first toy dataset is for the competency question verification test, the second for the inference verification test and the third for error provocation test. 

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

## Create own test cases

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

And for the creation of a test case for the error provocation test, you can use this template. 

```
@prefix owlunit: <https://w3id.org/OWLunit/ontology/> .  
@prefix om: .
@prefix tc: .
@prefix td: .
  
tc:xx a owlunit:ErrorProvocation ; 
      owlunit:hasInputData td:xx ; 
      owlunit:testsOntology om: . 
      
```

If you want to add your own testcases and toydatasets, be aware to add the ontology owl file. After you have created the test cases, the automation is triggered. 

## System automations

Now that you have added the input that was requested, the system firstly checks if all the input neccessary to construct a test case is present. If it is not, it will stop the process untill you have provided all the input. If it is, it checks the syntax of the sparql queries and of the expected results. If the syntax is correct, it will continue to construct the test cases. If not, the process will halt. Once the system has constructed the test case, it will create a Pull request to add the files to the directory that was created in the first workflow. After you Merge that request, the run-test workflow is triggered and it runs the test cases that were built. The results of the test case run are documented in the TestDocumentation folder of the ontology fragment. If the test execution was not successfull, then the system creates an issue for you to check. 

## Sharing feedback

- Please pay attention to all problems that you encounter during the session. We have created [GitHub issue templates](https://github.com/FiorelaCiroku/XD-Testing/issues) to make it easier for you to describe the problems. There is one template for bugs and one for features that you would like to have. 

- We have also opened several discussion boards [here](https://github.com/FiorelaCiroku/XD-Testing/discussions) to light up conversations regarding features, bugs, documentation and general feedback. We would really appreciate if you could participate in the dicussion boards. 

- Another way to share your feedback is on my channel on Discord. 

## Features under development

- Construct and run integration tests
- Integrate tested ontology fragments to module
- Adapt the tool to work with ontologies that are not structured in the same way

## Materials
- [Presentation](https://drive.google.com/file/d/1cTGpGYFXaAnyP0skhF4IgT8DIGB_H5Ti/view?usp=sharing)
- [Video Tutorial](https://www.dropbox.com/s/wnm5zwa443o4m68/XDTesting%20tutorial.mov?dl=0)
- [Ontology file](https://drive.google.com/file/d/1yHWstifYpPlByf1esQ_J9vGEvE4gZx1f/view?usp=sharing)


