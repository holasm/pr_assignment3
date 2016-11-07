addpath(genpath('/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dhmm/codes/HMMall'))
path= '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dhmm/data/digit_data/';%where all images are there;
inputdata=[];
filelength=[];
noofclass=9;
for i=0:noofclass
    tempinput=[];class=[];
    temp= sprintf('%s%d/*.txt',path,i);
    temp1=sprintf('%s%d/',path,i);
    file=dir(temp);
    for j=1:length(file)
        temp2=load(fullfile(temp1,file(j).name),'-ascii');
        filelength(i+1,j)=size(temp2,1);
        tempinput=[tempinput;temp2];
    end
    class(1:size(tempinput,1))=i+1;
    tempinput=horzcat(tempinput,class');
    inputdata=[inputdata;tempinput];
end

[id ,~]=kmeans(inputdata,10);
id(:,2)=inputdata(:,40);

start_ind=1;
end_ind=0;
test_cell=cell(1);
for i=1:10
    train_data=cell(128,1);
    test_data=cell(32,2);
    for j=1:128
        end_ind=start_ind+filelength(i,j)-1;
        train_data{j,1}=id(start_ind:end_ind,1)';
        start_ind=end_ind+1;
    end
    train_cell{1,i}=train_data;
    for j=129:160
        end_ind=start_ind+filelength(i,j)-1;
        test_data{j-128,1}=id(start_ind:end_ind,1)';
        test_data{j-128,2}=i;
        start_ind=end_ind+1;
    end
    test_cell{1}=[test_cell{1};test_data];
end

states=15;
outputsymbols=10;
parameter=cell(10,3);
for i=1:10
    parameter{i,1}=normalise(rand(states,1)); %https://www.cs.ubc.ca/~murphyk/Software/HMM/hmm_usage.html
    parameter{i,2}=mk_stochastic(rand(states,states)); %https://www.cs.ubc.ca/~murphyk/Software/HMM/hmm.html
    parameter{i,3}=mk_stochastic(rand(states,outputsymbols));
end


for i=1:10
        [~, parameter{i,1},parameter{i,2},parameter{i,3}] =dhmm_em(train_cell{1,i}',parameter{i,1}, parameter{i,2}, parameter{i,3},'max_iter', 50);
end

accuracy=0;
for j=1:length(test_cell{1,1})  
    for i=1:10
        likelihood(i)=dhmm_logprob(test_cell{1,1}{j,1}, parameter{i,1}, parameter{i,2}, parameter{i,3});
    end
    [~,idx]=max(likelihood);
    if(idx==test_cell{1,1}{j,2})
        accuracy=accuracy+1;
    end
end