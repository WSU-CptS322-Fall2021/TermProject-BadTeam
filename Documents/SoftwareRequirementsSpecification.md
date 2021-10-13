# Software Requirements Specification

## Poly_Type
--------
Prepared by:

* `Collin Nelson`, `Bad Team`
* `Tyler Jones`, `Bad Team`
* `Brandon Cook`,`Bad Team`
* `Anna Ueti`,`Bad Team`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Ploy_Type](#poly_type)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 User Stories](#22-user-stories)
  - [2.3 Use Cases](#23-use-cases)
  - [2.4 Non-Functional Requirements](#24-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name       | Date       | Changes            | Version |
| ---------- | ---------- | ------------------ | ------- |
| Revision 1 | 2021-10-05 | Initial draft      | 1.0     |
| Revision 2 | 2021-10-12 | Filled Out Details | 1.1     |

----
# 1. Introduction

## 1.1 Document Purpose

The purpose of the Software Requirement Specification document is to outline and guide this project. It serves as the guide rails that provide the structure to support this group as we move into starting this project. This document serves as a way to communicate the expectations we have in relation to what the software we are building is expected to be able to do. The intended audience of this document include the stakeholders. Most notably however, this document will be extremely helpful as a reference for both the developers and the owners of the software.

## 1.2 Product Scope

The goal of this software is to provide a platform that provides a competitive and fun environment for testing your typing ability. This is similar to other type testing software but with the added unique factor of a kahoot style competitive element.

The objectives of this project are as follows...
- Create an interface for a host to log in and create tests, which when published are a series of prompts that must be typed.
- Players should be able to join challenges under a chosen username, competing in each phase of the challenge.
- This challenge must evaluate their speed, accuracy, and record any errors they while typing.
- After the challenge, competitors should be able to see their ranking with others who have taken the test, comparing their accuracy and speed
- Hosts should be able to view the stored results of all tests they’ve run.


## 1.3 Document Overview

This document contains the required specifications including the Customer, User and Stakeholder information. Afterwards, we continue to discuss the different user stories that we have along with a basic overview of each one. In another section, this documents also hold all the Use Cases with describing details about their triggers, actions and more. As we move closer to the end we will reach a the expectations for what the UI will be and the general design principles we are trying to follow. Lastly, we give some reference websites that have similar functionalities to ours and a glossary of some of our terms that we have.

----
# 2. Requirements Specification


## 2.1 Customer, Users, and Stakeholders

1. **Primary Customer:** Professor Sakire Arslan Ay

2. **Primary Users:** Anonymous Internet Users, roughly separated into 2 groups. Hosts, who create content, likely to be educators or especially active users, and Competitors, anonymous users who join only to take a particular challenge.

3. **Primary Stakeholders:** Professor Ay; The members of Bad Team who will be developing, maintaining, and potentially using this project.

## 2.2 User Stories

**Host Accounts:** As a host, I want to be able to create a permanent account in which I can create and manage challenges, because I want to be able to generate custom challenges for a group of people.

**Challenge Management:** As a host I want to be able to manage my challenges, performing operations like editing, deleting, and initiating them, because without that ability I would quickly lose the ability to organize my challenges.

**Competitor Features:** As an anonymous competitor, I would like to be able to easily join, participate in, and see the results of challenges without needing to register an official account. I want to be able to use any username I want and join quickly and easily.

**View Results:** As a  user, I would like to be able to view the results of tests that I've either taken or hosted, because I want some record of previous challenges after they've been closed.

## 2.3 Use Cases

| Name              | Register                                                     |
| ----------------- | ------------------------------------------------------------ |
| Users             | All Users                                                  |
| Rationale         | In order to be able to use Host features, it is necessary to allow users to create a new Host account with which to authenticate and access Host functionality. |
| Triggers          | The User indicates that they would like to register a new account. |
| Preconditions     | User is on the site. They have *not* joined a challenge (see Use Case #18). |
| Actions           | 1. The User indicates that they would like to register.<br />2. The User inputs necessary account information<br />3. The User indicates that the information is correct<br />4. The software creates  a new Host user, logs the User in as this new Host, and displays Host functionality. |
| Alternative paths | Before Step 3, the user exits the registration process. In this case no new user is created and the User is only shown Competitor functionality. |
| Postconditions    | The User is now logged in as a Host (see Use Case #10). The User can now view Host functionality. |
| Acceptance tests  | Using register functionality, create new mock user. Confirm the creation of a user with the given details. |
| Iteration         | 1                                                            |
- - -
| Name              | Log In                                                       |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                            |
| Rationale         | In order to be able to access host features after creating a Host account, one needs to be able to authenticate and log in with that account. |
| Triggers          | The User has just created a new Host account OR The User indicates the would like to log in. |
| Preconditions     | The User is on the site. They are not logged in currently. They have not joined a challenge (see Use Case #18) |
| Actions           | 1. The User indicates that they would like to log in.<br />2. They provide necessary authentication details<br />3. The software checks their details and logs them in as the related Host user,  then displays Host functionalities. |
| Alternative Paths | 1. In Step 3, the software finds that the provided details match no known Host user. Instead of logging them in the software reports the error to the User and allows them to retry entering their details. </br>2. In between Step 1 and Step 2, the user decides that they no longer want to login as a host and return back to the main page|
| Postconditions    | The User is logged in and can view Host functionalities      |
| Acceptance Tests  | Using the log in process, attempt to provide details for a pre-created mock user. Confirm that log-in was successful. |
| Iteration         | 1                                                            |
- - -
| Name              | Edit Account Info                                            |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | If a Host User made a mistake while creating their account or wants to change a detail such as their password or their username, there should be functionality that allows them to do so through the software without having to create a totally new account. |
| Triggers          | The User indicates that they would like to edit their account info. |
| Preconditions     | The User is logged in as a Host.                             |
| Actions           | 1. The User indicates that they would like to edit their account details.<br />2. They indicate the updates or changes they would like to make<br />3. The software performs the necessary updates to their Host account. |
| Alternative Paths | During Step 2, the User exits the edit process. In this case no changes are made to the User account and the User is returned to the state they were in before beginning the edit process. |
| Postconditions    | The User is still logged in as their Host account but the software reflects the updates they've made to their account details where applicable. |
| Acceptance Tests  | Create a mock User. Establish and check that user's existing details. Use the edit functionality to update those User details. Confirm that the updates are correctly reflected. |
| Iteration         | 3                                                            |
- - -
| Name              | View Created Challenges                                      |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | When the host creates a challenge, they need to be able to view those challenges to access other functionality like editing (Use Case #14), deleting (Use Case #12) or initiating. (Use Case #11) |
| Triggers          | Immediately upon the user logging in as a Host OR when the user is using some other functionality and finishes or exits that feature. |
| Preconditions     | The User is logged in as a Host.                             |
| Actions           | 1. The User logs in as a Host (see Use Case #10)<br />2. The software displays a view of all the User's created challenges. |
| Alternative Paths | Instead of Step 1, the User is already logged in as a Host but is utilizing another feature which hides the view information. Upon exiting or finishing with that feature, move to Step 2. |
| Postconditions    | The User is able to view all of their created challenges, and access triggers for other challenge features. |
| Acceptance Tests  | Generate a mock user with a mock challenge associated with them. Log in as this User, and confirm that it displays the expected challenge data. |
| Iteration         | 1                                                            |
- - -
| Name              | Create Challenge                                             |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | In order to be able to take challenges, Host users need to be able to generate them in the application. |
| Triggers          | The user indicates that they would like to begin creating a new challenge. |
| Preconditions     | User is logged in as a host. The User has fewer than the maximum number of allowed created challenges. |
| Actions           | 1. The User indicates that they would like to create new challenge<br />2. The User enters the prompts for each phase of the challenge, adding new phases as needed.<br />3. The User indicates they are done editing the challenge.<br />4. The software creates a new challenge with the given information, tied to the Host's account. |
| Alternative Paths | During Step 2, Before Step 3, the User indicates that they would like to cancel the creation process. In this case no new challenge is created and the user is able to exit the creation process. |
| Postconditions    | The User has a new test with the given information viewable and associated with their account. (see. Use Case #8) |
| Acceptance Tests  | Ensure that when the Create Challenge feature is utilized with known prompts, that a new test is successfully created with the expected data. |
| Iteration         | 1                                                            |
- - -
| Name              | Initiate Challenge                                           |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | Once the User has created a challenge. They need to be able to 'initiate' it, opening it up temporarily to attempts from Competitors and logging that session's results. |
| Triggers          | The user indicates they would like to initiate a created challenge. |
| Preconditions     | The User is logged in as a Host. They have at least one challenge created. Their desired challenge is not already open. |
| Actions           | 1. The User indicates that they would like to initiate the challenge.<br />2. The software flags the challenge as open, changes it's state in the software, and generates a room code for the session.<br />3. The software reflects these changes and makes the room code available to the User |
| Alternative Paths | None                                                         |
| Postconditions    | The challenge is open to competitors. The room code is made available to the Host. |
| Acceptance Tests  | Mock up a test associated with a Host User. Using this functionality, initiate the test. Check that the test is open and that the room code has been generated. |
| Iteration         | 2                                                            |
- - -
| Name              | Update Challenge                                             |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | Once a Host has created a challenge, they may want to change the length or wording of its prompts, or add additional prompts. The software must therefore support the editing of created challenges. |
| Triggers          | The User indicates that they would like to edit a challenge  |
| Preconditions     | The User is logged in as a Host. They have at least one created challenge. Their chosen challenge is not in its initiated state (see Use Case #11) |
| Actions           | 1. The User indicates that they would like to edit a challenge.<br />2. They add a new prompt to that challenge with a quote of their choice.<br />3. They indicate that they would like to save their changes.<br />4. The software saves the edited prompt. |
| Alternative Paths | During Step 2, the user decides to exit or cancel their edits. In this case no changes are made, the challenge remains in its original form and the user is returned to the pre-edit state.<br /><br />During Step 2, the user does not add a new prompt but instead edits the content of a specific prompt. In this case those changes are saved over the content of the original prompt. |
| Postconditions    | The challenge is saved with its content edited and all future initiations of that challenge will utilize the updated content. |
| Acceptance Tests  | Create a mock challenge. Using the update challenge functionality, update some of the challenge values. Confirm that the challenge has been updated successfully. |
| Iteration         | 3                                                            |
- - -
| Name              | Delete Challenge                                             |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | Once a host has created challenges, they may decide that they don't want one or more of the challenges they've created. In this case, the software should support deleting challenges from one's library. |
| Triggers          | The user indicates that they would like to delete a challenge. |
| Preconditions     | The User is logged in as a host. They have created at least one challenge, and that challenge is not currently open. |
| Actions           | 1. The User indicates that they would like to delete a challenge.<br />2. The software deletes that challenge and all records and updates to reflect this change. |
| Alternative Paths | None                                                         |
| Postconditions    | All records relating the chosen test have been deleted and the software has updated to reflect the change. |
| Acceptance Tests  | Create a Mock Test. Using the delete test functionality, delete this test from the records. Confirm that this test and all records associated with it have been disposed of. |
| Iteration         | 3                                                            |
- - -
| Name              | Stop Challenge                                               |
| ----------------- | ------------------------------------------------------------ |
| Users             | Host                                                         |
| Rationale         | Once a Host has initiated a challenge. They may want to stop this session of the challenge, preventing all further attempts, and caching the results from these competitors |
| Triggers          | The User indicates that they would like to stop an initiated challenge. |
| Preconditions     | The User has created at least one challenge. The challenge is currently in the 'Initiated' state. |
| Actions           | 1. The User indicates that they would like to stop the challenge.<br />2. The software flags the challenge as stopped.<br />3. All competitors currently taking the challenge are allowed to finish and their statistics will be recorded<br />4. The results of this session of the challenge are cached and made viewable to the Host. |
| Alternative Paths | None                                                         |
| Postconditions    | The challenge is no longer in the 'initiated' state. The results are accessible to the Host |
| Acceptance Tests  | Create a mock challenge. Initiate this challenge. Using this functionality, stop the challenge. Confirm that the challenge is no longer initiated and that any results have been cached properly. |
| Iteration         | 2                                                            |
- - -
| Name              | Join Challenge                                               |
| ----------------- | ------------------------------------------------------------ |
| Users             | Competitor                                                   |
| Rationale         | In order to participate in user created challenges one must be able to join a challenge in progress. |
| Triggers          | The User provides a valid room identifier and indicates that they would like to join the challenge. |
| Preconditions     | The User is not logged in as a Host; The User has received a valid room identifier from the Host who has enabled the challenge. |
| Actions           | 1. The User indicates their room identifier.<br />2. The User indicates the name that they would like to be associated with their scores.<br />3. The User indicates they would like to join the challenge.<br />4. The software routes them to the Take Challenge functionality (see Use Case #15) |
| Alternative Paths | During Step 1, the User does not indicate a correct room identifier. In this case they are not allowed to proceed to Step 4, and they are informed that their room identifier is invalid. |
| Postconditions    | The User is engaged in the Take Challenge functionality (see Use Case #15) under their chosen pseudonym with which their results will be associated. |
| Acceptance Tests  | Create a mock challenge that is set to initiated. Attempt to use the join challenge functionality to join the challenge. Confirm that the challenge was joined correctly<br /><br />Attempt to join a mock challenge using a room identifier that isn't valid. Confirm that the error response is as expected. |
| Iteration         | 1                                                            |
- - -
| Name              | Take Challenge                                               |
| ----------------- | ------------------------------------------------------------ |
| Users             | Competitor                                                   |
| Rationale         | Once the user has indicated that they want to take a challenge and a have a valid room identifier, they actually need to be able to test themselves in the challenge itself. |
| Triggers          | The user is redirected to this functionality from the Join Challenge functionality (see Use Case #18) |
| Preconditions     | The user has satisfied the conditions of the Join Challenge Functionality. |
| Actions           | 1. The User is presented with a prompt, which they attempt to copy type as quickly as possible.<br />2. Upon completing each prompt, if there is another prompt, it is presented to the User.<br />3. While the user types, the software tracks their speed, and mistakes<br />4. When they have completed all of the prompts, they are redirected to the view results functionality (see Use Case #16) |
| Alternative Paths | During the challenge(Steps 1-3), the User leaves the test. If they do this the software stops tracking their challenge and disposes of the incomplete information. It is not recorded to the results of the challenge. |
| Postconditions    | The User is viewing the View Results functionality (see Use Case #16). Their results have been recorded to the challenge records. |
| Acceptance Tests  | Create a mock challenge. Mock up the taking of that challenge. Confirm that the results are stored to the challenge records. |
| Iteration         | 1                                                            |
- - -
| Name              | View Results                                                 |
| ----------------- | ------------------------------------------------------------ |
| Users             | Competitor                                                   |
| Rationale         | After taking a test, users will want to be able to see how well they did in relation to others in their session, as well as how well they performed objectively in terms of speed and error rate. To support this the software should support a view of the player's results immediately after the challenge. |
| Triggers          | The User completes a challenge.                              |
| Preconditions     | The User has completely finished a challenge. They meet all the preconditions for Take Challenge (see Use Case #18) |
| Actions           | 1. The User completes the challenge.<br />2. Statistics about the user's speed, error rate, and performance, as well as their rankings are made visible to the User.<br />3. The User confirms that they are done looking at their performance stats, and are returned to their pre-challenge state. |
| Alternative Paths | None                                                         |
| Postconditions    | The User has returned to their pre-challenge state.          |
| Acceptance Tests  | Simulate a challenge. Confirm that the results are made visible. |
| Iteration         | 2                                                            |
- - -
| Name              | View Test Results by Room Identifier                         |
| ----------------- | ------------------------------------------------------------ |
| Users             | All Users                                                    |
| Rationale         | After the closing of a session, it is desirable to be able to look back at the aggregate results of the whole session. This should be an option for Hosts who have hosted that particular challenge, as well as for anonymous users who still have the old room identifier. |
| Triggers          | A User in the Competitor state who is not taking a challenge indicates that they would like to view the results for a particular room identifier. <br />OR A User in the Host state indicates they would like to view the results for one the challenges they have run. |
| Preconditions     | A challenge with a particular room identifier has been initiated and stopped and its results have been cached. |
| Actions           | 1. A User indicates that they would like to view results for a particular valid room identifier.<br />2. The aggregate results are made visible to the User<br />3. The User indicates when they would like to return to their starting state. |
| Alternative Paths | In Step 1, If the User is  a host they may have a method of indicating their desire to see a particular results page without needing to manually remember the room identifier both display the same Step 2 information. |
| Postconditions    | The User had returned to their starting state.               |
| Acceptance Tests  | Create a challenge with some mock results. Using this functionality, confirm that one can view those challenge results. |
| Iteration         | 3                                                            |
- - -
**Include a swim-lane diagram that illustrates the message flow and activities for following scenario:**

“A host a creates a challenge in a create/edit state. They then save this challenge. They can then either go back to editing the challenge, or initiate it. An initiated challenge can be stopped at any point. While initiated, competitors can join and take the challenge.”

![Swimlane Diagram](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/7b3258e0975e5646e74ad104814646e48ab0e96d/Documents/swimlaneDiagram.png)

----
## 2.4 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. **Scalability:** We believe that this assignment could be a useful and interesting software to host beyond the bounds of the classroom. Because of this we need to build our backend structure to safely support online hosting with at least a minimum level of security and scalability. Specifically we should build this software such that, if it is hosted on a remote source it can be used by a small number of users without any broken functionality due to the remote hosting.
2. **UX Ease of Use:** In order to ensure that our user interface is easy and straightforward to use, we will impose a rule that from any point in the software, one should require a **maximum** of 4 clicks to reach any other functionality in the software.
3. **Minimized Page Reloads:** Within time-sensitive parts of the application, (most obviously the timed challenge portion, this principle could apply elsewhere as well) the user should not experience **any** full page reloads to minimize the delay to users in time critical moments.
4. **English Localization:** Our typing interface, regardless of the method that we use, should support all valid English language characters and punctuation, both during challenge creation and challenge taking.

----
# 3. User Interface

## 3.1 UI Philosophy

1. **Simplicity:** All Pages should cohere to a design philosophy that keeps as much of the UI inline as possible, and maintains user focus on the middle of the screen. UI should also *only* show necessary and relevant elements to the user at any one time.
2. **Colors:** The UI theme will consist of 5 colors. A *primary*, *accent*, *contrast*, *background*, and *error* color will be included. Even if it is not on our initial roadmap, the CSS should be built to accommodate easy, or even live runtime theme changes that swap the values of these colors.
3. **Solarized Dark:** The initial color scheme will follow what is normally called a solarized dark color palate.  

## 3.2 Mock Ups

1. **Log In/Join Challenge Page Mock Up**

![Login Mockup](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/7b3258e0975e5646e74ad104814646e48ab0e96d/Documents/loginMockup.jfif)

2. **Take Challenge Page Mock Up**

![Take Challenge Mockup](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/7b3258e0975e5646e74ad104814646e48ab0e96d/Documents/takeChallengeMockup.jfif)

3. **View Challenges Page Mock Up**

![View Challenge Mockup](https://github.com/WSU-CptS322-Fall2021/TermProject-BadTeam/blob/7b3258e0975e5646e74ad104814646e48ab0e96d/Documents/viewChallengeMockup.jfif)

----
# 4. References

1. For an excellent UI/UX and typing interface reference from which to draw inspiration;
   www.monkeytype.com

2. As a model for distributed anonymous challenge/test presentation;
   www.kahoot.com

----

# Glossary of Terms

**Challenge:** A *challenge* is a series of user created prompts. These are presented to a given *challenger* in a preset order. The goal of the *challenger* is to copy the prompts in the interface as quickly and accurately as they can, and their stats are cached and marked as related to the challenge.

**Competitor:** A *competitor* is a user, either completely anonymous, or who has joined a *challenge* under a username. They have no password, do not have access to the same features as a *host* and can only take challenges.

**Host:** A *host* is an authenticated user who has logged in with a registered host account. They cannot take challenges, but can create, manage, and initiate them.

**Room Identifier:** A generic term for an identifier, probably a 6 digit alphanumeric code,  which can be used to uniquely identify a challenge session. We used the generic term here because we wanted to avoid straying into implementation details by specifying it as an alphanumeric code, as it could be a QR code, or some other implementation. 
