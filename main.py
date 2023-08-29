from ai_analysis import Analyze

# Syntax : 
# query = Analyze (' Question you want to ask ', kwarg : Doc = 'Path of the Directory from which you want to ask the question')
# To get a response :
# query.respond

query = Analyze('Summarize the document into 5 lines exactly', Doc= "Guide")
query.respond()
