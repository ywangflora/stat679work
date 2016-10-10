echo analysis,h,CPUtime,Nruns,Nfails,frel,fabs,xabs,xrel,seed,under3460,under3450,under3440 > summarizeSNaQres2.csv
for filename in ./log/*.log
do
  #analysis=`echo $filename | cut -f 2 -d'.' | cut -f 3 -d'/'`
  analysis=`basename -s ".log" $filename`    # get the name of file with basename
  h=`grep 'hmax\s=\s\d' $filename | grep -o '\d'`  # get hmax data
  c=`grep 'Elapsed\stime' ./out/$analysis\.out | grep -oE "\d+\.\d+"`  # get the CPUtime
  Nruns=`grep 'runs' $filename | grep -oE 'BEGIN:\s\d+' | cut -f2 -d':' | grep -oE '\d+'` # get the run numbers
  Nfails=`grep 'max number of failed proposals' $filename | cut -f1 -d',' | grep -oE '\d+'`  # get the max number of failed proposals
  frel=`grep 'ftolRel' $filename | cut -f1 -d',' | cut -f2 -d':' | gsed 's/[=]/\t/' | cut -f2` # get the ftoRel number
  fabs=`grep 'ftolAbs' $filename | cut -f2 -d',' | gsed 's/[=]/\t/' | cut -f2` # get ftolAbs data
  xabs=`grep 'xtolAbs' $filename | cut -f1 -d',' | gsed 's/[=]/\t/' | cut -f2` # get xtolAbs data
  xrel=`grep 'xtolRel' $filename | cut -f2 -d',' | gsed 's/[=]/\t/' | cut -f2 | grep -oE '\d\.\d+'` # get xtolRel number
  seed=`grep 'main seed' $filename | cut -f3 -d" "` # get main seed number
  #loglik=`grep 'loglik of best' $filename | cut -f2 -d'=' | grep -oE '\d+.\d+$' | cut -f1 -d'.'`
  loglik=`grep 'loglik of best' $filename |cut -f10 -d' '| cut -f1 -d'.'`   # the values of loglik
  i=0
  k=0
  m=0
  for number in $loglik     # use a for loop to count numbers which are under 3460, 3450 and 3440
     do
       if [ $number -lt 3460 ]
       then
         i=$((i+1))
       fi
       if [ $number -lt 3450 ]
       then
         k=$((k+1))
       fi
       if [ $number -lt 3440 ]
       then
         m=$((m+1))
       fi
  done
  echo $analysis,$h,$c,$Nruns,$Nfails,$frel,$fabs,$xabs,$xrel,$seed,$i,$k,$m >> summarizeSNaQres2.csv
done
