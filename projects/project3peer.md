---
layout: assignment
title: 'Project 3: Interactive Visualization - Peer Grading'
parent: '📝 Projects'
released: true
nav_order: 5
---

# Project 3: Interactive Visualization - Peer Grading

You will review 3 Project 3 submissions from your classmates and share constructive feedback. This assignment is an opportunity to both (a) develop skills to effectively evaluate and critically analyze visualization designs, and (b) help guide subsequent efforts by your peers to improve project quality and visualization design across the class.

## Assignment

For each peer review, begin by engaging with the prototype. Interact with the visualization and try to exhaustively cover the views and interactions that the prototype supports. Note what you discover and learn about the data set as you do so. Be sure to also read the write-ups to gain more insight into the process and design decisions behind the prototype.

Next, author a constructive critique of the visualization covering at least the following concerns:

- Visual Encodings. Are expressive and effective visual encodings applied? How well do they reveal the most important features or trends of the underlying data? Is critical data easily seen, or is it unnecessarily "hidden" and only revealed in response to interaction? Is the target audience likely to understand the visualization?
- Interaction Techniques. Do the supported interaction techniques enable more effective discovery of interesting trends, patterns or outliers? Do they engage the viewer in a process of meaningful exploration or learning? Are the interactions well-implemented, without notable performance issues or usability problems?
- Design Quality. Assess the overall design quality in terms of organization and presentation. Are elements appropriately titled or labeled? Is there appropriate spacing, layout, legible type, and other forms of design styling? Is it clear where to begin viewing/interacting with the design? Is the overall display confusing or cluttered? How successful is the prototype in meeting the intended goals?

For each of the concerns listed above – visual encodings, interaction techniques, and overall design quality – we recommend using the ["I like / I wish / What if?"][link] format. Be sure to share positive feedback on effective aspects, critical (but respectful!) feedback on what might be improved, and more wild (even half-baked) ideas a team might explore in subsequent design iterations. Your peer review for each of your 3 submissions should contain **at least a dozen such comments (a minimum of 3 comments for each section (I Like/I wish/What if?))**, often much more!

[link]: https://github.com/dsc-courses/dsc106-wi24/raw/gh-pages/resources/reading/I-Like-I-Wish-What-If.pdf

## Submission Details

This is an individual assignment. You may not work in groups.

Your peer reviews are due **Fri 05/23, 11:59pm**. The links to the submissions that you are required to evaluate will be emailed to you. You must submit peer reviews for 3 Project 3 submissions. To submit your review, you must use gradescope. Please carefully respond to each of the questions raised.

**Some important instructions**:

1. Copy and paste the submission link sent to you for every peer review in the "Webpage Link" section on Gradescope.
2. Please write the 3 comments/sentences per section. Use this template for **each** text box:

```
1. [your statement here]

2. [your statement here]

3. [your statement here]

4. [optional, but feel free to include more feedback!]
```

3. Submit your reviews in the same order as emailed to you.

Here's an example of a high-quality peer review:

I like:

```
1. I like that the visualization effectively distinguishes between estrus and non-estrus periods using different colors. The colors make the differentiation easier as the reader doesn't need to strain their eyes trying to match it to values on the x-axis.

2. I like the implementation of tooltips because it adds another layer of detail that a static visualization would not be able to provide and enables the reader to partake in the data exploration process.

3. I like how the author provided visualization context to convey what the visualization is exactly about so the reader understands the relevant metrics and technical terms before exploring the visualization.

```

I wish:

```
1. I wish that when the reader enters an invalid time, where the minutes exceed the normal range, the system would prompt the user to enter a valid time instead of proceeding. Because the visualization still renders despite the incorrent input, it is unclear what the time represents.

2. I wish the author had simply left out the option to choose between genders with the dropdown menu. From the title and subtitle, it seems like the focus is on how estrus affects the core body temperature of female mice. This change would make the visualization less cluttered.

3. I wish there was more of a compelling story. When comparing estrus and non-estrus, the author could annotate points of the visualization where the difference is very large and very small, so that the reader's attention is immediately drawn to the interesting pattern.

```

What if?

```
1. What if instead of entering a time, there is a slider that allows the reader to simultaneously select valid start and end times?

2. What if the author emphasized the color encoded interactive button by adding an annotation or solid border? The interaction wasn't immediately obvious at first, and it took me quite some time to find out this was even possible.

3. What if the author implemented a dynamic y axis? Right now, the standardization allows the y-axis to be fixed but this makes the visualization less intuitive for the readers to interpret. I wonder if including the true data values will make it easier for the readers to draw conclusions.

```
