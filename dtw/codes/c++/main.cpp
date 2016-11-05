#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <limits.h>
#include <functional>
#include <numeric>
#include <math.h>

using namespace std; 

const int LOG_FILE = 0;
const int LOG_DATA = 0;
const int LOG_STAT = 0;
const int LOG_LINE = 0;
const int LOG_ALL = 0;

double FindMin(double a, double b, double c){
  b = a<b ? a:b;
  c = b<c ? b:c;
  return c;
}

/******************************************************
 * CALCULATE the norm of difference oftwo vector
 * @return: norm(first[] - second[])
 ******************************************************/

double Norm(vector<double> * first, vector<double> * second){
  vector<float> vec(first->size());
  double ret = 0;

  if(first->size() != second->size()){
    cout << "Error in Norm calculation" << endl;
    exit(1);
  } else {
    for(int i = first->size()-1; i >= 0; i--){
      vec.push_back((*first)[i] - (*second)[i]);
    }// for
  }

  for(auto v: vec){
    ret += v*v;
    // cout << ret << " "<< v*v << endl;
  }
  // cout << "-------------------------------------------------------------" << endl;
  return sqrt(ret);
}

double DTW(vector<vector<double> * > * test, vector<vector<double> * > * train) {
  double ret = 50000;
  double inf = 50000;
  int r, c;
  ofstream output;
  ofstream trainstream;
  string outputFile = "test.txt";
  string trainFile = "train.txt";

  // 
  r = test->size();
  c = train->size();

  vector<vector<float> > Dist(r, vector<float>(c, 0));

  // for(auto it = Dist[0].begin(); it < Dist[0].end(); it++){
  //   *it = 500000;
  // }
  // for(int i = Dist.size()-1; i >= 0; i--){
  //   *Dist[i].begin() = 500000; 
  // }


  for(int i = 0; i < r; i++){
    for(int j = 0; j < c; j++){
      Dist[i][j] = Norm( (*test)[i], (*train)[j] );
    }
  }
  

  Dist[0][0] = 0;

  for(int i = 0; i < r; i++){
    for(int j = 0; j < c; j++){
      if(i==0 && j==0){
        Dist[i][j] = Dist[i][j] + FindMin( 0, inf, inf );
      } else if( i==0 && j!= 0){
        Dist[i][j] = Dist[i][j] + FindMin( inf, Dist[i][j-1], inf );
      } else if( j==0 && i !=0 ){
        Dist[i][j] = Dist[i][j] + FindMin( inf, inf, Dist[i-1][j] );
      } else {
        Dist[i][j] = Dist[i][j] + FindMin( Dist[i-1][j-1], Dist[i][j-1], Dist[i-1][j] );
      }
    }
  }

  // output.open(outputFile);
  // for(auto vec: Dist){
  //   for(auto d: vec){
  //     output << d << " ";
  //   }
  //   output << "\n";
  // }
  // output.close();
  
  // cout << Dist[r-1][c-1] << endl;
  return Dist[r-1][c-1] / (r+c);
}

/******************************************************
 * LOADS the .mfcc feature file to vector
 * @return: file data in vector form
 ******************************************************/

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


/******************************************************
 * Classifiy the file at -i:pathOfTest
 * @return: strigified json object of classified file
 ******************************************************/

string Classify(string & pathOfTest, vector<vector<vector<double> * > * > & allTrain, vector<string> & allTrainPaths){
  int count = 0, min = 0;
  double val = 0, dist = 50000;
  vector<vector<double> * > * test;
  ifstream myfile;
  string line;

  // load the test file 
  test = LoadFile(pathOfTest);

  string ret = "{\n\"" + pathOfTest + "\" : ";

  for(auto train: allTrain){
    // create  multiple thread
    val = DTW(test, train);// CalcDTW(train, test);

    if(val < dist){ // if prev is greater than current dtw distance update
      dist = val;
      min = count;
    }

    count++;
    // cout << count << endl;
  }

  ret += "\"" + allTrainPaths[min] + "\"";
  
  ret += ",\n"; // ,
  ret += "\"dist\" : \"" + to_string(dist);
  ret += "\"";

  ret += "\n}";

  return ret;
}

int main(int argc, char const *argv[])
{
  string s1 = "./../../data/processed/test/Coimbatore.mfcc/1056_Coimbatore_.mfcc";
  string s2 = "./../../data/processed/train/Ariyalur.mfcc/1044Ariyalur_2.mfcc";
  ofstream output_1, output_2;

  vector<vector<double> * > * test = LoadFile(s1);
  vector<vector<double> * > * train = LoadFile(s2);

  // cout << Norm((*test)[1], (*test)[2]) << endl;

  // output_1.open("test_1.txt");
  // for(auto vec: *test){
  //   for(auto d: *vec){
  //     output_1 << d << " ";
  //   }
  //   output_1 << "\n";
  // }
  // output_1.close();

  // output_2.open("test_2.txt");
  // for(auto vec: *train){
  //   for(auto d: *vec){
  //     output_2 << d << " ";
  //   }
  //   output_2 << "\n";
  // }
  // output_2.close();

  cout << DTW(test, train) << endl;

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
  
//     //-----------------------------------
//     // testResultFile.open("./../../su/result.json", ios::app);
//     // testResultFile << "{\n";

//     // testListFiles.open(testFiles);
    
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);
    
//     // cout << line1 << endl;
//     // testResultFile << Classify(line1, allTrain, allTrainPaths) << endl;
    
//     // getline(testListFiles, line1);
//     // getline(testListFiles, line1);


//     // cout << line1 << endl;
//     // testResultFile << Classify(line1, allTrain, allTrainPaths) << endl;

//     // trainListFile.close();
//     //-----------------------------------

//   testResultFile.open("./../../su/result.json", ios::app);
//   testResultFile << "{\n";

//   int count = 0;

//   testListFiles.open(testFiles);
//   if(testListFiles.is_open()){
//     while(getline(testListFiles, line1)){
//       // √ calc dtw distance from one tet to all training file √
//       line2 = Classify(line1, allTrain, allTrainPaths);

//       testResultFile << line2 <<",\n"; // save in file

//       result.push_back(line2);
//       count++;
//       cout << count << endl;
//     }
//     trainListFile.close();
//   }

//   // cout << result.size() << endl;

//   // for(auto item: result){
//   //   testResultFile << item <<",\n";
//   // }

//   testResultFile << "}";

//   testResultFile.close();
//   // save the result in a file
//   // later process output

//   return 0;
// }