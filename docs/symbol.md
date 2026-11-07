# Symbology

This project provides an optional `SKOS` vocabulary for describing the visual elements depicted on tarot cards. These may include animals, objects, people, clothing, gestures, poses, architecture, landscapes, and other recognisable features of a card's imagery.

The vocabulary is non-exhaustive and has been developed primarily with reference to the Rider-Waite-Smith tarot deck.

`https://w3id.org/tarot/symbol`

- [Turtle](data/symbol.ttl)
- [JSON-LD](data/symbol.jsonld)

You can indicate that a card depicts particular symbology using the `tarot:hasSymbol` term.

This vocabulary is provided independently of any particular tarot deck and is entirely optional. Decks and datasets are free to use this vocabulary where appropriate, extend it with additional concepts, or disregard it completely.

The example [Rider-Waite-Smith](./decks.md) deck included in this project makes use of this vocabulary to describe elements of its card imagery.

Importantly, this vocabulary is concerned with what is depicted on the cards, rather than prescribing what those depictions mean. The presence of a particular animal, object, gesture, or other visual element does not imply a single, fixed interpretation or symbolic significance.

## On the use of SKOS

Symbols can carry different meanings across artistic traditions, historical periods, tarot decks, and individual readings. Even familiar visual elements may be identified or understood differently by different people. For example, the Moon card from the Rider-Waite-Smith deck may be described as depicting two dogs, or a wolf and a dog, depending on how the imagery is perceived.

`SKOS` has been used in an attempt to accommodate this nuance and diversity of perspectives. Its hierarchical and associative relationships allow concepts to be defined more broadly or narrowly, and related to one another, without requiring them to be treated as mutually exclusive or universally agreed upon.

The vocabulary therefore makes no attempt to define the meaning or significance of individual symbols, nor does it claim to provide an exhaustive catalogue of the imagery found in tarot. Its purpose is simply to provide a shared means of describing and referencing the visual elements that appear on many of the Rider-Waite-Smith cards, while allowing for differences in how those elements are identified and leaving their interpretation open to the individual reader.

### Use within the Rider-Waite-Smith dataset

Cards within the example [Rider-Waite-Smith](./decks.md) dataset indicate the **most specific** applicable symbols for a given card - they do not each exhaustively list, for example, all of the many ways of referring to a dog - this kind of broader/narrower nuance is made available through the `skos` heirachy.
