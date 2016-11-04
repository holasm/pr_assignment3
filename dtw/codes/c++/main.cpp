#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stdlib.h>     /* atof */

using namespace std; 

const int LOG_FILE = 0;
const int LOG_DATA = 0;
const int LOG_STAT = 0;
const int LOG_LINE = 0;
const int LOG_ALL = 0;

vector<vector<double> * > * LoadFile(string filePath){
  ifstream trainFile;
  vector<vector<double> * > * trainFileData = new vector<vector<double> * > ();
  trainFile.open(filePath); // open one train file
  string line2;
  vector<double> * row;
  string str;
  int count = 0;
  
  streambuf *cinbuf = cin.rdbuf(); //save old buf

  if (trainFile.is_open())
  {
    getline(trainFile, line2); // ignore the first line

    // load all test files path in a vector
    while ( getline(trainFile, line2) )
    {
      row = new vector<double> ();

      // read all points in one row -> line
      istringstream iss(line2);

      cin.rdbuf( iss.rdbuf() ); //redirect std::cin to iss.txt!

      while(cin >> str){
        if(LOG_LINE) cout << str << " ";
        row->push_back( stof(str) );
      };

      if(LOG_LINE) cout << endl;
      if(LOG_LINE) cout << row->size() << endl;

      if(row->size() > 0){
        trainFileData->push_back(row);
        // cout << count << endl;
        if(LOG_STAT) cout << count++ << endl;
      } else {
        cout << "\nError... in trainFile push_back" << endl;
        exit(0);
      }
    } // while for one file

    if(LOG_FILE) cout << "\n";
    trainFile.close();  
    if(LOG_DATA) cout << trainFileData->size() << endl;
  } // if
  
  cin.rdbuf(cinbuf);

  return trainFileData;
}

string Classify(string & pathOfTest, vector<vector<vector<double> * > * > & allTrain, vector<string> & allTrainPaths, int turn){
  int count = 0, min = 0;
  double val = 0, dist = 50000;
  vector<vector<double> * > * test;
  ifstream myfile;
  string line;

  // load the test file 
  test = LoadFile(pathOfTest);

  string ret = "{\n\"" + pathOfTest + "\" : ";

  for(auto train: allTrain){
    val = 1;// CalcDTW(train, test);

    if(val < dist){ // if prev is greater than current dtw distance update
      dist = val;
      min = count;
    }

    count++;
  }

  ret += "\"" + allTrainPaths[min] + "\"";
  
  ret += ",\n\""; // ,\n
  ret += to_string(turn) + "\" : " + "\"" + to_string(dist);
  ret += "\"";

  ret += "\n}";

  return ret;
}

int main(int argc, char const *argv[])
{
  string s1 = "./../../data/processed/test/Ariyalur.mfcc/1039Ariyalur.mfcc";
  string s2 = "./../../data/processed/test/Ariyalur.mfcc/1039Ariyalur.mfcc";
  return 0;
}

// int main(int argc, char const *argv[])
// {
//   string testFiles = "./../../data/processed/test.txt";
//   string trainFiles = "./../../data/processed/train.txt";
//   vector<vector<vector<double> * > * > allTrain;
//   vector<string> allTrainPaths, result;
  
//   string line1, line2;
//   ifstream trainListFile, testListFiles;
//   ofstream testResultFile;


//   // ----------------------------------------
//   // load all training data in a huge vector
//   // ----------------------------------------
//   trainListFile.open(trainFiles); // open file list file
//   if(trainListFile.is_open()){
//     while ( getline(trainListFile, line1) )
//     {
//       allTrain.push_back(LoadFile(line1));
//       allTrainPaths.push_back(line1);
//     } // while for fileList file

//     trainListFile.close();
//   } // if

//   if(LOG_ALL){
//     auto f1 = allTrain[1];
//     for(auto f2: *f1){
//       for(auto f3: *f2){
//         cout << f3 << " ";
//       }
//       cout << endl;
//     }
//   }

//   // -------------------------------------------
//   // classify all test files
//   // -------------------------------------------
//   testListFiles.open(testFiles);
//   int count = 0;
//   if(testListFiles.is_open()){
//     while(getline(testListFiles, line1)){
//       // √ calc dtw distance from one tet to all training file √
//       line2 = Classify(line1, allTrain, allTrainPaths, count);
//       result.push_back(line2);
//       count++;
//     }
//     trainListFile.close();
//   }

//   // cout << result.size() << endl;

//   testResultFile.open("./../../su/result.json");
//   testResultFile << "{\n";
//   for(auto item: result){
//     testResultFile << item <<",\n";
//   }

//   testResultFile << "}";

//   testResultFile.close();
//   // save the result in a file
//   // later process output

//   return 0;
// }












