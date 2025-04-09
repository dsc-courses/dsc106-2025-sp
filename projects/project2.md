---
layout: assignment
title: 'Project 2: Persuasive/Deceptive Visualization'
parent: '📝 Projects'
released: false
nav_order: 2
checkpoint_due: 'Tue Apr 22, 11:59pm PT'
due: 'Tue Apr 29, 11:59pm PT'
---

# Project 2: Persuasive or Deceptive Visualization?

{: .no_toc}

{: .summary}

> In this assignment, you will grapple with how to design visualizations
> ethically by crafting two different, opposing perspectives to the same
> question posed about a single dataset. Once this assignment is complete, we
> will (anonymously) peer review each other's visualizations.
>
> **Checkpoint Due: Tue 04/22, by 11:59pm**
>
> **Complete Project Due: Tue 04/29, by 11:59pm**

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

It is tempting to think of data and visualization as a neutral actor, with a
single "correct" set of design choices that "truthfully" _report_ the data.
However, outside of egregious errors (e.g., when dates are [sorted
incorrectly](https://www.atlantamagazine.com/great-reads/behind-georgias-covid-19-dashboard-disaster/)
or the y-axis is not [scaled
uniformly](https://twitter.com/whitehouse/status/1486709480351952901)), we see
that "ground truth" in data is much more contextual and situated. Design choices
we make give visualization a rhetorical power that influences what a reader
concludes and remembers about the data, and blurs the line between persuasion
and deception. For instance, contrast Simon Scarr's [Iraq's Bloody
Toll](http://www.simonscarr.com/iraqs-bloody-toll) with a [more conventional
representation](https://www.infoworld.com/article/3088166/why-how-to-lie-with-statistics-did-us-a-disservice.html)
of the same data, and consider why Scarr's visualization won an award while
another visualization that made similar design choices—[Gun deaths in
Florida](https://www.businessinsider.com/gun-deaths-in-florida-increased-with-stand-your-ground-2014-2)
by Christine Chan—was widely considered to be misleading.

## Your Tasks

1. Select one dataset from [the list provided below](#datasets). These datasets
   are intentionally chosen to cover politically charged topics, as ethical
   analysis and visualization is especially critical in such situations.

2. Spend time exploring and familiarizing yourself with the dataset (e.g.,
   through exploratory visual analysis). Once you feel like you've developed an
   understanding of the data, **devise a proposition** about it: a statement
   that asserts a judgement or opinion about the trends you might have
   uncovered. An example of a proposition might be _"Gun deaths spiked after
   Florida enacted its 'Stand Your Ground' law."_

   When devising your proposition, please keep in mind our goal of fostering a
   respectful and inclusive environment. In particular, while you are welcome to
   formulate controversial propositions, **propositions that demean or
   dehumanize people** (e.g., based on their race, gender expression, sexual
   orientation, disability, or other aspects of their identity) **are not
   acceptable**. If you are unsure whether your proposition is suitable or not,
   please make a private forum post or ask a course staff during office hours.

3. **Design two visualizations** to persuade a reader about each side of the
   proposition (i.e., one visualization should persuade the reader that the
   proposition is true while the other should persuade the reader that the
   proposition is _not_ true).

   We encourage you to use whatever design choices you find produces **the most
   persuasive** visualization _for each side_ of your proposition. You are
   welcome to not only use techniques we would usually consider to be _earnest_
   (e.g., effective and expressive encodings, transparently communicating data
   transformations, citing sources, etc.) but also those we might sometimes
   consider to be _deceptive_ (e.g., violating conventions, skewed or slanted
   titles and labels, truncated scales and axes, filtering outliers, etc.). In
   doing so, you are likely to discover that there is not always a clear
   distinction between the two categories.

   Note, however, that this goal of persuasion also means that, **if you use any
   deception techniques, they should not be immediately obvious** (including to
   the course staff!) as they might otherwise backfire and dissuade your reader.

   As with prior assignments, you are free to use any visualization tools, and
   should carefully consider data transformation, visual encoding, textual
   content (i.e., titles, axes, labels), and annotations. Moreover, in this
   assignment, we construe "visualization" broadly (i.e., a single visualization
   can include several concatenated or inset charts).

4. **Bullet point your design decisions and rationale.** For each visualization,
   enumerate 3–5 design decisions you think are central to making the
   visualization persuasive (note, a "design" decision can also refer to
   decisions you made about data transformation or textual content). For each
   decision:

   1. Score, on a diverging scale from `-2` to `2`, how deceptive or earnest
      your decision is (where `-2` is fully deceptive, `0` is neutral, and `2`
      is fully earnest). Only use a score of `0` if you are really unable to
      decide one way or another. You may use `0.5` steps as needed.

   2. Write a couple of sentences documenting your decision, with corresponding
      rationale/justification. How does this decision help make your
      visualization persuasive? What worked well, and what didn't? What other
      alternatives did you consider, and why did you settle on this one?

5. After documenting these decisions, write a 2–3 paragraph **final reflection**
   on your overall design process across both visualizations. What was
   straightforward or difficult? What surprised you? How do you now define
   "ethical analysis and visualization"? What bounds (if any) can you draw to
   distinguish "acceptable" persuasive choices vs. "misleading" ones (and if
   none, why not)?

## Submission Details

This is an individual assignment. **You may not work in groups**. There is a
checkpoint submission due on **Tue 04/22, by 11:59pm**. Your completed
assignment is due on **Tue 04/29, by 11:59pm**.

### Checkpoint Submission

You must submit your assignment using Gradescope. Please upload a single PDF with the following:

1. One the first page, 2 persuasive visualizations for one side of a proposition. The visualizations could be persuading the same proposition or two different propositions.
2. In a **separate** page, 2 persuasive visualizations for the other side of a proposition. Again, they will either be persuading the opposite stance from the same proposition as the first page or the two different propositions from the first page. 
3. In a **separate** page, a writeup that states what proposition(s) you are trying persuade on both sides, which set of visualizations you are leaning towards, and the deceptive techniques used. Bullet points are fine.

### Final Submission

Your final submission should take the form of an **HTML web page** that states
your proposition, includes both visualizations and their corresponding design
decisions and rationale, as well as your final reflection write up. To help you
put this page together, we're providing a <a href="project2_report.html"
download>basic HTML template</a> for you to fill in. You will need to edit the
HTML page to add your captions and correctly link your images (for simplicity,
we recommend exporting image files to the same local directory as your HTML
file).

Please **deploy your HTML report to a publicly accessible URL**. We recommend
GitHub Pages (as described in lab 1). Your Project 2 submission can be part of
the portfolio website that you've made for the labs (e.g., a subdirectory). Once
deployed, please **double check** that your web page is appearing and rendering
correctly at the publicly-accessible URL (e.g. that there are no broken images
or links).

## Grading

The assignment score is out of a maximum of 14 points: 5 points for each
visualization, and 4 points for your write-up. Submissions that squarely meet
the requirements (i.e., the "Satisfactory" column in the rubric below) will
receive a score of 10. We will use the following rubric to grade your
assignment. _Note:_ unlike Project 1, most rubric cells do not map
exactly to specific point scores because we anticipate a diversity in how you
choose to apply earnest and deceptive techniques. As a result, **the staff will
rely heavily on your write-up for grading this assignment** (in particular, to
identify _which_ techniques you used and whether you consider them an earnest or
deceptive application). _Note also:_ there is up to +1 bonus point available
for especially creative or original submissions.

{:#rubric.rubric}
| Component | Excellent | Satisfactory | Poor |
| --------- | --------- | -------------| -----|
| **Data Transformations**<br>_(per visualization)_ | More advanced transformations (e.g., groupings, binnings, calculated fields, etc.) extend or manipulate the dataset in interesting and/or unexpected ways.<br>_(0.5 points)_ | The raw dataset was mostly used directly, with perhaps some simple transforms (e.g., sorting, filtering) to facilitate communicating the visualization's message.<br>_(0 points)_ | - |
| **Marks, Encodings, and Visual Design**<br>_(per visualization)_ | Visual design persuasively argues the visualization's stance (for/against the proposition), and facilitates effortless reading even when used deceptively. Any deceptive visual design choices are very subtle—even seasoned readers can only identify them on close study.<br>_(2.5 points)_ | Visual design is largely persuasive, but some issues hinder comprehension. Any deceptive visual design cannot be detected at first glance, but are identifiable on a second look.<br>_(2 points)_| Visual design is distracting or makes the visualization unnecessarily or unintentionally difficult to read. Any deceptive design can be immediately identified.<br>_(1.5 points)_ |
| **Titles, Labels, and Annotations**<br>_(per visualization)_ | Titles, labels, and annotations persuasively describe, contextualize or frame the depicted data. Any slants that may be considered deceptive are imperceptible to the reader.<br>_(2 points)_ | Necessary titles and labels are present, but annotations could be better used to persuasively narrate the visualization's stance. Any deceptively slanted content is more easily detectable by readers.<br>_(1.5 points)_ | Several titles or labels are missing, or do not provide human-understandable information. Annotations are rarely used. Strong, charged, or colorful language makes it easy to detect deceptive content.<br>_(1 point)_ |
| **Design Rationale and Reflection** | Well crafted write-up provides reasoned justification for all design choices with a thoughtful reflection on their ethical implications.<br>_(4 points)_ | Most design decisions are described, but rationale or ethical reflections could be explained at a greater level of detail.<br>_(3 points)_ | Missing or incomplete. Several design choices are left unexplained, and/or ethical reflection is relatively shallow.<br>_(2 points)_ |
| **Creativity and Originality** | You exceeded the parameters of the assignment, with creative, original or a particularly engaging designs.<br>_(up to +1 bonus point)_ | You met all the parameters of the assignment.<br>_(0 points)_ | – |

## Datasets

Please select one dataset from the options below. **You must use the same dataset for both visualizations**, but you are free to transform the data differently for each design.

- [Human Development Indicators, 1960–2020](https://github.com/light-and-salt/World-Bank-Data-by-Indicators). The World Bank has tracked global human development by indicators such as economy, education, environment, gender equality, health, and science and technology since 1960. The linked repository contains indicators that have been cleaned and formatted to simplify visual analysis and visualization design. However, you're also welcome to browse and use the original data [by indicator](https://data.worldbank.org/indicator) or [by country](https://data.worldbank.org/country). Click on a category to download the CSV file on the right-hand sidebar.

- [Climate Change Indicators](https://climatedata.imf.org/). Similar to the previous dataset, the International Monetary Fund (IMF) tracks a number of metrics related to climate change including greenhouse gas emissions, strategies for mitigating or adapting to the impacts of climate change, transitioning to a low-carbon economy, climate finance, and the impact on weather. The data is structured as "crosstabs" (also known as "wide" data) where every time period (e.g., quarter or year) is given its own column. To facilitate visualization and visual analysis, you might wish to [pivot the data](https://help.tableau.com/current/pro/desktop/en-us/pivot.htm) into a "long" format.

- [Civilian Complaints Against New York City Police Officers](https://www.propublica.org/datastore/dataset/civilian-complaints-against-new-york-city-police-officers). This is a dataset compiled by ProPublica, an independent, nonprofit investigative journalism newsroom. It contains more than 12,000 civilian complaints filed against the NYPD, with demographic information about the complainant and officer, the category of the alleged misconduct, and the result of the complaint.

- [Abortion Data by U.S. State from the Guttmacher Institute](../resources/data/GuttmacherInstituteAbortionDataByState.xlsx) The Guttmacher Institute is a research and policy organization committed to advancing sexual and reproductive health and rights. They maintain a variety of global data related to global reproductive rights. This data set contains data about abortion rates, abortion providers, and abortion seekers, aggregated to the state level.

## Resources

The following research papers help enumerate the ways different choices in data transformation, visual design, and textual content can impact the persuasiveness of visualizations and readers' perceived trust in them:

- [The Work that Visualization Conventions Do](https://eprints.whiterose.ac.uk/93521/3/repository20.pdf), by Helen Kennedy et al. _Information, Communication & Society._
- [Frames and Slants in Titles of Visualizations on Controversial Topics](https://www.zcliu.org/vistitles/CHI18-VisTitles.pdf), by Ha-Kyung Kong et al. _ACM CHI 2018_
- [From Invisible to Visible: Impacts of Metadata in Communicative Data Visualization](https://cyxiong.com/wp-content/uploads/2022/12/impactsMetadata.pdf), by Alyxander Burns et al. _IEEE TVCG 2022_
- [Affective Learning Objectives for Communicative Visualizations](https://arxiv.org/abs/2208.04078), by Elsie Lee-Robbins and Eytan Adar. _IEEE TVCG 2023_
- [Affective Visualization Design: Leveraging the Emotional Impact of Data](https://arxiv.org/abs/2308.02831) by Xingyu Lan, Yanqiu Wu, and Nan Cao. _IEEE TVCG 2024_
