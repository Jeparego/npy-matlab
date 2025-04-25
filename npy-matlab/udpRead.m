
global data;
data = [];


port = 9870;
ip_id = "127.0.0.1";

u = udpport("datagram", "LocalHost", ip_id, "LocalPort", port);
disp("Lesting on port" + num2str(port));
configureCallback(u,"datagram", 1 ,@readUDP)


function readUDP(src,~)
    global data;
    disp("Data received:");
    read_data = read(src,1,"string");
    disp(read_data.Data + newline);
    struct_data = jsondecode(read_data.Data);
    new_data = [struct_data.strain_1; struct_data.strain_2; struct_data.strain_3; struct_data.temp; uint64(struct_data.timestamp)];
    data = [data new_data];
end
