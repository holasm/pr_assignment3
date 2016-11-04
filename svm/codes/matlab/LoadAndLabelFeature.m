function [features, labels]= LoadAndLabelFeature(filelist, label)
    disp(filelist)
    features = [];
    fp=fopen(filelist,'r');

    while (1)        
        line = fgetl(fp);
        disp(line)
        if line == -1,
            break
        end
        features = vertcat(features, load(line));
    end
  
    row = size(features, 1);
    labels = ones(row, 1);
    labels = labels * label;
    fclose(fp);
end