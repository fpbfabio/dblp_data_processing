#dblp_data_processing

A program that transforms the dblp xml file available on the web into an xml file compatible with Apache Solr. It is useful mainly to data science researchers

##Requirements

* python (version 3 or higher) command line tool set up

##How to use

```
python program.py <path-to-dblp-xml-file> <path-destination-file>
```
or
```
python3 program.py <path-to-dblp-xml-file> <path-destination-file>
```

###Detailed steps
1. Download dblp data set available on the official website
2. Clone this repository to a folder in your computer
3. Run the python file program.py, which is inside the folder named python, passing two parameters the path to the dblp xml file and the path to the destination xml file (as in the above example code)
4. Set up a core in Solr with the schema.xml file present in this repository
5. Post the xml files to that core using the post.jar tool
6. Start making searches!
