# Design Document

## Your Project Title
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
  - [## Your Project Title](#-your-project-title)
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


# 1. Introduction

Explain the purpose for providing this design document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief). 

Then provide a brief description of your project and state your project goal.

At the end of the introduction, provide an overview of the document outline.

Section II includes …

Section III includes …

# 2.	Architectural and Component-level Design
## 2.1 System Structure

This section should describe the high-level architecture of your software:  i.e., the major subsystems and how they fit together. 
If you adopted the application structure we used in the Smile App, your application would have the Model-View-Controller (MVC) pattern. If you adopted a different architectural pattern, mention the pattern you adopted in your software and briefly discuss the rationale for using the proposed architecture (i.e., why that pattern fits well for your system).

In this section:
 * Provide a UML component diagram that illustrates the architecture of your software.
 * Briefly explain the role of each subsystem in your architectural design and explain the dependencies between them. 
 * Discuss the rationale for the proposed decomposition in terms of cohesion and coupling.

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

Initialize App:
  * Creates a Flask Instance and configures the folder locations.
  * Initializes the database.
  * Register Blueprints.

Host Manager:
  * Directs the host to the Host Management UI
  * Manages the Host Log in operations.
  * Manages the Host Operations.

Challenge Manager:
  * Directs the host to the Challenge Participation UI
    * Located in View/Templates/createChallenge.html
  * Manages the Challenge Operations.

For each subsystem:
 * Explain the role of the subsystem (component) and its responsibilities.
 * 	Provide a detailed description of the subsystem interface, i.e., 
    * which other subsystems does it interact with?  
    * what are the interdependencies between them? 


(***in iteration-1***) Brainstorm with your team members and identify all routes you need to implement for the completed application and explain each route briefly. If you included most of the major routes but you missed only a few, it maybe still acceptable. 

(***in iteration-2***) Revise your route specifications, add the missing routes to your list, and update the routes you modified. Make sure to provide sufficient detail for each route. In iteration-2, you will be deducted points if you don’t include all major routes needed for implementing the required use-cases or if you haven’t described them in detail.

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. | createChallenge   | View/Templates/createChallenge.html | Allows the host to create a challenge with up to 5 specified prompts. |
|2. | takeChallenge     | View/Templates/takeChallenge.html | Allows the user to take a challenge by inputing a 6 string code. |
|3. | index             | View/Templates/index.html | Page where Words Per Minute test is timed. Also the default page. |
|4. | editChallenge     | N/A        | Page for editing challenges. |
|5. | editHost          | N/A        | Page for editing host settings. |


### 2.2.3 View and User Interface Design 

**Role of the View:** The view is designed to facilitate user interaction with the functionality of our system. Specific to this project, the view is what allows users to initiate the actions in the controller which handle the management of their challenges. The view is also largely responsible for the functionality of the typing test itself in this particular software, as by nature a typing test is little more than an assessment of how quickly and efficiently you can use the user interface.

**How the View is Constructed:** Our view is being written in standard HTML and CSS. As of right now, we have no plans to integrate any external libraries or systems into the software, as our assessment is that the UI is easy enough to accomplish without bulky external libraries. As of iteration 2 there will also be the inclusion of some javascript for page dynamics not able to be accomplished with only HTML and CSS, but for the time being the view does not include any JS. 

In our application specifically we are also setting up the CSS to enable the later addition of additional themes. To enable this all the colors are stored in CSS variables tied to a single class selector that can be changed later on for the implementation of additional themes. The current color theme is referred to as "solarized dark" and consists of five colors designated *primary, subtle, contrast, background,* and *error* 

**Current UI Overview:** Below are the pages included in the current build of the UI, including their screenshots, descriptions, and the use cases which they enable the user to engage with.

**Homepage**

![](C:\Users\colli\Desktop\CPTS-322\Poly_Type\repo\TermProject-BadTeam\Documents\HomepageImage1.png)

![](C:\Users\colli\Desktop\CPTS-322\Poly_Type\repo\TermProject-BadTeam\Documents\HomepageImage2.png)

*The Homepage:* The homepage is the first page that the average first-time user will see upon using the application. It is an intentionally versatile view layout. The first screenshot is the default view that the player will see, with a minimalist design that highlights the join functionality. If one hovers towards the login button, however, a login/register window will appear to allow for a user to authenticate. **This multi-functional design is intentional,** as one of our non-functional design goals is to minimize page reloads.

*Use Cases:* The homepage UI allows access to the use cases; *Register Host, Log in Host,* and *Join Challenge*

**Create Challenge Page**

![](C:\Users\colli\Desktop\CPTS-322\Poly_Type\repo\TermProject-BadTeam\Documents\CreateChallengeImage.png)

*The Create Challenge Page:* The Create Challenge page has only a single major functionality, which is that it allows the user to create a challenge, with a title and a series of prompts that the challengers will have to copy. After entering at least one prompt and a title at the top, the user can post their challenge, and it will open that new challenge for challengers to join.

*Use Cases:* The Create Challenge UI allows access the Use Case *Create Challenge* and *Update Challenge*

**Take Challenge Page:**

![](C:\Users\colli\Desktop\CPTS-322\Poly_Type\repo\TermProject-BadTeam\Documents\TakeChallengeImage.png)

*The Take Challenge Page:* The take challenge page will as of the later iterations become the main meat of our application. For now it allows you to type, and displays the first prompt of whatever challenge you've joined, as well as your chosen nickname in the top right corner. The original prompt is displayed in the *subtle* color and the letters you type are overlaid over this in the *primary* color.

*Use Cases:* This page specifically enables access to the *Take Challenge* Use Case.

# 3. Progress Report

Write a short paragraph summarizing your progress in iteration1.

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