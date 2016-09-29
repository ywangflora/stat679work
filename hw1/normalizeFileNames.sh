for number in {1..9}                                        # start in the log dictionary
do
mv timetest$number\_snaq.log timetest0$number\_snaq.log     # add 0 to log file names
done

cd ..
cd out/

for i in {1..9}; do mv timetest$i\_snaq.out timetest0$i\_snaq.out; done    # add 0 to out file names
