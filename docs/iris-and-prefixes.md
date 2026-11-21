# IRIs and Prefixes

Each RDF document has a permanent `w3id.org` identifier which supports content negotiation:

```sh
# Fetching the ttl verison of the ontology
curl -L -H "Accept: text/turtle" https://w3id.org/taro/ontology

# Fetching the json-ld version of the rider-waite dataset
curl -L -H "Accept: application/ld+json" https://w3id.org/taro/deck/rws
```

Within this project, we use the following prefixes. These are obviously just a human convenience so you don't need to use the same ones.

```ttl
@prefix tarot: <https://w3id.org/taro/ontology#> .
@prefix symbol: <https://w3id.org/taro/symbol#> .
@prefix corr:    <https://w3id.org/taro/correspondence#> .
@prefix rws:   <https://w3id.org/taro/deck/rws#> .
@prefix mar:   <https://w3id.org/taro/deck/marseille#> .
@prefix sb:    <https://w3id.org/taro/deck/sola-busca#> .
```

As you can see, we use hash URIs mainly for the benefits explained in this [Hash vs Slash W3C article](https://www.w3.org/wiki/HashVsSlash) (the short version being that it made it easier to publish the data).
