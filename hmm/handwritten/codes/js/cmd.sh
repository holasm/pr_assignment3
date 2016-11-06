echo "Creating all .mfcc path files"
node create_mfcc_path_list.js
echo "Creating all .mlf files"
node create_mlf.js
echo "Creating all .scp files"
node create_scp.js
echo "Creating all grammer/wlist/lexicon files"
node create_grammer.js