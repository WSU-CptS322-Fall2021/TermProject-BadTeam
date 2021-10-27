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
      - [Host](#host)
      - [Challenge](#challenge)
      - [Prompt](#prompt)
      - [Result](#result)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
| System Desgin | 2021-10-21 | Initial Meeting and intial draft of UML architecture diagram | 1.0 |
| Database Model Specification | 2021-10-26 | Creation of the Database model entry |1.1 |
| View Section | 2021-10-26 | Added info on the view | 1.2 |
| General Information | 2021-10-26 | Added general information for the document | 1.3 |
| Initial Controller Specification | 2021-10-26 | Inital information regarding the controller | 1.4 |
| Updated Controller Specification | 2021-10-26 | Rewrote the controller section to add more specific implementation details | 1.5 |

# 1. Introduction

The over arching goal of this design document is not only to promote organization and communication between developers but with stakeholders as well, in a manor that is easy to understand regardless of background. Within the design process, gaining the stakeholder's approval - Professor Ay, and TAs - for the design implementation plans is crucial, using a design document helps clearly illustrate the thoughts and goals that the developers have for the project in order to fulfill the needs of the user and the goals of the business. Having a design document also serves as a universal design baseline for team members and allows for isolated and collaborative member(s) to align around the same goals.

Our project, Poly type, is an interactive typing challenge application that allows for players to participate in challenges that hosts create. For players, they can enter a room code and username to join a typing challenge, participate in the pre-established challenges, and view their typing results (words per minutes, incorrect characters, rank).  For hosts, they can log in to their account and access their challenges (create, delete, modify, publish, review results). Our goal is to create a fun, easy to use, and collaborative way to learn and practice typing skills.

In the rest of this document...
| Section | Content |
| ------- | ------- |
| Section II | In-Depth descriptions of the architecture, subsystems, and components</br>Most importantly we dissect the specific design pattern that we are following (MVC). In the discussion around our choice it is mentioned why this is an appropraite design pattern and we further delve into the subsystems in our architecture. |
| Section III | Report of the current progess that is and has been made in iteration 1</br>Here is our current discussion of the processes that we have been using and our current thoughts on what has been effective so far.| 

# 2.	Architectural and Component-level Design
## 2.1 System Structure

**UML Component Diagram:**

![](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/20cc6e1e9abeab44bcb0ee41f7b2880491775244/Documents/UMLComponentDiagram.png)

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

Initialize App:
  * Creates an Instance of a Flask Web Server 
  * Configures the connection between our code and our MVC file strucutre
  * In the instance in which a database is not already created, initalizes an empty database
  * Registers the blueprints for the routes we are using to divide up and organize our application

Host Manager:
  * Directs the flow of information between the Host UI and the Host related entities in the database
  * Manages the numerous host-only functionalities
    * Create Challenge
    * Edit Challenge
    * Delete Challenge
    * Start Challenge
    * End Challenge
    * Edit Account Information
    * Logout
  * This component interacts with...
    * Host Management (UI), this provides the relevant interfaces required
    * Host Log In Operations, this component relies upon this system to make sure that the correct user is able to log in
    * Host Operations, this component relies upon this system to access the relevant operations related to a given host

Challenge Manager:
  * Directs the flow of information between the Challenger UI and the Challenger related entities in the database
  * Manages the functionalities only given to challengers (non-logged in users)
    * Login
    * Register
    * Join Challenge
    * Participate in Challenge
    * View Challenger Specific Results
  * This component interacts with...
    * Challenge Participation (UI), this component provides the relevant interfaces required
    * Challenge Operations, this component relies upon the information and functionalities found within this given system

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. | GET, POST | /create_challenge | GET: This will load an empty form for a host to then fill out with all of the necessary info to create a *challenge*, which they can then press the submit button to post the form.</br>POST: This is trigged on the completion of the create challenge form. After submitted a new *challenge* will be entered into the database with the current *host* associated. Additionally, during this process a random join code will be generated and given to the *challenge* |  
|2. | GET, POST | /take_challenge/&lt;guid&gt; | GET: This will be triggered after the *challenger* enters in a valid join code for a *challenge*. This page will then load with the given *challenge* that the *challenger* is participating in with its associated *prompts* being displayed for the *challenger* to type</br>POST: This post is going to collect the data associated with the *challenger* as they are participating in the *challenge*. After the *challenger* finishes typing in the final *prompt* a collection of information (elapsed time, # of correct characters, # of incorrect characters) will be sent to the result route to create a result.</br>Guid: This guid is a random identifier assigned to a *challenger* when they intially try to participate in a *challenge*. This guid will be used to access relevant information throughout the session. | 
|3. | GET, POST | /index | GET: Load the JoinChallenge form. This is the form a *challenger* can enter their username and join code into to then join a *challenge*</br>POST: After a JoinChallenge form is posted the *challenger* is routed to the take challenge route where they can participate in their *challenge*.</br>GET: Load the Login form. This is the form a *host* can enter their username and password into to login to their account.</br>POST: After a Login form is posted, assuming valid login information, the *host* will be redirected to their view challenges route where they can perform a myriad of *host* related operations.</br>GET: Load the registration form. This is the form where someone who does not have an account can enter a username and password to then create a *host* account.</br>POST: After a Registration form is posted, assuming valid input, a new *host* will be created and the newly created account will be redirected to the view challenges route similar to the login.</br>*IMPORTANT NOTE:* We intentionally include login and registration in this route to help acheive our design philosophy of reducing page redirects. This is not an attempt to reduce the overall work of routing our application. It should be noted that this change increased the overall complexity of our main page as we still needed to make it look nice |
|4. | GET, POST | /edit_challenge/&lt;post_id&gt;| GET: After getting to this route a single *challenge* will be loaded allowing for a *host* to change the content of the title or the prompts of this given *challenge*.</br>POST: On submission of the form, the new content will replace the old content from the original *challenge* updating this entity.</br>PostId: This is going to be used to route the challenges so that the correct challenge gets updated. | 
|5. | POST | /delete_challenge/&lt;post_id&gt; | POST: On submission of this form the *host* will have deleted the relevant *challenge*</br>PostId: This is going to be used to route the challenges so that the correct challenge gets deleted. 
|6. | GET, POST | /edit_host       | GET: This will load all of the currently known information for the give *host* onto the page where the logged in user can then update it</br>POST: On submission of the form, the new information will then be used to update the information currently associated with the current *host* |
|7. | GET | /result/guid?&lt;guid&gt; | GET: This is the *result* page associated with a specific *challenger* after they finish their *challenge*</br>Guid: This is the same guid that is assigned to the *challenger* when they initially join the *challenge* |
|8. | GET | /result/join_code?&lt;join_code&gt; | GET: On retrieval of the *result*, the information associated will be used to populate the page with relevant information allowing for both *hosts* and *challengers* to see the relevant rankings and results</br>Join Code: This is the join code of the *challenge* and will be used to query the database to know the exact enetity that needs to be pulled to get the relevant information |
|9. | POST | /logout | POST: In hopes of following MVC the logout button will be implemented as a form to keep separation between the view and the model. On form submission the current *host* will be logged out and will be redirected back to the index page. |


### 2.2.3 View and User Interface Design 

**Role of the View:** The view is designed to facilitate user interaction with the functionality of our system. Specific to this project, the view is what allows users to initiate the actions in the controller which handle the management of their challenges. The view is also largely responsible for the functionality of the typing test itself in this particular software, as by nature a typing test is little more than an assessment of how quickly and efficiently you can use the user interface.

**How the View is Constructed:** Our view is being written in standard HTML and CSS. As of right now, we have no plans to integrate any external libraries or systems into the software, as our assessment is that the UI is easy enough to accomplish without bulky external libraries. As of iteration 2 there will also be the inclusion of some javascript for page dynamics not able to be accomplished with only HTML and CSS, but for the time being the view does not include any JS. 

In our application specifically we are also setting up the CSS to enable the later addition of additional themes. To enable this all the colors are stored in CSS variables tied to a single class selector that can be changed later on for the implementation of additional themes. The current color theme is referred to as "solarized dark" and consists of five colors designated *primary, subtle, contrast, background,* and *error* 

**Current UI Overview:** Below are the pages included in the current build of the UI, including their screenshots, descriptions, and the use cases which they enable the user to engage with.

**Homepage**

![](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/20cc6e1e9abeab44bcb0ee41f7b2880491775244/Documents/HomepageImage1.png)

![](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/20cc6e1e9abeab44bcb0ee41f7b2880491775244/Documents/HomepageImage2.png)

*The Homepage:* The homepage is the first page that the average first-time user will see upon using the application. It is an intentionally versatile view layout. The first screenshot is the default view that the player will see, with a minimalist design that highlights the join functionality. If one hovers towards the login button, however, a login/register window will appear to allow for a user to authenticate. **This multi-functional design is intentional,** as one of our non-functional design goals is to minimize page reloads.

*Use Cases:* The homepage UI allows access to the use cases; *Register Host, Log in Host,* and *Join Challenge*

**Create Challenge Page**

![](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/20cc6e1e9abeab44bcb0ee41f7b2880491775244/Documents/CreateChallengeImage.png)

*The Create Challenge Page:* The Create Challenge page has only a single major functionality, which is that it allows the user to create a challenge, with a title and a series of prompts that the challengers will have to copy. After entering at least one prompt and a title at the top, the user can post their challenge, and it will open that new challenge for challengers to join.

*Use Cases:* The Create Challenge UI allows access the Use Case *Create Challenge* and *Update Challenge*

**Take Challenge Page:**

![](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/20cc6e1e9abeab44bcb0ee41f7b2880491775244/Documents/TakeChallengeImage.png)

*The Take Challenge Page:* The take challenge page will as of the later iterations become the main meat of our application. For now it allows you to type, and displays the first prompt of whatever challenge you've joined, as well as your chosen nickname in the top right corner. The original prompt is displayed in the *subtle* color and the letters you type are overlaid over this in the *primary* color.

*Use Cases:* This page specifically enables access to the *Take Challenge* Use Case.

# 3. Progress Report

In iteration one, for the Model, we implemented all the required database models for general functionality, for the Controller, we established basic routing, and for the View, we set up basic pages for user interaction. In terms of the more specific functionalities we have implemented, we have done: creation of host accout, creation of challenge, login, viewing challenges, joining a challenge, and the most basic participation in a challenge. In addition, our group feels as though we are effectively using github and think the current process of using Github Issues as an effective way to track work that needs to be done. We are starting to discuss the requirements and the work that we are wanting to get done in iteartion 2 which is most notibly is going to include the core functionality in participating in a challenge.
