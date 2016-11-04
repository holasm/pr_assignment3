train_model = svmtrain(allTrainingLabels, allTrainingFeatures);
result = svmpredict(allTestLabels, allTestFeatures, train_model);
