#!/bin/bash
# the steps are followed as per link
# http://sail.usc.edu/old/courses/EE619/digit-recognition-tutorial.txt

# @author: Subhasis Maity
root=$PWD
grammerfile="grammar" # the file name is written explicitly inside the cmd ->HParse

echo "-----------------INFO--------------------"
node ./scripts/create_grammer.js # creates grammer, wlist, lexicon
node ./scripts/create_mlf.js # creates MASTER LABEL FILE

echo "-----------------INFO--------------------"
printf "Step 1 => Create HTK wordnet lattice\n"
printf "\$_>: HParse grammer wordnet\n"
printf "grammerfile -> $grammerfile\n\n"

HParse grammer wordnet # Convert this grammar to an HTK wordnet lattice using the HParse tool

# create lexicon, wlist ***with proper order***

echo "-----------------INFO--------------------"
printf "Step 2 => Create HTK wordnet lattice\n"
printf "\$_>: HDMan -m -w wlist -n models1 -l dlog dict lexicon\n"

HDMan -m -w wlist -n models1 -l dlog dict lexicon