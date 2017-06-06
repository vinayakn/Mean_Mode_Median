#######################################
#AUTHOR: VINAYAK.V.NAVALE
#DATE:06/06/2017
#######################################


class Stats(object):
	try :
		def __init__(self,data):
			self.data=data
			if self.data is not list:
				print "provide Array as input"
			else :  pass

		def mean(self):
			
			try:
				result=[]
				mean_data=float(sum(self.data)/len(self.data))
				
				result.append("===============================")
				result.append("Mean of Data : "+str(mean_data))
				result.append("===============================")
				return ('\n').join(result)
			except:	"Not Array of Numbers"+"\n"
				

		def median(self):
			try:
				result=[]
	    			SortData = sorted(self.data)
				DataLen = len(self.data)
				index = (DataLen - 1) // 2
				if (DataLen % 2):
				        median_data=SortData[index]
                                        result.append("===================================")
                                        result.append("Median of Data : "+str(median_data))
                                        result.append("===================================")
#                                       return  result
                                        return ('\n').join(result)

				else:
					median_data=(SortData[index] + SortData[index + 1])/2.0
	                                result.append("===================================")
                	                result.append("Median of Data : "+ str(median_data))
					result.append("===================================")
#					return  result
					return ('\n').join(result)

			except: "Not Array of Numbers"+"\n"
		def mode(self):
			try:
				result=[]
				freq_dict = {}
				for i in (self.data):   
				        count = self.data.count(i)
			        	if i not in freq_dict.keys():
		       				freq_dict[i] = count
				max_count = 0 
				for key in freq_dict: 
				        if freq_dict[key] >= max_count:
            					max_count = freq_dict[key]
				freq_keys = [] 
				for freq_key, freq_value in freq_dict.items():
					        if freq_dict[freq_key] == max_count:
							            freq_keys.append(freq_key)
				if max_count == 1 and len(freq_dict) != 1: 
				        return 'There is no mode for this data set. All values occur only once.'
				else: 
     					result.append("=========================================================")
				        freq_keys = sorted(freq_keys)
#				        return freq_keys, max_count
					result.append("Mode of Data : "+ str(freq_keys)+"  Freq: "+str(max_count))
					result.append("=========================================================")
					return ('\n').join(result)	
			except:	"Not Array "+"\n"

	
	except Exception :
		print "error"

#test
#d=Stats([1,2,3,3,2,2,2,3,3])
#print d.mean()
#print d.median()
#print d.mode()
