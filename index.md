# Welcome to eXtreme Design Testing

This website is created to present the work regarding the test automation for the [eXtreme Design](https://extremedesign.info) ontology modelling methodology.

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

## Guidelines on using the automation for the testing of the ontologies

The first thing that you have to do is it access the repository of the testing. The repository can be found by clicking the button in the top of the page or by clicking [here](https://github.com/FiorelaCiroku/XD-Testing). In this repository, you can find several directories, most importantly the Documentation folder and **ontology-network** folder. When you open the **ontology-network** folder, you will see that there is another folder named **musical-performance-module**. This is the folder where you, as an ontology tester, can trigger the automatic testing of conceptual components of your modules. The actions that you need to take are:
1. Create a folder for a new Conceptual Component with a README.md file in the **ontology-network** folder.
2. Wait a couple of second for the first automation to be completed. This automation will create a Pull request that you can find in the horizontal menu of Github. The Pull request consists on the creation of a directory structure for the testing of the conceptual component. The structure should be as shown bellow. 

![Screenshot 2021-12-29 at 06 50 29](https://user-images.githubusercontent.com/12375920/147631401-d4ab9ebd-1215-4356-a351-ca22bfacd13c.png)

3. Merge the Pull request to the master branch of the repository. Quickly, you can see in the **musical-performance-module** folder that a new folder was created with the name **test**. If you browse in the inside of the folder, you can verify that the structure shown above is the result of the automation performed when you added the new conceptual component folder. 
4. 



















[1] https://dl.acm.org/doi/pdf/10.1145/3460210.3493542
