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

sections = singleRootSection(0, 4*pi, 4)