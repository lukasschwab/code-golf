% Lukas Schwab 6/18/14

% http://codegolf.stackexchange.com/questions/31943/return-the-flipped-version-of-a-number/31986#31986
% POSTED

% --------------------

function [~]=flip(n)

f=[0,-1,5,-1,-1,2,9,-1,8,6];
f(n+1)

% --------------------

function [~]=flip(n)

[0,-1,5,-1,-1,2,9,-1,8,6];
ans(n+1)

% --------------------

% The two above have equal character counts (35) and are pretty effective.
% I'm assuming all the function notation gets left out...
% Could remove the semicolon to make it one character shorter.
% Note that you can't actually run this m-file.