STATEMENT.md

##Project Statement

The goal of this project is to create a simple command-line based expense management system that allows multiple users to record shared expenses and automatically calculate how much each participant owes or is owed. The system stores data persistently, processes equal splits among all registered users, and generates a clear settlement plan.

This project aligns with the requirement of building an original, self-contained application that demonstrates understanding of fundamental programming concepts such as file handling, data structures, control flow, and algorithmic problem-solving.

##Scope of the Project

The system includes the following core functionalities:

Adding participants to the expense pool.

Recording bills with a description, total amount, and payer name.

Automatically splitting each bill equally among all registered users.

Maintaining persistent storage using a JSON file (data.json).

Computing net balances for each participant.

Generating settlement instructions to simplify final payments.

Optional CSV export of settlement results.

The project focuses on equal-split expense tracking only. Advanced features such as custom percentage splits, editing/deleting entries, or multi-group management are outside the current scope.

##Problem Description

When multiple people share expenses, manually calculating who owes whom becomes tedious and error-prone. Even simple outings or shared living situations involve multiple payers and uneven contributions. Without a structured system, participants often struggle to track individual balances and determine a fair settlement.

The program solves this issue by:

Recording all transactions,

Calculating exact balances for each participant,

And generating the minimum number of transactions required to settle all dues.

This eliminates manual calculations and reduces confusion.

##Target Users

Small groups of friends sharing outing or trip expenses.

Roommates splitting monthly costs.

Students collaborating on group activities.

Anyone needing a basic equal-split expense tracker without complex features or external libraries.

The tool is designed for users who prefer a simple command-line interface and require quick, accurate settlement calculations.

##High-Level Features

User Management
Add and store participant names in a persistent file.

Bill Recording
Store expense details including:

Description

Amount

Payer name

Equal distribution across all users

Balance Calculation
Compute per-user balances based on payments and shares.

Settlement Generation
Produce clear instructions in the format:
