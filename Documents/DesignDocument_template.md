# Design Document

## Poly Type

--------
Prepared by:

* `Collin Nelson`,`Bad Team`
* `Anna Ueti`,`Bad Team`
* `Brandon Cook`,`Bad Team`
* `Tyler Jones`,`Bad Team`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [Poly Type](#poly-type)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2021-10-05 |Initial draft | 1.0        |
|Database Model |2021-10-26 | Creation of the Database model entry |1.1 |
| View Section | 2021-10-26 | Added info on the view | 1.2 |
| General Information | 2021-10-26 | Added general information for the document | 1.3 |


# 1. Introduction

The over arching goal of this design document is not only to promote organization and communication between developers but with stakeholders as well, in a manor that is easy to understand regardless of background. Within the design process, gaining the stakeholder's approval - Professor Ay, and TAs - for the design implementation plans is crucial, using a design document helps clearly illustrate the thoughts and goals that the developers have for the project in order to fulfill the needs of the user and the goals of the business. Having a design document also serves as a universal design baseline for team members and allows for isolated and collaborative member(s) to align around the same goals.



Our project, Poly type, is an interactive typing challenge application that allows for players to participate in challenges that hosts create. For players, they can enter a room code and username to join a typing challenge, participate in the pre-established challenges, and view their typing results (words per minutes, incorrect characters, rank).  For hosts, they can log in to their account and access their challenges (create, delete, modify, publish, review results). Our goal is to create a fun, easy to use, and collaborative way to learn and practice typing skills.



**Section II** includes in-depth descriptions of the the architecture and component designs.

**Section III** includes a report of our progress for Iteration 1.

**Section IV** includes our plans for testing our designs.

**Section V** includes our references.



If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief).

# 2.	Architectural and Component-level Design
## 2.1 System Structure

**UML Component Diagram:**

![](.\UMLComponentDiagram.png)

**View:** The View handles displaying information and UI elements to the user, takes any input from the user, and conveys the given inputs and outputs to Controller. The View is dependent on the Controller for authenticating hosts and connecting players to open challenges (Host management to Host Manager, and Challenge Participation to Challenge Manager respectively).

**Controller:** The Controller provides a layer of separation between the front end and the back end, handles complex business logic for the functionalities of the application, and facilitates communication between the View and the Model. The Controller is dependent on the Model for providing the data for authenticating hosts, accurately populating the Host's list of challenges, and displaying the prompts of an open challenge.

**Model:** The Model stores raw data for hosts, challenges, prompts, and results, as well as handles database operations.



**Rationale:** We chose to use MVC in order to create a clear distinction between the front end (View) and the back end (Model) to decrease coupling. Only the Controller has access to the Model so if the View needs data from the Model it must request it from the Controller. This architecture naturally groups elements that are similar in functionality together - for example, all the .html files for the website are contained within the View system - which encourages and enhances cohesion. Additionally, it allows us to easily update or modify the View without needing to change the Model. 

## 2.2 Subsystem Design 

(Note: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

### 2.2.1 Model

The model defines the schema for our database and the 'plain old python objects' we are going to be using throughout our application
In our database we are going to have 4 main tables:

#### Host

| Field | Description |
| ------ | ------ |
| **Id** | Primary key for the host entry |
| **Username** | Username that is associated with the host (used for logging in) |
| **PasswordHash** | Password hash that is associated with the host (also used for loggin in) | 
| **Challenges** | Relationship between a host and the challenges associated with their account</br>One to many relationship (1 -> *) | 

#### Challenge

| Field | Description |
| ------ | ------ |
| **Id** | Primary key for the challenge entry |
| **HostId** | Foreign key that links a challenge back to its host |
| **Title** | Name/title that is associated with a challenge |
| **JoinCode** | 6 character alpha-numeric code that is going to be used as the way for a challenger to join a specific challenge  |
| **Prompts** | Relationship between a challenge and the prompts associated with that specific challenge </br> One to many relationship, at least one prompt is required (1 -> 1*)|
| **Results** |Relationship between a challenge and the results of all of the challengers that have taken this specific challenge</br> One to many relationship (1 -> *)|
| **Open** | Boolean value that stores whether or not the challenge is able to be taken currently |

#### Prompt

| Field | Description |
| ------ | ------ |
| **Id** | Primary key for the prompt entry |
| **ChallengeId** | Foreign key that links a prompt back to its challenge |
| **Text** | Text that is associated with a given prompt</br>This is what a challenger will actually be typing out when they are participating in a challenge |

#### Result

| Field | Description |
| ------ | ------ |
| **Id** | Primary key for the result entry |
| **ChallengeId** | Foreign key that links a result back to its challenge |
| **Challenger** | Username of challenger who took the challenge linked to this result |
| **ElapsedTime** | Total elapsed time that it took for the challenger to complete all prompts in the linked challenge |
| **Correct** | Total number of correct characters that the challenger typed while completing all prompts in the linked challenge |
| **Incorrect** | Total number of incorrect characters that the challenger typed while completing all prompts in the linked challenge |

### 2.2.2 Controller

Briefly explain the role of the controller. If your controller is decomposed into smaller subsystems (similar to the Smile App design we discussed in class), list each of those subsystems as subsections. 

For each subsystem:
 * Explain the role of the subsystem (component) and its responsibilities.
 * 	Provide a detailed description of the subsystem interface, i.e., 
    * which other subsystems does it interact with?  
    * what are the interdependencies between them? 

**Note:** Some of your subsystems will interact with the Web clients (browsers). Make sure to include a detailed description of the  Web API interface (i.e. the set of routes) your application will implement. For each route specify its “methods”, “URL path”, and “a description of the operation it implements”.  
You can use the following table template to list your route specifications. 

(***in iteration-1***) Brainstorm with your team members and identify all routes you need to implement for the completed application and explain each route briefly. If you included most of the major routes but you missed only a few, it maybe still acceptable. 

(***in iteration-2***) Revise your route specifications, add the missing routes to your list, and update the routes you modified. Make sure to provide sufficient detail for each route. In iteration-2, you will be deducted points if you don’t include all major routes needed for implementing the required use-cases or if you haven’t described them in detail.

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. |                   |            |              |
|2. |                   |            |              |
|3. |                   |            |              |
|4. |                   |            |              |
|5. |                   |            |              |
|6. |                   |            |              |


### 2.2.3 View and User Interface Design 

**Role of the View:** The view is designed to facilitate user interaction with the functionality of our system. Specific to this project, the view is what allows users to initiate the actions in the controller which handle the management of their challenges. The view is also largely responsible for the functionality of the typing test itself in this particular software, as by nature a typing test is little more than an assessment of how quickly and efficiently you can use the user interface.

**How the View is Constructed:** Our view is being written in standard HTML and CSS. As of right now, we have no plans to integrate any external libraries or systems into the software, as our assessment is that the UI is easy enough to accomplish without bulky external libraries. As of iteration 2 there will also be the inclusion of some javascript for page dynamics not able to be accomplished with only HTML and CSS, but for the time being the view does not include any JS. 

In our application specifically we are also setting up the CSS to enable the later addition of additional themes. To enable this all the colors are stored in CSS variables tied to a single class selector that can be changed later on for the implementation of additional themes. The current color theme is referred to as "solarized dark" and consists of five colors designated *primary, subtle, contrast, background,* and *error* 

**Current UI Overview:** Below are the pages included in the current build of the UI, including their screenshots, descriptions, and the use cases which they enable the user to engage with.

**Homepage**

![](.\HomepageImage1.png)

![](.\HomepageImage2.png)

*The Homepage:* The homepage is the first page that the average first-time user will see upon using the application. It is an intentionally versatile view layout. The first screenshot is the default view that the player will see, with a minimalist design that highlights the join functionality. If one hovers towards the login button, however, a login/register window will appear to allow for a user to authenticate. **This multi-functional design is intentional,** as one of our non-functional design goals is to minimize page reloads.

*Use Cases:* The homepage UI allows access to the use cases; *Register Host, Log in Host,* and *Join Challenge*

**Create Challenge Page**

![](.\CreateChallengeImage.png)

*The Create Challenge Page:* The Create Challenge page has only a single major functionality, which is that it allows the user to create a challenge, with a title and a series of prompts that the challengers will have to copy. After entering at least one prompt and a title at the top, the user can post their challenge, and it will open that new challenge for challengers to join.

*Use Cases:* The Create Challenge UI allows access the Use Case *Create Challenge* and *Update Challenge*

**Take Challenge Page:**

![](.\TakeChallengeImage.png)

*The Take Challenge Page:* The take challenge page will as of the later iterations become the main meat of our application. For now it allows you to type, and displays the first prompt of whatever challenge you've joined, as well as your chosen nickname in the top right corner. The original prompt is displayed in the *subtle* color and the letters you type are overlaid over this in the *primary* color.

*Use Cases:* This page specifically enables access to the *Take Challenge* Use Case.

# 3. Progress Report

In iteration one, for the Model, we implemented all the required database models for general functionality, for the Controller, we established basic routing, and for the View, we set up basic pages for user interaction.  

# 4. Testing Plan

(***in iteration 1***)
Don't include this section.

(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the API routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? (Manual tests are OK)
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)



# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.


----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 


|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 10        | Is the architecture of the system described well, with the major components and their interfaces?  Is the rationale for the proposed decomposition in terms of cohesion and coupling explained well? |
| 15        | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear and complete UML component diagram illustrating the architecture of the system? |
| 15        | Is the model (i.e., “database model”) explained well with sufficient detail? | 
| 10        | Is the controller explained in sufficient detail?  |
| 20        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? |
| 10        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.   |
| 5         | Is there sufficient detail in the design to start Iteration 2?   |
| 5         | Progress report  |
|           |   |
|           | **Clarity** |
| 5         | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
|           |  |
|           | **Total** |
|           |  |