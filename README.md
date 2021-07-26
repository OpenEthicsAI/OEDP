# Open Ethics Data Passport (OEDP)

[![DOI](https://zenodo.org/badge/388838903.svg)](https://zenodo.org/badge/latestdoi/388838903)

## This repository
This repository scopes the Open Ethics Data Passport (OEDP)

## Contributors
- Alice Pavaloiu
- Nikita Lukianets

## Key concepts
- Data labeler
- Supervised machine learning
- Input-output mapping
- Training data
- Test data
- Data model
- Prediction
- Bias
- Fairness
- Ethics vector
- Data source

## Problem
Supervised learning remains one of the most widely used approaches in machine learning. A supervised learning approach requires data annotated by subject-matter experts to train machine learning algorithms. Part of the bias and algorithmic unfairness gets inherited from the historically labeled data. It is a socio-technological phenomenon that happens because people who label the data or the ones who make decisions mapping inputs to outputs unconsciously carry biases already (we are humans). Transparency around who labeled the data and the impact of the profile of the data labeler - their expertise, their personality, and their value hierarchies on the resulting fairness and accuracy properties of the machine learning models remain unknown.

## Purpose
Bring transparency to the systemic properties of the AI models by developing a Data Passport. The Data Passport has a purpose at depicting the origins of the training datasets by bringing a standardized approach to convey information about data annotation processes, data labelers profiles, and correct scoping of the labeler’s job.

## Objectives
1. Establish a baseline self-disclosure approach to depict the origins of the training data
2. Develop evaluation methodology to assess data labelers’ profile
3. Develop a tool that will allow using this evaluation methodology
4. Make this tool available for market players in data labeling
5. Combine these approaches into a machine-readable Data Passport
6. Make Data Passport an integral part of the Open Ethics Transparency Protocol

## OEDP Structutre
### 1. Product Profile
    1.1. Data labeling approach – internal (in-house)/ outsourcing/ crowdsourcing/ data labeling service (specialized outsourcing)/ synthetic labeling/ data programming (scripts)
    1.2. Tools used (if any), automation
    1.3. Quality assurance – data accuracy, data quality
    1.4. Process iteration
    1.5. Hiring, training, and management of data labelers & integration of new members
    1.6. Project management (planning, process operationalization, and measurement of success)
    1.7. Scaling
    1.8. Outsourcing
    1.9. Security
    1.10. Tracking performance
    1.11. Product Scoping

### 2. Labeler Profile
    2.1.	Identity [name, email]
    2.2.	Details on current project (if disclosable – description, duration, task) [text]
    2.3.	Type of contract (employee, contractor, 3rd party platform, data-labeling service provider, etc.) & position in the company if applicable [select]
    2.4.	Previous expertise & skills in data science (or only in data labeling if we isolate it) [list]
    2.5.	Training provided by the company [list]
    2.6.	What tools are they using [list]

## Taxonomy of Labeling approaches

|     Approach                             	|     Description                                                                                                              	|
|------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------	|
|     Internal   labeling                  	|     Assignment of tasks to an in-house data science team                                                                   	|
|     Outsourcing                          	|     Recruitment of   temporary employees on freelance platforms. posting vacancies on social media   and job search sites    	|
|     Crowdsourcing                        	|     Cooperation with freelancers from crowdsourcing   platforms                                                              	|
|     Specialized outsourcing companies    	|     Hiring an external team for a specific project                                                                         	|
|     Synthetic labeling                 	|     Generating data with the same statistical properties and attributes as real data                                                                  	|
|     Data programming                     	|     Using scripts that programmatically label datasets                                                 	|

## Roadmap and deliverables
1. Profile structure [JSON/XML/CSV]
2. Profile assessment tool with identity management and labeling history [web-based]
3. A machine-readable Data Passport [JSON]
4. Integration into the Open Ethics Transparency Protocol https://openethics.ai/oetp/
