%x = linspace(0, 4*pi, 400);

x = linspace(0,  pi, 400);
plot(x, rootByDichotomy_f(x));
drawnow;
pause;

x = linspace(1*pi, 2*pi, 400);
plot(x, rootByDichotomy_f(x));
drawnow;
pause;

x = linspace(2*pi, 3*pi, 400);
plot(x, rootByDichotomy_f(x));
drawnow;
pause;

x = linspace(3*pi, 4*pi, 400);
plot(x, rootByDichotomy_f(x));
drawnow;
pause;

sections = singleRootSection(0, 4*pi, 4);
% sections =
%     1.5708    3.1416
%     3.1416    4.7124
%     7.8540    9.4248
%     9.4248   10.9956
n = size(sections, 1)
for i = 1:n
    root = rootByDichotomy(sections(i, 1), sections(i, 2), 1e-3)
end