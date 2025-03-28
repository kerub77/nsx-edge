**Python script to deploy NSX-T edge**

1.  Complete the variables into the file variables.txt.
2.  Run the script like below:

    ```bash
    # python edge.py
    ```

    A file called `out.json` will be created.

Deploy the edge:

```bash
# curl -k -X POST -u 'user:password' -H "Content-Type: application/json" -d @out.json https://NSX-Manager-VIP/api/v1/transport-nodes
