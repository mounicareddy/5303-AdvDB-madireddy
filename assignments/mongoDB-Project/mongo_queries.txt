Mongodb queries by:
Madireddy Mounika M20227730
Agumamidi Avinash M20225303
-------------------------------------------------------------------------------------------------------------------------

1)Find all restaurants with zip code X or Y -Using 89117 and 89122
$regex:
Provides regular expression capabilities for pattern matching strings in queries.

db.yelp.business.find({$or: [{"full_address":{$regex: '89117'}},{"full_address":{$regex: '89122'}}]}).count()



2)Find all restaurants in city X
db.yelp.business.find({"full_address":{$regex: 'Las Vegas'}}).count()

3)Find the restaurants within 5 miles of lat , lon
db.yelp.business.find({
   loc: {
        $geoWithin: { $center: [ [ -80.839186,35.226504] , .004 ] } 
   }
})

4)Find all the reviews for restaurant X

db.yelp.review.find({"business_id":"mVHrayjG3uZ_RLHkLj-AMg"}).count() 

5)Find all the reviews for restaurant X that are 5 stars.

db.yelp.review.find({"business_id":"mVHrayjG3uZ_RLHkLj-AMg","stars":5}).count() 

6)Find all the users that have been 'yelping' for over 5 years.

db.yelp.user.aggregate(
   [
     {
       $project:
          {
            year: { $substr: [ "$yelping_since", 2, 2 ] }
          }
      }
   ]
)

7)Find the business that has the tip with the most likes?

db.yelp.tip.find({},{business_id :1,likes:1}).sort({likes:-1}).limit(1)

{likes -1}for max
{likes -1} for min

8)Find the average review_count for users

db.yelp.user.aggregate(
   [
     {
       $group:
         {
           _id: "$name",
           avgreviewcount: { $avg: "$review_count" }
         }
     }
   ]
)



9)Find all the users that are considered elite.

db.yelp.user.find(
   [
     {
       $project:
          {
            _id:"$name",
            year: { " $elite "}
          }
      }
   ]
)


10)Find the longest elite user.

db.yelp.user.aggregate([{$group : {_id : "$name", longest : {$max :{$size : "$elite"}}}}])

11)Of elite users, whats the average number of years someone is elite.

db.yelp.user.aggregate([{$group : {_id : "$name", average : {$avg:{$size : "$elite"}}}}])


Difficult:

2)Find the busiest checkin times for all businesses in the 75205 & 75225 zip codes.


db.yelp.business.find({$or: [{"full_address":{$regex: '75205'}},{"full_address":{$regex: '75225'}},{_id :"$name"}]}).count()
output:
0

so the is no business with55205 zip codes with 7





5)Find all restaurants with over a 3.5 star rating average  rating?

In mongodb query results can be stored in a variable and the variable can be used for querying again.

var a =db.yelp.business.aggregate([{$group : {_id : "$name", average : {$avg:"$stars"}}}])
a.forEach(function(d) {print(d.average);})
