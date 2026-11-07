# Example decks

This project includes several example datasets which demonstrate the ontology in use. All deck datasets include every card along with their rank and suit, as well as images (via `foaf:depiction`) - some decks include additional information as indicated below.

## Rider-Waite-Smith { #rws }

Published in 1909 by William Rider & Son (London) and beautifully illustrated by Pamela Colman Smith under the direction of Arthur Edward Waite.

`https://w3id.org/tarot/deck/rws`

- [Turtle](data/deck/rws.ttl)
- [JSON-LD](data/deck/rws.jsonld)

Of all the datasets included in the project, this is the one that's received the most attention. Every card includes:

- A hand-written `tarot:visualDescription` of each card.
- One popular, non-authoritative interpretation of each card (via `tarot:popularInterpretation`).
- The **symbology** depicted on every card, painstakingly created over many a cup of tea using the provided [symbol](symbol.md) vocabulary.
- Several popular **correspondences** for each card, created using the provided [correspondences](correspondence.md) vocabulary and applied as per the Golden Dawn tradition.

The data also includes links to the equivalent DBpedia resources.

## Tarot de Marseille { #marseille }

Cards following the Marseille tradition and dated to the Jean Dodal edition (Lyon, c. 1701–1715).

`https://w3id.org/tarot/deck/marseille`

- [Turtle](data/deck/marseille.ttl)
- [JSON-LD](data/deck/marseille.jsonld)

In addition, this dataset includes `tarot:visualDescription` for the major arcana and court cards, and the **symbology** depicted on them (via the [symbol](symbol.md) vocabulary).

## Sola Busca { #sola-busca }

Cards of the Sola Busca, made in Italy in the late 15th century (c. 1491). The original maker is unknown.

`https://w3id.org/tarot/deck/sola-busca`

- [Turtle](data/deck/sola-busca.ttl)
- [JSON-LD](data/deck/sola-busca.jsonld)

In addition, this dataset includes `tarot:visualDescription` for some of the cards.
