
global data;
data = [];




u = udpport("datagram", "LocalHost", "127.0.0.1", "LocalPort", 9870);
configureCallback(u,"datagram", 1 ,@readUDPData)


function readUDPData(src,~)
    global data;
    disp("Data received:");
    read_data = read(src,1,"string");
    disp(read_data.Data + newline);
    struct_data = jsondecode(read_data.Data);
    new_data = [struct_data.strain_1; struct_data.strain_2; struct_data.strain_3; struct_data.temp; uint64(struct_data.timestamp)];
    data = [data new_data];
end
