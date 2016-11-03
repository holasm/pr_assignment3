#!/bin/bash
# the steps are followed as per link
# http://sail.usc.edu/old/courses/EE619/digit-recognition-tutorial.txt

# @author: Subhasis Maity
root=$PWD
grammerfile="grammar" # the file name is written explicitly inside the cmd ->HParse

# echo "-----------------INFO--------------------"
# node ./scripts/create_grammer.js # creates grammer, wlist, lexicon
# node ./scripts/create_mlf.js # creates MASTER LABEL FILE

echo "-----------------INFO--------------------"
printf "Step 1 => Create HTK wordnet lattice\n"
printf "\$_>: HParse io/grammer io/gen/wordnet\n"
printf "grammerfile -> $grammerfile\n\n"

HParse io/created/grammer io/gen/wordnet # Convert this grammar to an HTK wordnet lattice using the HParse tool

# create lexicon, wlist ***with proper order***

echo "-----------------INFO--------------------"
printf "Step 2 => Create the dictionary\n"
printf "\$_>: HDMan -m -w wlist -n models1 -l dlog dict lexicon\n\n"

HDMan -m -w io/created/wlist -n io/gen/models1 -l io/gen/dlog io/gen/dict io/created/lexicon

echo "-----------------INFO--------------------"
echo "***SKIPPING***"
printf "Step 3 => Expanding the word transcriptions into model transcriptions\n"
printf "\$_>: HLEd -l '*' -d dict -i io/models/models0.mlf io/created/mkphones0.led io/created/mlf/man.mlf\n"
printf "\$_>: HLEd -l '*' -d dict -i io/models/models1.mlf io/created/mkphones0.led io/created/mlf/woman.mlf\n\n"

# HLEd -l '*' -d dict -i io/models/models0.mlf io/created/mkphones0.led io/created/mlf/all.mlf


echo "-----------------INFO--------------------"
printf "Step 4 => Encoding the data.\n"
printf "\$_>: HCopy -T 1 -C io/created/config -S io/created/scp/man.scp\n"
printf "\$_>: HCopy -T 1 -C io/created/config -S io/created/scp/woman.scp\n\n"

# HCompV -C io/created/config -f 0.01 -m -S io/created/train/man.scp -M hmm0 io/created/proto

HCompV -f 0.01 -m -S all.scp -M hmm0 proto # in hmm folder
 

HERest  -I all.mlf -S all.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 models0
HERest  -I all.mlf -S all.scp -H hmm1/macros -H hmm1/hmmdefs -M hmm2 models0
HERest  -I all.mlf -S all.scp -H hmm2/macros -H hmm2/hmmdefs -M hmm3 models0
HERest  -I all.mlf -S all.scp -H hmm3/macros -H hmm3/hmmdefs -M hmm4 models0

HVite -H hmm3/macros -H hmm3/hmmdefs -S test.scp -l '*' -i result.mlf -w ../../gen/wordnet ../../gen/dict models0

HResults -I testref.mlf models0 result.mlf










