path1 = '../../data/processed/train/coast.txt';
path2 = '../../data/processed/train/forest.txt';
path3 = '../../data/processed/train/highway.txt';
path4 = '../../data/processed/train/insidecity.txt';
path5 = '../../data/processed/train/mountain.txt';
path6 = '../../data/processed/train/opencountry.txt';
path7 = '../../data/processed/train/street.txt';
path8 = '../../data/processed/train/tallbuildings.txt';

allTrainingFeatures = [];
allTrainingLabels = [];
allTestFeatures = [];
allTestLabels = [];

%-------------------------------------------------
% READ ALL TRAINING FEATURE LIST
%-------------------------------------------------

[featureList, labels] = LoadAndLabelFeature(path1, 1);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path2, 2);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path3, 3);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path4, 4);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path5, 5);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path6, 6);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path7, 7);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path8, 8);
allTrainingFeatures = vertcat(allTrainingFeatures, featureList);
allTrainingLabels = vertcat(allTrainingLabels, labels);

%-------------------------------------------------
% READ ALL TEST FEATURE LIST
%-------------------------------------------------

path1 = '../../data/processed/test/coast.txt';
path2 = '../../data/processed/test/forest.txt';
path3 = '../../data/processed/test/highway.txt';
path4 = '../../data/processed/test/insidecity.txt';
path5 = '../../data/processed/test/mountain.txt';
path6 = '../../data/processed/test/opencountry.txt';
path7 = '../../data/processed/test/street.txt';
path8 = '../../data/processed/test/tallbuildings.txt';

[featureList, labels] = LoadAndLabelFeature(path1, 1);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path2, 2);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path3, 3);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path4, 4);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path5, 5);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path6, 6);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path7, 7);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

[featureList, labels] = LoadAndLabelFeature(path8, 8);
allTestFeatures = vertcat(allTestFeatures, featureList);
allTestLabels = vertcat(allTestLabels, labels);

% train_model = svmtrain(allTrainingLabels, allTrainingFeatures);
% result = svmpredict(allTestLabels, allTestFeatures, train_model);
