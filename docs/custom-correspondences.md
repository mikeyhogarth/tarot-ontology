# Adding your own correspondences

The core ontology doesn't ship any correspondences. It provides two extension points, the class `tarot:Correspondence` and the property `tarot:correspondsTo` - the optional [correspondences vocabulary](./correspondence.md) includes several example correspondence systems built using these extension points. Anyone can publish another system in their own namespace, without changing or asking permission from this project (that's the wonderful thing about RDF and Linked Data!).

## To create a correspondence system

1. Define a class for your kind of correspondence, as a subclass of `tarot:Correspondence`.
2. Define individuals of that class.
3. Define a sub-property of `tarot:correspondsTo` whose range is your class.
4. Link cards to your individuals using that property.

## Worked example: numerology

Numerologists are interested in how numbers relate to one another: for example, that 11 corresponds to 1 (it is made only of 1s) and to 2 (it contains two 1s, and 1 + 1 = 2). This project does not include any numerology correspondences, but its extension points let anyone express them.

The following snippet demonstrates how one might create a numerology correspondence.

```turtle
@prefix tarot: <https://w3id.org/tarot/ontology#> .
@prefix rws:   <https://w3id.org/tarot/deck/rws#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .

# The namespace used here (`example.org`) is a placeholder: if you do this yourself,
# you should publish your own vocabulary under a namespace you control.
@prefix num:   <https://example.org/numerology#> .

# 1. A class of correspondence
num:Number a owl:Class ;
    rdfs:subClassOf tarot:Correspondence ;
    rdfs:label "Number"@en .

# 2. Individuals
num:One    a num:Number ; rdf:value 1 .
num:Two    a num:Number ; rdf:value 2 .
num:Eleven a num:Number ; rdf:value 11 ;
    num:reducesTo  num:Two ;   # 1 + 1
    num:composedOf num:One .   # made only of 1s

# 3. A sub-property of tarot:correspondsTo
num:correspondsToNumber a owl:ObjectProperty ;
    rdfs:subPropertyOf tarot:correspondsTo ;
    rdfs:domain tarot:TarotCard ;
    rdfs:range num:Number ;
    rdfs:label "corresponds to number"@en .

# 4. Link a card to a number
rws:Justice num:correspondsToNumber num:Eleven .
```

As with the [correspondences vocabulary](./correspondence.md), this example is only a demonstration of the mechanism and is not seeking to define any numerology correspondences authoritively.
