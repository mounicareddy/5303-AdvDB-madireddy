from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_restful import reqparse
from flask import jsonify
from flask_cors import CORS, cross_origin

#from pymongo import MongoClient
import pymongo
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId

import datetime

import json
import urllib


import timeit

app = FlaskAPI(__name__)
CORS(app)

client = pymongo.MongoClient('localhost', 27017)
db = client['mounika']
businessdb = db['yelp.business']
review = db['yelp.review']
userdb = db['yelp.user']
tipdb = db['yelp.tip']


parser = reqparse.RequestParser()

"""=================================================================================="""
"""=================================================================================="""
"""=================================================================================="""


@cross_origin() # allow all origins all methods. 
@app.route("/", methods=['GET'])
def index():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return func_list

   
"""=================================================================================="""
@app.route("/find_zips/<args>", methods=['GET'])
def find_zips(args):

    args = myParseArgs(args)
    
    start= int(args['start'])
    
    end = int(args['limit'])
    
    data = []
    zip = []
    
    zip = args['zip'].split(',') 
    
    result = businessdb.find({},{'_id':0}) 
     		
   
    for r in result:
        parts = r['full_address'].split(' ')
        target = parts[-1]
        if target in zip and start < end :  
            data.append(r['business_id'])
            start += 1
			
    return {"count":data} 
   
"""=================================================================================="""
@app.route("/find_city/<args>", methods=['GET'])
def find_city(args):
 
    args = myParseArgs(args)
    
    start = int(args['start'])
    
    end = int(args['limit'])

    data = []
    mycity = args['city'] 
    result = businessdb.find({},{'_id':0})  
    for r in result:
        target = r['city']   
        if target == mycity and start < end : 
            data.append(r['business_id'])
            start += 1 
    return {"data":data}
"""======================================================================================"""

@app.route("/review_count/", methods=['GET'])
def find_averagereview():

    """args = myParseArgs(args)"""
    
    data = []
    result = userdb.aggregate(
	[
		{
			"$group" : 
				{
					"_id" : "$name", "averagereviewcount" : {"$avg":"$review_count"}
				}
		}
	]
)
    


    for r in result:
        data.append(r) 
    return {"data":(data)}
	




"""======================================================================================="""
@app.route("/reviews/<args>", methods=['GET'])
def reviews(args):

    args = myParseArgs(args)
    start= int(args['start'])
    end = int(args['limit'])

    data = []
    
    businessid = args['id']
    result = review.find()
    for r in result:
        parts = r['business_id']

        if  parts == businessid and start < end:
            data.append(r['business_id'])
            start += 1
    return {"count":len(data)}  
	
"""======================================================================================"""
@app.route("/closest/<args>", methods=['GET'])
def closestlocation(args):

    args = myParseArgs(args)
    lat = float(args['lat'])
    lon = float(args['lon'])
	
    
    if 'skip' in args.keys():
        args['skip'] = int(args['skip'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    #.skip(1).limit(1)
    
    if 'skip' in args.keys() and 'limit' in args.keys():
        result = businessdb.find({
   "loc": {
        "$geoWithin": { "$center": [[lon,lat] , .004 ] }
   }  
}).skip(args['skip']).limit(args['limit'])
    elif 'skip' in args.keys():
        result = businessdb.find({
   "loc": {
        "$geoWithin": { "$center": [[lon,lat] , .004 ] }
   }  
}).skip(args['skip'])
    elif 'limit' in args.keys():
        result = businessdb.find({
   "loc": {
        "$geoWithin": { "$center": [[lon,lat] , .004 ] }
   }  
}).limit(args['limit'])
    else:
        result = businessdb.find({
   "loc": {
        "$geoWithin": { "$center": [[lon,lat] , .004 ] }
   }  
}).limit(10)  
    
   
    for r in result:
        data.append(r['business_id'])
    return {"data":data} 
"""======================================================================================"""
@app.route("/stars/<args>", methods=['GET'])
def stars(args):

    args = myParseArgs(args)
    start= int(args['start'])
    end = int(args['limit'])
    
    data = []
    args['num_stars'] = int(args['num_stars'])
    noofstars = args['num_stars']
	
    
    result = review.find()
    for r in result:
        target = r['stars']
        if target == noofstars and start < end: 
            data.append(r['user_id'])
            start += 1
    return {"count":len(data)}
"""========================================================================================"""

@app.route("/elite/<args>", methods=['GET'])
def find_elite(args):

    args = myParseArgs(args)
    start= int(args['start'])
    end = int(args['limit'])
    
    data = [] 
    result = userdb.find()
    for r in result:
        target = r['elite']
        if len(target) != 0 and start < end : 
            data.append(r['user_id'])
            start += 1
    return {"data":data} 
"""=========================================================================================="""
@app.route("/yelping/<args>", methods=['GET'])
def yelpingsince(args):

    args = myParseArgs(args)
    
	
    
    if 'skip' in args.keys():
        args['skip'] = int(args['skip'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    #.skip(1).limit(1)
    
    if 'skip' in args.keys() and 'limit' in args.keys():
        result = userdbdb.find({ "yelping_since" : {"$lte":"2011-11"}}, {"_id":0,"name":1}).skip(args['skip']).limit(args['limit'])
    elif 'skip' in args.keys():
        result = businessdb.find({ "yelping_since" : {"$lte":"2011-11"}}, {"_id":0,"name":1}).skip(args['skip'])
    elif 'limit' in args.keys():
        result = businessdb.find({ "yelping_since" : {"$lte":"2011-11"}}, {"_id":0,"name":1}).limit(args['limit'])
    else:
        result = userdb.find({ "yelping_since" : {"$lte":"2011-11"}}, {"_id":0,"name":1}).limit(10)  
    
   
    for r in result:
        data.append(r['name'])
    return {"data":data} 



"""=========================================================================================="""

@app.route("/review_count/", methods=['GET'])
def averagereview():

    """args = myParseArgs(args)"""
    
    data = []
    result = userdb.aggregate(
	[
		{
			"$group" : 
				{
					"_id" : "$name", "averagereviewcount" : {"$avg":"$review_count"}
				}
		}
	]
)





"""=========================================================================================="""
@app.route("/longelite/<args>", methods=['GET'])
def elite1(args):

    
    args = myParseArgs(args)
    start= int(args['start'])
    end= int(args['limit'])
    
    
    data3 = [] 
    
    
    result = userdb.find()
    
    for r in result: 
        
        data1=len(r['elite'])
        if data1 == 12 and start < end :
		
            data3.append(r['user_id'])
            start += 1
		
        
	
    return {"data":data3} 

"""========================================================================================="""
@app.route("/avg_elite/", methods=['GET'])
def find_averageuserelite():

    
    
    data = []
    result = userdb.aggregate(
	[
		{
			"$group" :  
				{
					"_id" : "$name", "average" : {"$avg":{"$size" : "$elite"}}
				}
		}
	]
)





"""=========================================================================================="""
@app.route("/most_likes/<args>", methods=['GET'])
def find_mostlikes(args):
    args = myParseArgs(args)
    start= int(args['start'])
    end= int(args['limit'])

    data = []
    result = tipdb.find()
    for r in result:
        data.append(r['likes'])
    return {"data":max(data)}

"""======================================================================================"""
@app.route("/user/<args>", methods=['GET'])
def user(args): 

    args = myParseArgs(args)
    
    if 'skip' in args.keys():
        args['skip'] = int(args['skip'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    #.skip(1).limit(1)
    
    if 'skip' in args.keys() and 'limit' in args.keys():
        result = userdb.find({},{'_id':0}).skip(args['skip']).limit(args['limit'])
    elif 'skip' in args.keys():
        result = userdb.find({},{'_id':0}).skip(args['skip'])
    elif 'limit' in args.keys():
        result = userdb.find({},{'_id':0}).limit(args['limit'])
    else:
        result = userdb.find({},{'_id':0}).limit(10)  

    for row in result:
        data.append(row)


    return {"data":data}
    

"""=================================================================================================="""
@app.route("/business/<args>", methods=['GET'])
def business(args):

    args = myParseArgs(args)
    
    data = []
    
    result = businessdb.find({},{'_id':0})
    
    for row in result:
        data.append(row)
    

    return {"count":len(data)}
"""=================================================================================="""
def snap_time(time,snap_val):
    time = int(time)
    m = time % snap_val
    if m < (snap_val // 2):
        time -= m
    else:
        time += (snap_val - m)
        
    if (time + 40) % 100 == 0:
        time += 40
        
    return int(time)

"""=================================================================================="""
def myParseArgs(pairs=None):
    """Parses a url for key value pairs. Not very RESTful.
    Splits on ":"'s first, then "=" signs.
    
    Args:
        pairs: string of key value pairs
        
    Example:
    
        curl -X GET http://cs.mwsu.edu:5000/images/
        
    Returns:
        json object with all images
    """
    
    if not pairs:
        return {}
    
    argsList = pairs.split(":")
    argsDict = {}

    for arg in argsList:
        key,val = arg.split("=")
        argsDict[key]=str(val)
        
    return argsDict
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
