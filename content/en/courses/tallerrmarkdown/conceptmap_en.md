---
title: Concept Map - English
linktitle: Concept Map - English
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  tallerrmarkdown:
    name: Concept Map - English
    weight: 3

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 1
---

The [Concept Maps] (http://teachtogether.tech/#s:memory-concept-maps) describe the topics that the course will address and how they are connected to each other. They also organize the lessons into sets of concepts to be taught per lesson, taking into account the cognitive load and the rule of 7 + - 2 concepts per lesson. This information should help in the decision to use the materials, both to take the course, and to use them in order to generate their own.

> If you want to learn more about Concept Maps and how to teach tech stuff go here: http://teachtogether.tech/


## Concept Map - Full Workshop

{{< diagram >}}
graph LR;
  A[RMarkdown] -->|has diferents| B[outputs];
  A -->|can contein| C[YAML]; 
  A -->|can contein| D[text];
  A -->|can contein| E[code];
  A -->|can contein| F[other];
  D -->|in line| E;
  E -->|named| G[chunks];
  G -->|has| H[name];
  G -->|control| I[behavior];
  C -->|can have| J[params];
  K[symbols] -->|specified| C;
  K -->|specified| D;
  K -->|specified| G;
{{< /diagram >}}


## Concept Map - Lesson 1

{{< diagram >}}
graph LR;
  A[RMarkdown]-->|can contein| C[YAML]; 
  A -->|can contein| D[text];
  A -->|can contein| E[code];
  A -->|can contein| F[other];
  K[symbols] -->|specified| C;
  K -->|specified| D;
  K -->|specified| E;
{{< /diagram >}}

## Concept Map - Lesson 2
{{< diagram >}}
graph LR;
  D[text]; 
  E[code];
  D -->|in line| E;
  E -->|named| G[chunks];
  G -->|has| H[name];
  G -->|control| I[behavior];
{{< /diagram >}}

## Concept Map - Lesson 3

{{< diagram >}}
graph LR;
  A[RMarkdown] -->|has diferents| B[outputs]; 
{{< /diagram >}}

## Concept Map - Lesson 4

{{< diagram >}}
graph LR;
  A[RMarkdown] -->|can contein| C[YAML]; 
  C -->|can have| J[params];
{{< /diagram >}}