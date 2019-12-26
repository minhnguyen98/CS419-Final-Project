from model.descriptor import RGBHistogram
from model.searcher import Searcher
import argparse
import cv2

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Command line argument
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--features", required = True,
	help = "Path to features file")
parser.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
parser.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(parser.parse_args())

descriptor = RGBHistogram((8, 12, 3))

query = cv2.imread(args["query"])
features = descriptor.describe(query)

searcher = Searcher(args["features"])
results = searcher.search(features)

cv2.imshow("Query", query)

for (score, resultID) in results:
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)