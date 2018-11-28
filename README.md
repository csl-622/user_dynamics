# user_dynamics
This project is about the characterisation of user contributions on a Wikipedia page.

1.The first part involves getting the data of the user contributions by reading the xml dump file and getting the 
  username/ip address(if anonymous) and then getting the edits he/she has done in that particular page. This is 
  using the users_list() function in new_file.py .
  
2.The second part involves training a model data using nltk and gensim models to create topics from reading the 
  user contributions. This is done using the file train_model.py .
  
3.The third part involves getting the topics from the model just trained by reading the edits and feeding them to
  model just trained. This is done in the second part of the code in new_file.py but the function for topic creation
  i.e. getTopicForQuery() is defined in testing.py .
  
4.The new_file.py uses the xml.eTree library to parse the xml file and then storing the username/ip address and their
  edits in a dictionary as key value pair. Using the dictionary the edits are traversed and then stored in separate files
  with the same username/ip .txt naming convention stored inside the folder with the xml file name. Then the files are read
  and the getTopicForQuery() function is called on the edits to get the topics and they are stored in a 2D matrix.

Edit:-

5.A new code driver.py is created to model the topics that were calculated and stored in the 2D matrix. The similarity threshold is hardcoded for 70%. The word embedding is done using a file named "lexvec.commoncrawl.300d.W+C.pos.vectors" but it is not uploaded here(it's more than 5 GB). To download the file, open the link given below and then extract it and paste the content in the working directory...

https://www.dropbox.com/s/zkiajh6fj0hm0m7/lexvec.commoncrawl.300d.W%2BC.pos.vectors.gz?dl=1
  
How to run the code:

(if you want to train the model from scratch, not needed here as the trained model files are included so skip the first command)
$ python3 train_lda.py\
$ python3 new_file.py xml_file_name(without the .xml extension)

Note:-For this code to work, please remove the attributes in mediawiki tag in the beginning of the xml file, then 
  run the code.
  
-----------------------------------------------------------------

Note:-Design Doc will be ready soon.
