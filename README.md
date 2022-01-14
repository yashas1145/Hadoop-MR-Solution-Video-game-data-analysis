# Hadoop-MR-Solution-Video-game-data-analysis

****************************************************************************************************

Hadoop MR Solution to classify a handle based on total number of sales.
Dataset: Video games data set containing a number of parameters.

1) Format the datanode: 
   Command: hadoop namenode -format

2) Start all the services: 
   Command: start-dfs.sh; start-yarn.sh OR start-all.sh
   For GUI, open localhost:9870 in browser
   
3) Create a directory in hdfs for handling input: 
   Command: hadoop fs -mkdir /myInput

4) Copy the dataset into the input directory: 
   Command: hadoop fs -put "path-to-dataSet" /myInput

5) Exectue the hadoop streaming jar:
   "hs" is aliased to run a function having the command "hadoop jar hadoop-streaming-3.3.1.jar -mapper "mapper.py" -reducer "reducer.py" -file $1 -file $2 -input $3 -output $4"
   Command: hs mapper.py reducer.py /myInput /myOutput
   
6) Fetch the reduced output to a file: 
   Command: hadoop fs -get /myOutput/part-00000 "path-to-result"

7) Plotting the graph using matplotlib library:
   "py" is aliased to execute python shell
   Command: py resParse.py
   
****************************************************************************************************
   
Files and their usage:
   
1) mapper.py: Code to execute mapper function
2) reducer.py: Code to execute reducer function
3) resParse.py: Code to plot graph using reduced output
4) intRes: Intermediate output from mapper
5) res: Final output from reducer
6) Solution graph.png: Plot of analysis
