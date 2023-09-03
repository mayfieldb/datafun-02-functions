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
    logger.info(f"CALLING get_converToAcres({square_mileage})")

    try: 
        acres_in_mile = square_mileage / ACRE
        logger.info(f"The circle area is {acres_in_mile}")
        return acres_in_mile
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    

converToAcres(square_mileage)

if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")

