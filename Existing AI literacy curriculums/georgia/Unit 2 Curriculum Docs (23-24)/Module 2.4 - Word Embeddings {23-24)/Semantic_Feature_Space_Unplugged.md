# Semantic Feature Space Unplugged Activity

**Summary:** students turn their classroom into a three-dimensional
semantic feature space and model the representations of words by holding
up an index card to indicate a word's location in the space. This
activity helps them understand how computers represent word meanings as
points in a multi-dimensional space. These representations are called
"embeddings", and in real AI systems, instead of using just 3 dimensions
we may use 300 or more.

**Authors:** Will Hanna and Amber Jones

**Grade bands:** 6-8, 9-12

**AI4K12** guidelines relevant to this activity:

- **2-A-iv.6-8**: Representation: Feature vectors (word embeddings)

**Materials/Resources:**

- Tutorial material on word embeddings from
  [[https://www.cs.cmu.edu/\~dst/WordEmbeddingDemo/tutorial.html]{.underline}](https://www.cs.cmu.edu/~dst/WordEmbeddingDemo/tutorial.html)

- Index cards or other object that students can hold up to indicate a
  point in space.

**Other relevant education standards:** TBD

**Other relevant activities:**

- Interactive word embedding demo at
  [[https://www.cs.cmu.edu/\~dst/WordEmbeddingDemo]{.underline}](https://www.cs.cmu.edu/~dst/WordEmbeddingDemo)

**Vocabulary**: semantics, semantic feature, feature space, word
embedding

### Vocabulary Definitions

- **Semantics**: the *meaning* of a word or phrase.

- **Semantic feature**: one component of meaning, e.g., features such as
  gender (male/female), animacy (animate/inanimate), age (child/adult),
  number (singular/plural), etc.

- **Feature space**: a multi-dimensional conceptual space where each
  dimension is a feature. Items can be represented in a feature space by
  giving their coordinates along each dimension, e.g., the word "boy"
  could be represented in a two-dimensional age x gender feature space
  as (age=young, gender=male).

- **Word embedding**: a collection of items in a high-dimensional
  feature space where the dimensions are semantic features and the items
  are words. Word embeddings are used by neural network natural language
  processing programs for tasks such as question answering or machine
  translation.

###  Preparation

1.  Decide on a set of three semantic features. The WordEmbeddingDemo
    tutorial uses age, gender, and royalty, but you can choose other
    features if you like, such as size, cuteness, and edibility.

2.  Decide on a set of words that students will encode in this space.
    For example, you could choose "lamb", "automobile", "tree", and
    "gumdrop".

3.  Decide how to lay out the three semantic dimensions in the room. For
    example, you could use the north/south axis to encode size, the
    east/west axis to encode cuteness, and the floor/ceiling axis to
    encode edibility.

4.  Optional: place signs on the walls to help students remember the
    axes, e.g., the center of the north wall could have a sign saying
    "small" while the center of the south wall has a sign saying
    "large". The center of the east wall could have a sign saying "cute"
    and the west wall a sign saying "not cute". You could put an
    "inedible" sign on the floor, and if you can't reach the ceiling,
    put an "edible" sign as high as possible on some wall.

5.  Give each student an index card.

### Student Instructions

- You could introduce the notion of semantic feature space using the
  illustrations in the WordEmbeddingDemo tutorial linked above. Or you
  just could start with this unplugged activity.

- Tell students that this activity will simulate how a computer
  represents the meanings of words in a three-dimensional coordinate
  system, and explain what the three dimensions are (e.g., size,
  cuteness, and edibility). Point out the axis label signs on the walls
  and floor.

- Explain that to indicate the location of a word in the space we're
  going to hold an index card at that point.

- Demonstrate using one word, such as "automobile". Automobiles are
  fairly large (compared with people), so you'll want to be close to the
  south wall. They're not cute but not ugly either, so you might be half
  way between the east and west walls. Finally, automobiles are
  definitely not edible, so you'll want to hold the card close to the
  floor.

- Now pick another word and ask students to decide where that word fits
  in the semantic space. They should hold their index cards in the
  position they think reflects the correct features for that word.

- Students should mostly agree with each other, so their index cards
  should end up in roughly the same place. Pick one student and ask them
  to explain why they chose the location they did.

- If some students are outliers (their cards are far from the others),
  pick one and ask them to explain their reasoning. For example, some
  might think that cars are cute and others might feel that all
  machinery is ugly, so for "automobile" they will hold their index
  cards further east or further west, respectively, than their
  classmates.

### Things to Watch Out For

- We want students to understand that the encoding should represent what
  they think is the common understanding of the word, not their personal
  preferences. So, for example, a student who is a vegetarian will not
  eat lamb, and a diabetic student will not eat gumdrops, but that
  doesn't mean that those things are inedible.

- Attributes like "small" are relative, so it's important to clarify
  what we're comparing to. (Houses are big, but relative to planets they
  are small.) So be sure to specify that for our purposes we're
  assessing size relative to humans.

- Students might want to know how the computer gets its word embeddings.
  The answer is that it uses a machine learning algorithm that is
  trained on a large corpus of text, such as all of Wikipedia. It looks
  at which words appear near each other. For example, the word "gumdrop"
  may appear near words such as "eat", "flavor", "candy", and "tasty",
  suggesting that it is edible.

### What to Do Next

- Try having a student pick a point in space (by holding their index
  card there) and ask the other students to suggest words that might fit
  that point.

- Try the online WordEmbeddingDemo to look at embeddings in a 300
  dimensional space.
