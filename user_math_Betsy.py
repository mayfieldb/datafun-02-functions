""
#Betsy_Mayfield
#August_31 
#custom_script
""

#Find the acreage of the Mark Twain National Forest, the Missouri home of Bigfoot
import math

from util_logger import setup_logger
logger, logname = setup_logger(__name__)

ACRE = .0015625
square_mileage = float(input ("How many square miles is the MTNF?"))

def converToAcres(square_mileage):
    acres_in_mile = square_mileage / ACRE
    print ("Your acreage is %.2f" % acres_in_mile, "acres")

converToAcres(square_mileage)

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")