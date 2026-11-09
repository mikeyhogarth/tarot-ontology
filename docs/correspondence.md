# Correspondences

This project provides an optional vocabulary for describing various esoteric correspondences, including elements, zodiac signs, celestial bodies, and Hebrew letters. The correspondences included in this vocabulary are drawn primarily from systems popularised by the Hermetic Order of the Golden Dawn.

`https://w3id.org/tarot/correspondence`

- Download as [Turtle](data/correspondence.ttl){ aria-label="Download the correspondences vocabulary as Turtle" }
- Download as [JSON-LD](data/correspondence.jsonld){ aria-label="Download the correspondences vocabulary as JSON-LD" }

You can apply a correspondence to a card using `tarot:correspondsTo`, or more specifically one of its sub-properties defined in this vocabulary:

- `corr:correspondsToElement`
- `corr:correspondsToZodiacSign`
- `corr:correspondsToCelestialBody`
- `corr:correspondsToHebrewLetter`

This vocabulary is provided independently of any particular tarot deck and is entirely optional. Decks and datasets are free to make use of it where appropriate, or to disregard it altogether. Datasets may also provide their own correspondences: see [Adding your own correspondences](./custom-correspondences.md).

The example [Rider-Waite-Smith](./decks.md) deck included in this project makes use of this correspondences vocabulary. This is particularly relevant given Arthur Edward Waite's historical association with the Hermetic Order of the Golden Dawn, from which many of the correspondences represented here originate.

As with other aspects of tarot, correspondences can be deeply personal, subjective, and dependent on the particular tradition or system being followed. Different schools of thought may assign different correspondences to the same card, and individual practitioners may develop or adopt their own systems. Their inclusion is intended to make these systems available for reference and use, not to privilege one system over another.
