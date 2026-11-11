# Design Philosophy

This page lists some of the design philosophy behind the ontology - please bear these in mind when considering contributions or making suggestions for changes.

## No authoritative interpretations

All data within this project, including the ontology itself, is deliberately designed to avoid prescribing or asserting any definitive interpretation of any particular tarot card. We do provide extension points for people to do that though - see [Interpretations](./interpretation.md) for more info.

## Vocabulary reuse

The reuse of established vocabularies for generic concepts is encouraged. Not every concept needs to be defined within a tarot-specific ontology, particularly where suitable terms already exist in well-established vocabularies.

Reusing existing vocabularies helps avoid unnecessary duplication, promotes interoperability, and makes the project's data easier to integrate with other datasets and knowledge graphs.

Throughout this project, we make use of established vocabularies where appropriate. For example, `skos` is used to provide labels for concepts, while `foaf:depiction` is used to link cards to images of them.

We encourage others working with this ontology to follow the same approach, reusing existing terms wherever they adequately describe the concepts being represented.

## Naming conventions

Every property defined in this project is named as a verb phrase describing how a card relates to the value, for example `tarot:hasSuit`, `tarot:inDeck`, `tarot:depictsSymbol` and `tarot:correspondsTo`. Each property's label uses the same words as its name ("has suit", "in deck"), so any statement can be read aloud as a sentence: _the Two of Cups has suit Cups_.

The verb should be chosen to reflect the nature of the statement being made. Correspondences, for instance, use `correspondsTo` rather than `hasCorrespondence`.
