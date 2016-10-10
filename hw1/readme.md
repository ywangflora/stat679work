# hw1
## exercise1
- I got the data from [coursedata](https://github.com/UWMadison-computingtools/coursedata/tree/master/hw1-snaqTimeTests) in the github. In hw1 directory, there will be two directories called log and out. In log directory, I change all file names timetesty_snaq.log to timetest0y_snaq.log where "y" is a digit between 1 and 9 by using a for loop in the shell. Similarly, I change timetesty_snaq.out to timetest0y_snaq.out in out directory.

## exercise2
- The aim of doing exercise2 is to produce a table in csv format, with 1 row per analysis and 3 columns. The columns' name are anlysis, hmax and CPUtime. All the data is collected in both the log and out dictionary. This is what the script called 'summarizeSNaQres2.sh' does. I use the grep method to get the rootname, hmax and CPUtime from both the log and out file. Then a for loop is used to extract all the corresponding data. Finally, I save all the data to a new file called summarizeSNaQres.csv.

## exercise3
- The aim of exercise3 is to grab useful information through both the log and out file and then display it in a csv file. This is what the script called 'summarySNaQres2.sh' does. I use the 'grep' and 'sed' method to capture appointed information. The output file is called summarizeSNaQres2.csv.