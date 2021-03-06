"""
Author: Chris Dare
Version: 1.0
"""

########################################################
#                      CLASSES                         #
########################################################

class OVALResult:
    """ Very simple class which simply allows us to gather
        the information of our driver and put it together
        in a neat format """

    def __init__(self, title, outputs):
        self.title = title
        self.descriptions = []
        self.passed = True

        for output in outputs:
            # unpack each tuple from _execute_tests
            descriptionList, status = output
            self.passed &= status
	    # a single result may have multiple lines
	    for description in descriptionList:
            	self.descriptions.append(description)


    def __repr__(self):
        return self.title + ": " + str(self.passed) 


########################################################
#                      TESTING                         #
########################################################

# For testing purposes only
if __name__ == "__main__":
    
    from oval_request import OVALRequest
    from oval_parser import OVALParser, XMLElement
    from oval_driver import OVALDriver
    import sys
    
    if len(sys.argv) < 2:
        print("\n\tUsage: python oval_driver.py [file]\n")
        sys.exit()

    filename = sys.argv[1]

    parser = OVALParser()
    parser.parse(filename)
    print(parser)

    request = OVALRequest(parser)
    request.initialize()
    print("request:", request)

    driver = OVALDriver(request)
    print(driver.execute_tests())

    result = OVALResult(driver.request.title, driver.execute_tests())
    print(result)
