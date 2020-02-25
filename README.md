# Git Tutorial
This tutorial is intended to teach you how to use git for version control, proper branch workflow, and handling merge conflicts.

## Lets create a git repository
Navigate to the project in gitlab underwhich you'd like to create your repository and, near the top-right corner, click the green "New Project" button. I am creating this one under RSI Development Team > RSI Internal and naming it "git tutorial".

<image>

Fill in the project name and click the green "Create Project" button at the bottom. Then, follow the instructions for cloning your repo to your computer.

<image>

## Lets create our first file, the README.md
Currently, you are on the master branch. The master branch should be reserved for production code only. Lets initialize a README.md and then switch over to a new branch.

    touch README.md

    git add README.md
    git commit -m 'initialized README.md'
    git push

    git checkout -b dev

let us break down the git commands:

git add - stages the file for commiting

git commit -m - appends a custom note to describe changes that were made

git push - pushes the changes to the repository

git checkout -b - use 'git checkout' to checkout another existing branch. Use the '-b' to create a new branch.



