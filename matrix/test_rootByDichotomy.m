x = linspace(0,  pi, 400);
subplot(221)
plot(x, rootByDichotomy_f(x));
drawnow;

x = linspace(1*pi, 2*pi, 400);
subplot(222)
plot(x, rootByDichotomy_f(x));
drawnow;

x = linspace(2*pi, 3*pi, 400);
subplot(223)
plot(x, rootByDichotomy_f(x));
drawnow;

x = linspace(3*pi, 4*pi, 400);
subplot(224)
plot(x, rootByDichotomy_f(x));
drawnow;

sections = singleRootSection(0, 4*pi, 4);
% sections =
%     1.5708    3.1416
%     3.1416    4.7124
%     7.8540    9.4248
%     9.4248   10.9956
n = size(sections, 1)
format long
for i = 1:n
    root = rootByDichotomy(sections(i, 1), sections(i, 2), 1e-3)
end
% root =  1.88066044594780
% root =  4.69408906895421
% root =  7.85475761253710
% root =  10.9955407223719

% subplot(211),imshow(.....);
% subplot(212),imhist(.....);