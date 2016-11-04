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

int main(int argc, char const *argv[])
{
  vector<vector<vector<double> * > * > allTrain;
  string testFiles = "./../../data/processed/test.txt";
  string trainFiles = "./../../data/processed/train.txt";
  ifstream trainFile, trainListFile;
  string line1, line2;
  vector<double> * row;
  vector<vector<double> * > * trainFileData;
  streambuf *cinbuf = cin.rdbuf(); //save old buf
  string str;
  int count = 0;
  // load all training data in a huge vector
  trainListFile.open(trainFiles); // open file list file
  if(trainListFile.is_open()){
    while ( getline(trainListFile, line1) )
    {
      trainFileData = new vector<vector<double> * > ();
      trainFile.open(line1); // open one train file

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

      allTrain.push_back(trainFileData);
    } // while for fileList file

    trainListFile.close();
  } // if

  if(LOG_ALL){
    auto f1 = allTrain[1];
    for(auto f2: *f1){
      for(auto f3: *f2){
        cout << f3 << " ";
      }
      cout << endl;
    }
  }

  // √ calc dtw distance from one tet to all training file √
  
  // save the result in a file
  // later process output
  // 

  cin.rdbuf(cinbuf);
  return 0;
}