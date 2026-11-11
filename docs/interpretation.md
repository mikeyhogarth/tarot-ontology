# Interpretations

All data within this project, including the ontology itself, deliberately avoids prescribing or asserting a definitive interpretation of any particular tarot card.

Interpretation is an inherently contextual and deeply personal aspect of tarot reading. We do not believe it is the role of this project, or of any single authority, to dictate how others should interpret the cards or their meanings, and we are confident that this is the prevailing view within the tarot community. Interpretations may vary considerably, and this diversity is something we seek to respect.

That said, we have provided a small number of interpretation-related properties for those who wish to express and document their interpretations:

- `tarot:hasInterpretation` is a property that can be used to record an individual's or group's own interpretation of a card. We strongly recommend that interpretations are accompanied by provenance information identifying whose interpretation is being represented.
- `tarot:hasPopularInterpretation` can be used to describe an interpretation that is widely recognised or accepted within a particular tradition or school of tarot. Our example [Rider-Waite-Smith dataset](./decks.md) includes a popular interpretation for each card.

Ultimately, it is our view that the human element is what makes tarot special. This project makes no attempt to establish a definitive or universally authoritative interpretation of any card, nor does it seek to imply that such an interpretation exists. Its purpose is to provide a framework through which interpretations can be represented, attributed, and explored, while leaving the act of interpretation where it belongs: with the individual reader.

## Assigning an interpretation to a card

There are no restrictions on what the value of an interpretation can be - you can use a literal (such as a piece of text), a link to a resource from any vocabulary or concept scheme, or a structure of your own design.

Here are three ways of giving `rws:TheFool` the interpretation of "a new beginning".

```turtle
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix tarot: <https://w3id.org/tarot/ontology#> .
@prefix rws:   <https://w3id.org/tarot/deck/rws#> .

# The namespace used here (`example.org`) is a placeholder: if you do this yourself,
# you should publish your own concepts under a namespace you control.
@prefix ex:    <https://example.org/> .

# As text
rws:TheFool tarot:hasInterpretation "A new beginning."@en .

# As a link to a concept
rws:TheFool tarot:hasInterpretation ex:BeginningOfJourney .

# As a blank node
rws:TheFool tarot:hasInterpretation [
    rdfs:label "The beginning of a journey"@en ;
    rdfs:comment "Travelling towards the unknown, who knows what the future holds!"@en ;
] .
```

## Attributing an interpretation

Because no interpretation represents the definitive meaning of a card, we strongly recommend recording whose interpretation it is alongside the interpretation itself wihtin your data.

### With TriG

A simple way to record provenance is to put the interpretation in a named graph and describe that graph. This can be written in [TriG](https://www.w3.org/TR/trig/) like so:

```trig
@prefix tarot:   <https://w3id.org/tarot/ontology#> .
@prefix rws:     <https://w3id.org/tarot/deck/rws#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex:      <https://example.org/> .

# The interpretation itself, in a named graph
ex:my-reading {
    rws:TheFool tarot:hasInterpretation "A new beginning."@en ;
                tarot:hasInterpretation ex:BeginningOfJourney .
}

# Who the interpretation was created by.
ex:my-reading dcterms:creator ex:alice .
```

Anyone consuming the data can then decide whose interpretations they want to use, by selecting the graphs created by a person or group they trust.

### With RDF 1.2

[RDF 1.2](https://www.w3.org/TR/rdf12-concepts/) lets you attach provenance to an individual statement via [Triple Annotations](https://www.w3.org/TR/rdf12-concepts/#dfn-triple-annotation). In Turtle 1.2, anything inside [`{| ... |}`](https://www.w3.org/TR/rdf12-turtle/#annotation-syntax) adds additional details to statements:

```turtle
@prefix tarot:   <https://w3id.org/tarot/ontology#> .
@prefix rws:     <https://w3id.org/tarot/deck/rws#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:      <https://example.org/> .

rws:TheFool tarot:hasInterpretation "A new beginning."@en {|
    dcterms:creator ex:alice ;
    dcterms:created "2026-11-11"^^xsd:date
|} .

rws:TheFool tarot:hasInterpretation ex:BeginningOfJourney {|
    dcterms:creator ex:bob
|} .
```

Note that at the time of writing, RDF 1.2 and its Turtle syntax are still W3C drafts and as such support within semantic web tooling is not yet ubiquitous.
