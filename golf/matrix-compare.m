% Lukas Schwab 6/18/14

% http://codegolf.stackexchange.com/questions/31684/randomized-algorithm-in-matrices
% This question was a hard one to decipher but I did my best. Thank god for matrix tools in matlab!

%---------------------

function [x]=compare(o,t)

if sum(sum(isequal(o,t)))+1==n^2
	x=1;
else
	x=0;
end

%---------------------

% Does this meet the complexity requriement?