# UMass Fall 2022 Info90S - Project 1 Slayer Puzzle

Overview

One strategy for finding a solution to a number puzzle is to describe the solution by a set of algebraic constraints and then solve the constraints. Consider the following puzzle:

The Jets and the Sharks are the names of two rival dance teams. The Jets say to the Sharks, “If one of you joins our team, then our team will double the size of yours”. The Sharks reply, “If one of you joins our team, then the sizes of our teams will be equal”. What are the sizes of the two teams?

If the sizes of the Jets and Sharks are denoted by j and s, respectively, then any solution to this puzzle satisfies the constraints: 

j+1=2(s-1)
s+1=j-1

Solving these constraints leads to a solution to the puzzle. For example, j=7 and s=5. While solving the constraints in this example is straightforward, solving constraints for some number problems can be hard. In such cases, another strategy is to guess possible solutions and then check if the guess works. Consider, the following puzzle:

What digits can replace the letters A, B, and C to make a 3-digit number ABC for which the following equation is true: ABC=A∙B∙C∙(A+B+C).

This puzzle is not easily solved directly. But any guess for the 3-digit number ABC can be easily checked to see if it satisfies the equation. For example, suppose you guess that ABC is 123. This guess does not work because it requires A=1, B=2, C=3, and 123≠1∙2∙3∙(1+2+3). In contrast, the guess that ABC is 135 works since 135=1∙3∙5∙(1+3+5).

You will write a program that can be used to check guesses for the following puzzle:

For what 6-digit number SLAYER is the following equation true, where each letter stands for the digit in the position shown: SLAYER+SLAYER+SLAYER=LAYERS.
