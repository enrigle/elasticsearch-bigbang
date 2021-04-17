import requests
import json
import re
from elasticsearch import Elasticsearch

r = requests.get(
    "http://api.tvmaze.com/singlesearch/shows?q=big-bang-theory&embed=episodes"
)

jd = json.loads(r.content)
print(jd["_embedded"]["episodes"][0])

# The list ldocs now contains 200 documents in the form of dictionary objects
ldocs = []
for jo in jd["_embedded"]["episodes"][0:200]:
    d = {}
    d["id"] = jo["id"]
    d["season"] = jo["season"]
    d["episode"] = jo["number"]
    d["name"] = jo["name"]
    d["summary"] = re.sub("<[^<]+?>", "", jo["summary"])
    ldocs.append(d)

# connect to elastic
es = Elasticsearch([{"host": "localhost", "port": 9200}])

# iterate through documents indexing them
for doc in ldocs:
    es.index(index="tvshows", doc_type="bigbang", id=doc["id"], body=json.dumps(doc))

# python elasticsearch get by id
print("###########")
print(es.get(index="tvshows", doc_type="bigbang", id=2915))
print("###########")

# term search
print("term search")

print(
    es.search(
        index="tvshows",
        doc_type="bigbang",
        body={"query": {"match": {"summary": "rivalry"}}},
    )
)

# fuzzy search
# After you run this code, you will notice 2 results, one document in which rival was found,
# and another document in which rivalry was matched.
print(
    es.search(
        index="tvshows",
        doc_type="bigbang",
        body={"query": {"fuzzy": {"summary": "rival"}}},
    )
)


# delete index
es.indices.delete(index="bigbang", ignore=[400, 404])
