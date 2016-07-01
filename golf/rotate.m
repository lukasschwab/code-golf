% Lukas Schwab, 7/4/14

% http://codegolf.stackexchange.com/questions/20154/rotate-simple-ascii-art/32938#32938
% Aha! Matrix manipulation! Easy!
% Originally the answer to a duplicate of this question...

a = [0,1,2,3,4,5; 6,7,8,9,0,1; 2,3,4,5,6,7,8,9,0,1,2,3];	% Array assignment, 0
k = 3 														% No. of rotations, -15
rot90(a)													% Rotates and prints, +10
															% 10 - 15 = -5