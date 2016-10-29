% Convert feature files to HTK readable format. It accepts a list file as
% the input, Column1 with name of feature files, and Column2 with name of
% HTK files


function[]=Convert_To_HTK(filelist)

    fp=fopen(filelist,'r');
    samplingperiod=(1/44100);
    
    while (1)        
        line = fgetl(fp);
        if line == -1,
            break
        end
        
        inputFileName = line;
        outputFileName = regexprep(line, 'mfcc', 'htk');
               disp(outputFileName)
        fprintf('%s %s\n',inputFileName,outputFileName); 
        mydata = load(inputFileName);                     
        
        writehtk_lite(outputFileName,mydata,samplingperiod,9);
    end

    fclose(fp);
end