# Design Philosophy

## No single interpretation

All data within this project, including the ontology itself, is deliberately designed to avoid prescribing or asserting any definitive interpretation of any particular tarot card.

Interpretation is an inherently contextual and deeply personal aspect of tarot reading. We do not believe it is the role of this project, or of any single authority, to dictate how others should interpret the cards or their meanings, and we are confident that this is the prevailing view within the tarot community. Interpretations may vary considerably, and this diversity is something we seek to respect.

That said, we have provided a small number of interpretation-related properties for those who wish to express and document interpretations:

- `tarot:hasInterpretation` is a property that can be used to record an individual's or group's own interpretation of a card. We strongly recommend that interpretations are accompanied by provenance information identifying whose interpretation is being represented.
- `tarot:hasPopularInterpretation` can be used to describe an interpretation that is widely recognised or accepted within a particular tradition or school of tarot. Our example [Rider-Waite-Smith dataset](./decks.md), for instance, includes a popular interpretation for each card.

Ultimately, the human element is what makes tarot special. This project makes no attempt to establish a definitive or universally authoritative interpretation of any card, nor does it seek to imply that such an interpretation exists. Its purpose is to provide a framework through which interpretations can be represented, attributed, and explored, while leaving the act of interpretation where it belongs: with the individual reader.

## Vocabulary reuse

The reuse of established vocabularies for generic concepts is encouraged. Not every concept needs to be defined within a tarot-specific ontology, particularly where suitable terms already exist in well-established vocabularies.

Reusing existing vocabularies helps avoid unnecessary duplication, promotes interoperability, and makes the project's data easier to integrate with other datasets and knowledge graphs.

Throughout this project, we make use of established vocabularies where appropriate. For example, `skos` is used to provide labels for concepts, while `foaf:depiction` is used to link cards to images of them.

We encourage others working with this ontology to follow the same approach, reusing existing terms wherever they adequately describe the concepts being represented.

## Naming conventions

Every property defined in this project is named as a verb phrase describing how a card relates to the value, for example `tarot:hasSuit`, `tarot:inDeck`, `tarot:depictsSymbol` and `tarot:correspondsTo`. Each property's label uses the same words as its name ("has suit", "in deck"), so any statement can be read aloud as a sentence: _the Two of Cups has suit Cups_.

The verb should be chosen to reflect the nature of the statement being made. Correspondences, for instance, use `correspondsTo` rather than `hasCorrespondence`.
