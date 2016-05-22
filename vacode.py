# curl "https://api.havenondemand.com/1/api/sync/querytextindex/v1?text=carjack&absolute_max_results=10&highlight=terms&ignore_operators=false&indexes=vacodeindex&print=all&promotion=false&total_results=true&apikey=a5582336-3213-4ecf-919e-56f90ea2405b"

# curl -X POST --form "text=carjack" --form "absolute_max_results=10" --form "highlight=terms" --form "ignore_operators=false" --form "indexes=vacodeindex" --form "print=all" --form "promotion=false" --form "total_results=true" --form "apikey=a5582336-3213-4ecf-919e-56f90ea2405b" https://api.havenondemand.com/1/api/sync/querytextindex/v1


from havenondemand.hodclient import *

# hodClient = HODClient("a5582336-3213-4ecf-919e-56f90ea2405b", "v1")

# # callback function
# def requestCompleted(response,error, **kwargs):
    # resp = ""
    # if error is not None:
        # resp += "Error code: %d \nReason: %s \nDetails: %s\n" % (err.error,err.reason, err.detail)
    # elif response is not None:
        # entities = response["entities"]
        # for entity in entities:
            # if entity["type"] == "companies_eng":
                # resp += "Company name: " + entity["normalized_text"] + "\n"
            # elif entity["type"] == "places_eng":
                # resp += "Place name: " + entity["normalized_text"] + "\n"
            # else:
                # resp += "People name: " + entity["normalized_text"] + "\n"
    # print (resp)

# params = dict()
# params["url"] = "http://www.cnn.com"
# params["unique_entities"] = "true"
# params["entity_type"] = ["people_eng","places_eng","companies_eng"]

# hodClient.get_request(params, HODApps.ENTITY_EXTRACTION, False, requestCompleted)


##########
import requests
url="https://api.havenondemand.com/1/api/sync/querytextindex/v1"
apikey="a5582336-3213-4ecf-919e-56f90ea2405b"

def postrequests(function,data={},files={}):
               data["apikey"]=apikey
               callurl=url.format(function)
               r=requests.post(callurl,data=data,files=files)
               return r.json()

def formulateRequest(iSearchState, iSearchTerm):
	# curl -X POST --form "text=carjack" --form "absolute_max_results=10" --form "highlight=terms" --form "ignore_operators=false" --form "indexes=vacodeindex" --form "print=all" --form "promotion=false" --form "total_results=true" --form "apikey=a5582336-3213-4ecf-919e-56f90ea2405b" https://api.havenondemand.com/1/api/sync/querytextindex/v1
	
	params = dict()
	params["text"] = iSearchTerm
	print("------------------------------------------------------------")
	print ("Searching for:",iSearchTerm,"in state (US)",iSearchState,sep=" ")
	print("------------------------------------------------------------")
		
	params["absolute_max_results"] = 10
	params["highlight"] = "terms"
	params["ignore_operators"] = "false"
	params["indexes"] = [iSearchState.lower()+"codeindex"]
	params["print"] = "all"
	params["promotion"] = "false"
	params["total_results"] = "true"
	
	oResults=postrequests('querytextindex',params)
	
	for document in oResults["documents"]:
		print("------------------------------------------------------------")
		print ("From collection:", document["collection"])
		print ("Title:", document["title"].encode("utf-8"))
		print("Refer:", document["reference"])
		print("Detailed information (read carefully please - Think Twice!):", document["content"].encode("utf-8"))
	#return oResults
	print("------------------------------------------------------------")
	print("Total number of matching codes found:", oResults["totalhits"])
	print("JAMJustice - Think Twice!")
	print("------------------------------------------------------------")

wantToContinue="yes"

while wantToContinue=="yes":
	print("------------------------------------------------------------")
	print("---------------  INPUT--------------------------------------")
	print("------------------------------------------------------------")
	searchState = input('Which STATE of US are you in? --> ')	
	searchTerm = input('What are you planning to COMMIT? Think Twice! --> ')
	print("------------------------------------------------------------")
	results=formulateRequest(searchState, searchTerm)	
	wantToContinue = input('Want to continue searching (yes/no)? -->')
	if (wantToContinue is None):
		wantToContinue = "yes"


			  		  