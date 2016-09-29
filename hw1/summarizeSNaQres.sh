echo analysis, h, CPUtime > summarizeSNaQres.csv   # add the name of the columns

for filename in ./log/*.log                        # for loop to search log file in certain directory
    do
    analysis=`echo $filename | cut -f 2 -d'.' | cut -f 3 -d'/'`   # get the name of the file
    h=`grep 'hmax\s=\s\d' $filename | grep -o '\d'`               # get hmax
    o=`echo ./out/$analysis\.out`                                 # get the relative path to the out file
    c=`grep 'Elapsed\stime' $o | grep -oE "\d+\.\d+"`             # get CPUtime
    echo $analysis, $h, $c >> summarizeSNaQres.csv                # display in a csv file
    done
