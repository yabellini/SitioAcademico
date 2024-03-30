---
title: "useR! Knowledgebase"
subtitle: "The R Project - 2021 Google Season of Docs"
excerpt: "Knowledgebase for organizing the useR! conference (and others)"
date: 2021-11-20
author: "Yanina Bellini Saibene"
featured: true
draft: false
tags:
  - Community
  - R
  - Conferences
categories:
  - Community
  - English
  - R
  - Conferences
# layout options: single or single-sidebar
layout: single
links:
- icon: door-open
  icon_pack: fas
  name: website knowledge base
  url: https://rconf.gitlab.io/userknowledgebase/main/index.html
- icon: door-open
  icon_pack: fas
  name: website info board
  url: https://rconf.gitlab.io/userinfoboard/#welcome
- icon: gitlab
  icon_pack: fab
  name: repo
  url: https://gitlab.com/rconf/userorganization
---

## Project idea: create a knowledgebase for organizing the useR! conference

<img src='featured.png' align="right" height="200" alt='Hexsticker de LatinR. America Latina dibujadas con lineas'/>

### Problem

useR!, the main conference of the R user/developer community organized by the R Foundation, is organized by a different team of (mostly voluntary) organizers each year. Although organizers from one conference will pass information from one year to the next, this usually comes in the form of a massive information dump, e.g. giving access to cloud storage, and the next organizers have to wade through many local/event-specific details to find information relevant for the current year. Long-term history is lost, so each set of organizers often re-evaluates similar tools and processes. Organizations that work with organizers across years, e.g. the R Foundation Conference Committee (RFCC) that selects hosts, or Forwards, the R Foundation taskforce for women and underrepresented groups, often end up re-explaining processes and it can be difficult to ensure improvements made one year are carried over. There has been some effort to gather information centrally, but it is patchy and not in an easily digestible/navigatable form.
Details of Documentation Project

This project will gather existing pieces of documentation and use that as the basis for a useR! knowledgebase in the form of a web book. A good example from the wider R community is the satRdays knowledgebase. The DISCOVER cookbook is another nice example that focuses on diversity and inclusion in scientific computing conferences.

Some of the existing documentation includes:

  * The set of HOWTOs written by Forwards, on aspects that support diversity and inclusion in general:
  * Practical implementation of the code of conduct
  * Organizing community-focused events as part of the conference (newbie session, sessions for community groups)
   * Outreach initiatives (diversity scholarships, conference buddies)
   * The event best practices written by Forwards, on creating a conference that is accessible. Some work on extending this to the virtual conference setting was done in this blog post by the useR! 2021 diversity team.
   * The useR! organization GitLab, created by the RFCC and useR! 2021 organizers. This includes information about:
   * Captioning, background on why it is recommended, what has been used at previous useR!s and some information on providers.
   * Logo files and a corporate identity manual.
   * Summary of review process for contributed presentations and overview of tools used/evaluated by previous useR!s.
   * Summary of review process for tutorials and some helper code for managing.
   * Email templates (e.g. invite emails).
   * Past sponsorship brochures.

Some of this information would be included in the web book, replacing markdown files in git repositories. In other cases, it will still make sense to store files in a git repository, but the web book would describe and link to the relevant files to make them easier to find and use.
How to measure success

The project will be successful if the knowledgebase becomes the authoritative source of documentation on organizing useR! and if R community members contribute to the knowledgebase, helping to improve the documentation and keep it up-to-date.

Therefore, we will consider the project a success if

   * At least two-thirds of the conference-related documentation files currently maintained in the useRorganization GitLab repository and the Forwards conferences and event_best_practices GitHub repositories are deprecated by incorporating and updating that information in the knowledgebase.
   * At least one member of Forwards and at least one useR! organizer (from any year) directly contributes to the text of the knowledgebase.

### Expected Impact

Current/prospective useR! organizers will be able to find more information out for themselves, reducing the burden on knowledgeable individuals such as members of the RFCC or Forwards, or leaders of the useR! organization team. This is especially important as useR! plans to move to a more distributed conference model, with a main conference and regional satellite conferences, each with their own organizing team.
Duration

The scope of this project can be adjusted according to the availability and background of the technical writer(s). As stated, the project could be completed in ~5 hours/week over the 6 month period.

If a writer has more availability, or there are two interested writers, the project could be extended to ~10 hours/week over 6 months to include substantial development/extending of the existing documentation to fill some of the gaps. This would require at least one writer with knowledge/experience of organizing technical/scientific conferences.
Required skills needed to work on this project?

The documentation should be easy for R community members to contribute to. This suggests a markdown-based format, such as Hugo or bookdown. 

### Volunteers

* Heather Turner (@hturner), a member of both RFCC and Forwards, can assist with navigating the existing documentation and creating a workplan for the knowledgebase.
* __Yanina Bellini Saibene__ (@yabellini), a global co-ordinator of useR! 2021, can advise on the topics of tutorials, branding and community partners (the latter is a new topic to be documented).
* John Nash (@nashjc), author of several books on numerical computing and past editor on publications including American Statistician, SSC Liaison (Statistical Society of Canada), can help with copy-editing.

### Citation

To cite the useR! knowledgebase please use:

Sánchez-Tapia, A., Tamir, N., Moy Das, S., Bellini Saibene, Y., Joo, R., Morandeira, N., Hug Peter, D., Vialaneix, N., Bannert, M., Turner, H., 2021. useR! Knowledgebase [WWW Document]. URL https://rconf.gitlab.io/userknowledgebase/ (date of access).

### License

The useR! knowledgebase is under the CC BY-SA 4.0 license
