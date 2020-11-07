# Enter you module contents here
''' Module to calculate area and hyp from /\ '''

__version__ = "1"
__author__ = "Luciano"

def hypothenuse (L1,L2):
	'''Returns rect triangle hyp'''
	return (L1**2+L2**2)**0.5
def area (L1,L2):
	'''Returns rect triangle area'''
	return(L1*L2/2)

