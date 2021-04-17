# elasticsearch-bigbang

# Download Elasticsearch
- Go to https://www.elastic.co/es/downloads/elasticsearch
- For macos: download MACOS shaasc file
- Unzip the elasticserch folder 
- Change to that directory
- Run `bin/elasticsearch` on the terminal
- Test that it is workking by going to the URL: http://localhost:9200/
- The following message should appear:
    `{
        "name": "JORGE.local",
        "cluster_name": "elasticsearch",
        "cluster_uuid": "jhasdjkasdjlkasa",
        "version": {
        "number": "7.12.0",
        "build_flavor": "default",
        "build_type": "tar",
        "build_hash": "jlkdsjalsdaksdajkdsal",
        "build_date": "2021-03-18",
        "build_snapshot": false,
        "lucene_version": "8.8.0",
        "minimum_wire_compatibility_version": "6.8.0",
        "minimum_index_compatibility_version": "6.0.0-beta1"
        },
        "tagline": "You Know, for Search"
    }`


# Install the following libraries
requests
json
re
elasticsearch

For instance, to install elasticsearch run `python -m pip install elasticsearch`

# Execute the app.py
go to the terminal and run `python app.py`
