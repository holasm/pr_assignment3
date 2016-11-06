digits=(a ai bA chA dA lA tA)
MAX_ITER=10

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HInit ... not HCompV ...

for ((i=0; i<${#digits[*]}; i++));
do
  END=$MAX_ITER
  start=0
  for ((j=1;j<=END;j++)); do
    echo "$j th iteration for ${digits[i]}"
      rm -rf "io/hmms/${digits[i]}/hmm$j"
      mkdir -p "io/hmms/${digits[i]}/hmm$j"

      echo "$ HRest ..."
      HRest  -L io/created/mlf/train/${digits[i]}.mlf -S io/created/scp/train/${digits[i]}.scp -M io/hmms/${digits[i]}/hmm$j io/hmms/${digits[i]}/hmm$start/proto
      start=$j
  done
  echo "---------------"
done
#=====TESTS=====
# HERest  -I all.mlf -S all.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 models0
# HRest  -L io/created/mlf/train/a.mlf -S io/created/scp/train/a.scp -M io/hmms/a/hmm1 io/hmms/a/hmm0/proto
#==============
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

echo "$ node create_hmmdefs.js "
node create_hmmdefs.js

# HVite ...

# 
echo "$ HVite ..."
HVite -H io/hmms/hmmdefs -S io/created/scp/test.scp -l '*' -i io/hmms/result.mlf -w io/gen/wordnet io/gen/dict io/hmms/hmmlist

#=====TESTS=====
# HVite -H io/hmms/hmmdefs -S io/created/scp/test.scp -l '*' -i result.mlf -w io/gen/wordnet io/gen/dict io/hmms/hmmlist
#==============
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 
HHEd -H io/hmms/hmmdefs -M io/hmms/hmm_ incmix.4.hed io/hmms/hmmlist

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HResults ...

echo "$ HResults ..."
HResults -I io/created/mlf/test.mlf io/hmms/hmmlist io/hmms/result.mlf








# ###############
# 
# ###############
# ff=""
# for ((i=0; i<${#digits[*]}; i++));
# do
#   ff="$ff $(cat io/hmms/${digits[i]}/hmm$MAX_ITER/proto) \n"
#   # ff="$ff cat"
# done
# echo $ff > io/hmms/hmmdefs

