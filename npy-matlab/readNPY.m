

function data = readNPY(filename)
% Function to read NPY files into matlab.
% *** Only reads a subset of all possible NPY files, specifically N-D arrays of certain data types.
% See https://github.com/kwikteam/npy-matlab/blob/master/tests/npy.ipynb for
% more.
%

[shape, dataType, fortranOrder, littleEndian, totalHeaderLength, ~] = readNPYheader(filename);

if littleEndian
    fid = fopen(filename, 'r', 'l');
else
    fid = fopen(filename, 'r', 'b');
end

try

    [~] = fread(fid, totalHeaderLength, 'uint8');


    data = [];
    % read the data
    for i = 1:shape
        data = [data [fread(fid, 4, [dataType '=>' dataType]); fread(fid, 1, 'uint64=>uint64')]];
    end
    

    if length(shape)>1 && ~fortranOrder
        data = reshape(data, shape(end:-1:1));
        data = permute(data, [length(shape):-1:1]);
    elseif length(shape)>1
        data = reshape(data, shape);
    end

    fclose(fid);

catch me
    fclose(fid);
    rethrow(me);
end
