      
  
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