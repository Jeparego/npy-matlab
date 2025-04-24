data = readNPY('sensor_dump.npy');

figure('Name','Numppy Data','NumberTitle','off','Position', [10, 20, 1000, 750]);

time_stamp = data(5,:);

subplot(2,2,1)
plot(time_stamp, data(1,:));
xlabel('time');
ylabel('Strain 1 Values');
title('Strain 1');
grid on;

subplot(2,2,2)
plot(time_stamp, data(2,:));
xlabel('time');
ylabel('Strain 2 Values');
title('Strain 2');
grid on;

subplot(2,2,3)
plot(time_stamp, data(3,:));
xlabel('time');
ylabel('Strain 3 Values');
title('Strain 3');
grid on;

subplot(2,2,4)
plot(time_stamp, data(4,:));
xlabel('time');
ylabel('Temperature °C');
title('Temperature');
grid on;