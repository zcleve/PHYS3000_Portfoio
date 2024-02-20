Zackary Cleveland - 2/6/2024 12:13am

Completed my basis for the Integral and Data Analysis long prompts.
The data analysis prompt has achieved its desired function, but now needs to be polished and portfolio worthy. More work 
is needed on the integral prompt. I got the simpson method to produce an 'accurate' result for 3 terms of the specifed 
integral. It took an extreme # of N so i moved onto the Gaussian-Legendre method. This method with n=8 Revealed the difference 
between pi/2 that was expected, but at N = 2500. I want to locate sources of error within my code to attempt to get this number down. 
The first thing I may explore is a different domain change I.E. x = tanz. I'd also like to further explore the impact of different polynomial 
sets on the gaussian quadrature numerical integration approx. And in the end iterate over values of N to find the smallest acceptable value of N. 
I also just need to organize the crap outta it when I get that all wrapped up too.

I'm also beginning to explore some project ideas, not really ready for the github yet (mostly drawings). I saw this grid created in the textbook to
visualize 2D electrostatics. The idea of a universal grid system/libary sounds extremely appealing to me. I.E. a grid system that would only require additional functions
to say, simulate electronic circuits or net forces in a truss. The idea is the underlying grid system would have all coordinate, distance, connections, nodes, joints, etc modules.
All that I would need to do for a type of physics would be to specify ohms law and electronics objects on the grid. So in summation: a system to represent nodes/joints and members on an XY grid.
Where the members and joints can have functionality programmed ontop of them, I.E., this member is a resistor or this joint is a double shear bolt. This would be ultimately awesome to accomplish
especially from a Statics and Mechanics of materials persepective. 



Zackary Cleveland - 2/19/2024 9:53pm

Worked on a lot of stuff between the last progress reports. Explored a bit of CFD as discussed and as seen in the CFD/Learning directory. Mostly pushed ODEs / PDEs and their numerical solutions.
Specificially finsihed the two drag prompts from prompt bank 2, the long and short one. Also did some crude data analysis for my mechanics of materials class, as seen in MECH2500. Numerical DEs contains some
work from in class. TOOLS contains some new and more fleshed out personal use/reuse libraries. Going to work on consoldiating a pretty solid ODE and PDE libarary over the next week to handle essentially
any form I could possible come across. Will be sending a Project Proposal to you ideally before thursday.
