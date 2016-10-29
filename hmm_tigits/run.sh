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

# HLEd -l '*' -d dict -i io/models/models0.mlf io/created/mkphones0.led io/created/mlf/man.mlf
# HLEd -l '*' -d dict -i io/models/models1.mlf io/created/mkphones0.led io/created/mlf/woman.mlf

echo "-----------------INFO--------------------"
printf "Step 4 => Expanding the word transcriptions into model transcriptions\n"
printf "\$_>: HDMan -m -w wlist -n models1 -l dlog dict lexicon\n\n"

# HCopy -T 1 -C io/created/config -S io/created/scp/man.scp
# HCopy -T 1 -C io/created/config -S io/created/scp/woman.scp













