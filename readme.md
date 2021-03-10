# Book Depository Tracker

Python script to track shipments from Bookdepository.com, sent via Post.nl service.

Given a csv with: Description | TrackID, the script will make a POST request to post.nl website, then the request content will be parsed with Beautifoul Soup in order to retrieve the desired shipment status information.

Finally, an output .txt file will be created, listing each order and it's current status.
