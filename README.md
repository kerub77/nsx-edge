
Python script to deploy NSX-T edge
1. Complete the variables
2. Run the script like below:

# python edge.py
A file called out.json will be created

Deploy the edge:
# curl -k -X POST -u 'user:password' -H "Content-Type: application/json" -d @out.json https://NSX-Manager-VIP/api/v1/transport-nodes 
