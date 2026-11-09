# Symbology

This project provides an optional `SKOS` vocabulary for describing the visual elements depicted on tarot cards. These may include animals, objects, people, clothing, gestures, poses, architecture, landscapes, and other recognisable features of a card's imagery.

The vocabulary is non-exhaustive and has been developed primarily with reference to the Rider-Waite-Smith tarot deck.

`https://w3id.org/tarot/symbol`

- Download as [Turtle](data/symbol.ttl){ aria-label="Download the symbology vocabulary as Turtle" }
- Download as [JSON-LD](data/symbol.jsonld){ aria-label="Download the symbology vocabulary as JSON-LD" }

You can indicate that a card depicts particular symbology using the `tarot:depictsSymbol` term.

This vocabulary is provided independently of any particular tarot deck and is entirely optional. Decks and datasets are free to use this vocabulary where appropriate, extend it with additional concepts, or disregard it completely.

The example [Rider-Waite-Smith](./decks.md) deck included in this project makes use of this vocabulary to describe elements of its card imagery.

Importantly, this vocabulary is concerned with what is depicted on the cards, rather than prescribing what those depictions mean. The presence of a particular animal, object, gesture, or other visual element does not imply a single, fixed interpretation or symbolic significance.

## On the use of SKOS

Symbols can carry different meanings across artistic traditions, historical periods, tarot decks, and individual readings. Even familiar visual elements may be identified or understood differently by different people. For example, the Moon card from the Rider-Waite-Smith deck may be described as depicting two dogs, or a wolf and a dog, depending on how the imagery is perceived.

`SKOS` has been used in an attempt to accommodate this diversity of perspectives. Its hierarchical and associative relationships allow concepts to be defined more broadly or narrowly, and related to one another, without requiring them to be treated as mutually exclusive or universally agreed upon. This means that even if people disagree on whether something is a dog or a wolf, they may be able to agree on a broader term and as such the user experience for the data still somewhat works even for people who disagree on the symbolism.

### Symbolism specificity within the data

Cards within the [example decks](./decks.md) only indicate the **most specific** applicable symbols for a given card. The data does not exhaustively list, for example, every ancestor concept for the term "dog" (e.g. "animal") - this information is implied by the `skos` heirachy.
