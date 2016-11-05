/*
 * CLASSIFIES the test data using all training data
 */
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>
using namespace std; 


string Classify(string pathOfTest, vector<vector<vector<double> * > * > & allTrain, vector<string> &allTrainPaths){
  int count = 0, min = 0;
  double val = 0, prev = 50000;
  vector<double> dist;
  vector<vector<double>> test;
  ifstream myfile;
  string line;

  // load the test file 
  myfile.open(pathOfTest);
  if (myfile.is_open())
  {
    // ignore the first line
    getline(myfile, line)
    while ( getline(myfile, line) )
    {
      vector<float> row = new vector<float> ();
      // read all points in one row -> line
      istringstream iss(line);
      copy( istream_iterator<string>(iss),
          istream_iterator<string>(),
          back_inserter(atof(row)) );

      test.push_back(row);
    }
    myfile.close();
  }

  string ret = "\n\"" + pathOfTest + "\" : ";

  for(auto train: allTrain){
    val = CalcDTW(train, test);

    if(prev > val){ // if prev is greater than current dtw distance update
      dist.push(val);
      min = count;
      prev = val;
    }

    count++;
  }

  ret += "\"" + allTrainPaths[min] + "\" : ";

  return ret;
}