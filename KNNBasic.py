from dataMovies import moviesDataset, movieLabels

def euclidianDistance(movieOne, movieTwo):
    diff = 0
    for i in range(len(movieOne)):
        diff += (movieOne[i] - movieTwo[i]) ** 2
    finalVal = diff ** 0.5
    return finalVal

def normalizationStat(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for value in lst:
    normalized_num = (value - minimum) / (maximum - minimum)
    normalized.append(normalized_num)
  return normalized


def classify(unknown, dataSet, k):
    distance = []
    for title in dataSet:
        movie = dataSet[title]
        distanceToPoint = euclidianDistance(movie, unknown)
        distance.append([distanceToPoint, title])
    distance.sort()
    kNearestNeighbors = distance[0:k]
    return kNearestNeighbors


print("KNearestNeighbors of selected movie", classify([0.0163726237623701, 0.2354948805460751, 0.9101123595505618], moviesDataset, 5))