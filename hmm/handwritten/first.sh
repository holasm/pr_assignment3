digits=(a ai bA chA dA lA tA)

# HParse ...

# rm -rf io/gen/wordnet
# mkdir -p io/gen/wordnet
# for ((i=0; i<${#digits[*]}; i++));
# do
#   # echo ${digits[i]}
#   HParse io/created/grammer/${digits[i]} io/gen/wordnet/${digits[i]}
# done

HParse io/created/grammer io/gen/wordnet

# HDMan ...

# mkdir -p io/gen/dlog
# mkdir -p io/gen/dict
# mkdir -p io/gen/models
# for ((i=0; i<${#digits[*]}; i++));
# do
#   HDMan -m -w io/created/wlist/${digits[i]} -n io/gen/models/${digits[i]} -l io/gen/dlog/${digits[i]} io/gen/dict/${digits[i]} io/created/lexicon/${digits[i]}
# done

HDMan -m -w io/created/wlist -n io/gen/models0 -l io/gen/dlog io/gen/dict io/created/lexicon

# HInit ... not HCompV ...
for ((i=0; i<${#digits[*]}; i++));
do
  mkdir -p io/hmms/${digits[i]}
  mkdir -p io/hmms/${digits[i]}/hmm0
  HInit -S io/created/scp/train/${digits[i]}.scp -M io/hmms/${digits[i]}/hmm0 -I io/created/mlf/train/${digits[i]}.mlf io/hmms/proto
done

# Hinit -S io/created/scp/train/a.scp -M io/hmms/a/hmm0 io/hmms/proto
# HInit -S io/created/scp/train/a.scp -M io/hmms/a/hmm0 -I io/created/mlf/train/a.mlf io/hmms/proto
# HInit -S io/created/scp/train/${digits[i]}.scp -M io/hmms/${digits[i]}/hmm0 -I io/created/mlf/train/${digits[i]}.mlf io/hmms/proto



