# Tips for solving coding problems using Recursion

## Identifying a recursive problem

  - You must "try" every possibility (e.g: permutations)
  - When it deals with recursive objects(Graphs, Trees)
 
 
## Solving the problem

### Top-down

* Define a way to break the problem down into a smaller one
* Assume you have a magical function that will solve the smaller problem for you (which is really just the function you’re writing)

### Bottom-up

* Start from the base case and solve incrementally harder problems
* Figure out how you can use an easier instantiation of the problem to solve the current, harder problem (Ex: using the permutations of [1, 2] to generate the permutations of [1, 2, 3])


## Analazying the Algorithm

