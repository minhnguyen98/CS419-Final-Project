from model.descriptor import RGBHistogram
import argparse
import glob
import os
import cv2
 
################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Command line argument
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", required = True,
	help = "Path to dataset.")
parser.add_argument("-i", "--features", required = True,
	help = "Path to features file.")
args = vars(parser.parse_args())

descriptor = RGBHistogram((8, 12, 3))

output = open(args["features"], "w")
 
for filename in glob.glob(args["dataset"] + "/*.jpg"):
	img_name = filename[filename.rfind('\\') + 1:]
	image = cv2.imread(filename)

	features = descriptor.describe(image)

	features = [str(f) for f in features]
	output.write("%s,%s\n" % (img_name, ",".join(features)))
 
output.close()