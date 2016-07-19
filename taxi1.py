
"""count the frequency of particular vendor type."""
from mrjob.job import MRJob
import re
WORD_RE = re.compile(r"[\w']+")
i=[]
tot=[]
yyy=[]
def functi(item):
        nos=0
        total=0.0
        for x in item:
                
                nos+=1
        return nos


class MRFreqCount(MRJob):

    def mapper(self, _, line):
       	values=line.split(",")
	yield((values[10],values[11],values[2]),1)


    def combiner(self, taxi, count):

	yield(taxi,sum(count))
                  	
	if __name__ == '__main__':
     MRFreqCount.run()

