# Broadbean tech assignment

You should not spend more than a few hours on this.

If you're not finished by then, make some notes in the notebook.md
file what your next steps would be.


## Format

* Unpack the tarball with the git repo and the workspace
* Create a branch with your name from master
* Do the work and check it in. Smaller commits are nicer.
* Tar up the repo and the workspace and send back


## Requirements

### Business requirements

We need software to model a six-sided die (1-6 dots), and a handful of
5 dice.

Given one throw of the handful of dice, it should be able to identify
these outcomes:

- two-of-a-kind
- three-of-a-kind

A) Design and write code for this. Write test for this as needed, but
at minimum to identify the different outcomes.

B) Write a tiny command line script that throws a handful of dice and
prints the dots for each die, and the best outcome, e.g.

    $ ./bin/throw-dice
    4 4 2 6 1
    Two of a kind

    $ ./bin/throw-dice
    4 4 2 3 4
    Three of a kind


### Practical Requirements

Make it possible to:

* install any dependencies using something like `cpanm --installdeps .`
* run tests using something like `prove -r t`
* run the script as described above


## Your Task

* Given the requirements, create some modules/classes/whatever to
  capture the design. This is a small problem, but imagine that it is
  larger and needs to fit into a large system, with e.g. a web
  application.
* Review the requirements, are they good/bad/incomplete?


## Deliverables

* Code and tests, script
* Review of requirements, a sentence or three


## Followup interview

* We'll ask about the solution, and how you approached the problem.
* If possible, it's useful if you can share your screen with the code
  (if you can't, it's not a problem)
