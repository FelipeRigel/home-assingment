import csv

#I may move this to a new file for constants paths

cleanFile = "data/movies.csv"

def loadImdbFile():
    imdbPath = "data/imdb.csv"
    with open(imdbPath, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def loadRating():
    with open(cleanFile, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def createExcerciseFile(data):
    with open(cleanFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def createFile():
    #If this is not working check your working DIR
    imdbFile = loadImdbFile()
    headers = imdbFile.pop(0)
    print("Headers check: " + headers[5] + " " + headers[9] + " " + headers[11])
    cleanMovies = []
    for movie in imdbFile:
        #print(movie[5] + " " + movie[9] + " " + movie[11])
        cleanMovies.append([movie[0],float(movie[9]),movie[5],1 if int(movie[11])>2009 else 0])
    #print(cleanMovies)
    createExcerciseFile(cleanMovies)
