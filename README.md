Zackary Cleveland - 2/6/2024 12:13

Completed my basis for the Integral and Data Analysis long prompts.
The data analysis prompt has achieved its desired function, but now needs to be polished and portfolio worthy.
More work is needed on the integral prompt. I got the simpson method to produce an 'accurate' result for 3 terms
of the specifed integral. It took an extreme # of N so i moved onto the Gaussian-Legendre method. This method with n=8
Revealed the difference between pi/2 that was expected, but at N = 2500. I want to locate sources of error within my code 
to attempt to get this number down. The first thing I may explore is a different domain change I.E. x = tanz. I'd also like to 
further explore the impact of different polynomial sets on the gaussian quadrature numerical integration approx. And in the end iterate
over values of N to find the smallest acceptable value of N. I also just need to organize the crap outta it when I get that all wrapped up too.

I'm also beginning to explore some project ideas, not really ready for the github yet (mostly drawings). I saw this grid created in the textbook to
visualize 2D electrostatics. The idea of a universal grid system/libary sounds extremely appealing to me. I.E. a grid system that would only require additional functions
to say, simulate electronic circuits or net forces in a truss. The idea is the underlying grid system would have all coordinate, distance, connections, nodes, joints, etc modules.
All that I would need to do for a type of physics would be to specify ohms law and electronics objects on the grid. So in summation: a system to represent nodes/joints and members on an XY grid.
Where the members and joints can have functionality programmed ontop of them, I.E., this member is a resistor or this joint is a double shear bolt. This would be ultimately awesome to accomplish
especially from a Statics and Mechanics of materials persepective. 
