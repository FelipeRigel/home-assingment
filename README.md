# home-assingment
softwaremind code assigment
  ______   ______     _                  _       
 |  ____| |___  /    | |                (_)      
 | |__       / / __ _| |_ __ _ _ __ __ _ _ _ __  
 |  __|     / / / _` | __/ _` | '__/ _` | | '_ \ 
 | |       / /_| (_| | || (_| | | | (_| | | | | |
 |_|      /_____\__,_|\__\__,_|_|  \__,_|_|_| |_|


 1.- I got a mock file for the CSV from a IMDb example https://github.com/sharkdp/imdb-ratings/blob/master/ratings.csv?plain=1
 2.- I cleaned to match the format, I do not have info on what certified fresh was, so I took movies/series from 2010 or newer (file is from 2014)
 3.- Created some endpoints I used flask since the instruction was to create a BACKEND
 4.- Main file make a couple of things before instialize the server
    4.1- first createFile creates movies.csv simulating the example mention for the format rating, title and certified fresh
    4.2- inits a DB example mention to use postgres but nothing postgres specific is needed in the task, so I creates a minial
         DB using sqlite, easily translate for postgres, postgres does have a couple of better fuctions like BOOL as native
         sqlite use numbers, views in postgres can be dynamic or saved in memory, in this case we are not updating so we can keep
         a not dynamic view and only updating on trigger update of the main table
    4.3- For recomendations this approch is not optimal, if any there is extension for postgres to make optimal structures for KNN similar algorithms
         the most vanilla thing I can implement is to make some index to rapid query colums used for calculations, but only thing I can use
         given the example is title and rating
 5.- Following Problem 1 excecute the main file should start a server on http://127.0.0.1:5000/
    5.1 - http://127.0.0.1:5000/dbratings should show the DB example of all the movies in our fake postgres (sqlite).
    5.2 - http://127.0.0.1:5000/top is showing the top 10 of those movies that are mark as certified fresh
    5.3 - the other two endpoinds is only a default to ccheck server is running and /csvratings only to check the file is created
          http://127.0.0.1:5000/csvratings is the equivalent for movie_list
 6.- Depencies to run are only flask and csv
 7.- if having problems executing the project verify you are executing for the main folder where main.py is localted. I am not using OS for 
     relative paths to keep it as minimal as posible. 
