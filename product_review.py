#1. Product Review Analysis
#Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. 
#The function should return the count of positive and negative words for each review.

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
#Dylan Katina provided the following feedback on your response:
#Strong star, here are some hints to help with the next 2 tasks

#1.2) Will look pretty similar to 1, but here we are wanting to use .count() to count each positive and negative word in our review

#1.3) This will center on slicing, and making sure the slice doesnt happen in the middle of the word, so you may want to push your index over until it points to a space 
#(if you cant get the "not in the middle of the word part" totally fine you'll only lose 5 points).



reviews =  ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]


words=["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"
    "bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def review_highlight(reviews):   
    for review in reviews:
        for word in words:
            review = review.replace(word, word.upper())
            review = review.replace(word.title(),word.upper())
               
        print(review)    
review_highlight(reviews)

def x (reviews):
    
    word_counts = {word: reviews.count(word) for word in words}
    for word, count in word_counts.items():#The items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
        print(f"Occurrences of '{word}': {count}")
x(reviews)
                   