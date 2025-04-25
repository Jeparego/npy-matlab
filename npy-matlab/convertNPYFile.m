[data, time_stamp] = readNPY('sensor_dump.npy');

%array with date and time in wich the values were recorde according to the
%order of data received. Reference of conversion is numpy epoch time (datetime(1970,1,1,0,0,0)
converted_time_stamp = datetime(time_stamp,'ConvertFrom','epochtime','Epoch',datetime(1970,1,1,0,0,0),'TicksPerSecond',1e6, 'Format','uuuu-MM-dd''T''HH:mm:ss.SSSSSS');

figure('Name','Numppy Data','NumberTitle','off','Position', [10, 20, 1000, 750]);

subplot(2,2,1);
plot(time_stamp, data(1,:));
ylim([-0.01 0.01]);
xlabel('time');
ylabel('Strain 1 Values');
title('Strain 1');
grid on;

subplot(2,2,2)
plot(time_stamp, data(2,:));
ylim([-0.01 0.01]);
xlabel('time');
ylabel('Strain 2 Values');
title('Strain 2');
grid on;

subplot(2,2,3)
plot(time_stamp, data(3,:));
ylim([-0.01 0.01]);
xlabel('time');
ylabel('Strain 3 Values');
title('Strain 3');
grid on;

subplot(2,2,4)
plot(time_stamp, data(4,:));
ylim([0 50]);
xlabel('time');
ylabel('Temperature °C');
title('Temperature');
grid on;