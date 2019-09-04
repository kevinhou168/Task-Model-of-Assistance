# Task Model of Assistance
## Description
The Task Model of Assistance is a classifier of assistance based on a person's task progress. 
Utilizing Dana Nau's Pyhop, found at https://bitbucket.org/dananau/pyhop/src/default/, we are able to determine 
a routine of steps needed for completing a specific task. This means that we can see how far a person is from finishing the
task, as well as whether the steps they take are productive towards the finish by comparing with the Pyhop routine. For another, maze-based implementation of Pyhop, see https://github.com/kevinhou168/mazeHTN.

**Sample Task:** The task we've based our model on is a medication sorting task. A participant is placed in front of
a grid, with the x-axis symbolizing days and the y-axis symbolizing certain times.
Given two types of pills(greens and blues) as well as criteria for the times and days at which they must be taken, 
the participants must sort them into the correct boxes. These participants were filmed in the process.

![ParticipantVideo](https://i.imgur.com/gWcdOut.jpg)

**Currently, work on the Task Model has shifted after it has been integrated into the Computational Model of Assistance, 
a multi-model that utilizes multiple signals such as the medication sorter's gaze direction, task progress, and 
lexical cues to determine a measure of whether assistance is needed.**
