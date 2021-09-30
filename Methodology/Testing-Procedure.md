This page is created to provide information about the testing procedures that are conducted in the eXtreme Design methodology. 

# Testing

There are three main instances, or variants, of this methodology regarding the testing: CQ verification, inference verification, and error provocation. The first two are each connected to verifying the correct implementation of a requirement, e.g. a CQ or an inference task.

In the following tables, are shown the protocol for the testing in general and the properties that should describe a test case. 

<img width="749" alt="Screenshot 2021-09-23 at 15 50 59" src="https://user-images.githubusercontent.com/12375920/135452349-62729248-5fb5-4234-afa6-f51b83829d62.png">

<img width="749" alt="Screenshot 2021-09-23 at 15 48 31" src="https://user-images.githubusercontent.com/12375920/135452481-0aa5f7c8-2479-4531-aa6b-5e24665b7c31.png">

Even though the protocol is the same for all three types of tests, there are some differences regarding the process of testing. In the following sections, there is information about the process of each test in specific. 

## Competency question verification

The procedure for the competency question verification test is:

1. Create a list of competency questions.
2. Choose one competency question to create the unit test. 
3. Reformulate the competency question into a SPARQL query using elements from the module to be tested. 
4. A test case OWL file is created, as well as a test run OWL file, i.e. the latter being an empty ontology where we import the module realizing the initial CQ from step 1, and we document them by inferring to the testing metamodel. 
5. Test data related to the query is added to the test run file.
6. Determine which of the instances should be part of the expected result set. 
7. The SPARQL query is ran on the test run ontology.
8. The results can be automatically verified against the expected output. 
9. In case of unexpected results, they are analysed.
10. The test results are documented in the test run ontology file using the properties provided by the metamodel. 
11. Continue to iterate on this test if there is a negative result, otherwise continue with the testing of the next competency question. 

## Inference verification

The procedure for the inference verification test is:

1. Start from a set of requirements. 
2. Choose a requirement to run the test on.
3. Describe the test procedure (often classification, commonly provided by OWL reasoners).
4. A new test case is created and a first test run OWL file importing the ontology to be tested. 
5. Test data is added, both the data that will produce the inference and the data that should not. 
6. Define the expected result of the test.
7. An OWL reasoner is run over the test run OWL-file.
8. The results are verified against the expected ones and stored.
9. For any faults discovered, the module is analysed and undesired side effects have to be assessed to determine whether they can be handled by changing the ontology. 
10. The test run is documented.
11. Any remaining requirements are treated. 

## Error provocation

Apart from performing correct inferences and supporting queries, another important characteristic of an ontology is to allow as few erroneous facts or inferences as possible. 

The procedure for the error provocation test is:

1. Gather requirements
2. Select a requirement
3. The test procedure is established as consistency checking using an OWL reasoner. 
4. The test case and test run OWL-files are created.
5. Instances are added to the test data, where at least one erroneous data is present. 
6. The expected result is an inconsistency since the test data violates our requirement. 
7. Run the OWL reasoner.
8. The results are run automatically. The test is assessed as positive is the test run reports an inconsistency.
9. If not, we analyze the module. 
10. Document the test run
11. Iterate or proceed

# Further Reading

Blomqvist, Eva, Azam Seil Sepour, and Valentina Presutti. "Ontology testing-methodology and tool." International Conference on Knowledge Engineering and Knowledge Management. Springer, Berlin, Heidelberg, 2012.
