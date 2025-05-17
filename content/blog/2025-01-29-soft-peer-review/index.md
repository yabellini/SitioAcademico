---
title: "Implementing Software Peer Review. Tips and Examples"
author: 
- Yanina Bellini Saibene
summary: "Peer review is a helpful tool for ensuring high-quality, reliable, and maintainable software. In this document, we share insights discussed in the Chan-Zuckerberg Initiative’s Essential Open Source Software program community call held on January 29, 2025, featuring rOpenSci’s Noam Ross." 
date: '2024-01-29'
categories:
  - Community
  - 100DaysToOffload
  - Open Source Software
tags:
  - Community
  - 100DaysToOffload
  - Open Source Software
---

{{< figure src="featured.jpg" alt="">}}

This resource was first developed by attendees at the January 29, 2025 Chan Zuckerberg Initiative community call for the Essential Open Source Software program. The call featured Noam Ross from rOpenSci, who shared his experience with implementing peer review in open source software.

## Setting Goals for the Peer Review Process: What does your project want to achieve?

Software peer review is beneficial at various stages of development and can be used for a variety of purposes. When considering implementing a review process, the first step is thinking about the task itself: What is it that you’re trying to review? A few examples of cases that can benefit from review include:

- A new, complete software project (e.g., preparing for its first release)
- A new pull request for an existing project
- An existing project undergoing maintenance
- An existing project receiving major updates
- An existing project adding features or security enhancements

Each particular case requires thinking through the goals of the review. In some cases, for example, the goal is to improve the quality of the software and ensure that contributions and packages follow best-practices; in other cases, review motivations may be more narrowly focused, such as ensuring that software complies with an organization’s security standards. It is therefore worthwhile to discuss objectives with project members and the community, focusing as much as possible on the groups the changes will impact the most. In other words, what is your project’s goal in implementing peer review processes, and who do these enhancements benefit?

Goals that benefit the project’s **developers** might include:

- Managing interoperability and dependencies
- Software development skill-building and best-practices
- Improving or maintaining security
- Protecting the project’s brand or reputation
- Benefitting from various areas of expertise of team members and the community
- Saving time

Goals that benefit the project’s **users** might include:

- Higher quality software
- Reusable software
- Improving awareness of the project’s changes
- Minimizing breaking changes and downtime for users

When considering implementing peer review, take time to think about other stakeholders who might benefit (or otherwise be impacted) by review processes and their outcomes. Are there upstream or downstream projects whose developers should have input into review process design? Is there someone on your team who communicates project changes and needs to be brought into the implementation process to better help the community understand the new process? Starting with the broadest group of stakeholders possible and narrowing the group down according to the goals and impacts of the review process helps to ensure that the new process is well-received and sensitive to stakeholder needs.

## Quick Tips

### Set Basic, High-Level Guidelines

Establishing and communicating the top-level goals and processes involved in your project’s peer review implementation makes it easy for the community to understand the value of reviews and the expectations associated with being involved in the review process. rOpenSci’s Editorial Board, for example, succinctly states the project’s objectives and expectations (quoted below, verbatim):

- **Develop standards and guidelines** for your authors and reviewers to use. Borrow these freely from other projects (feel free to use ours), and modify them iteratively as you go.
- **Use automated tools** such as code linters, test suites, and test coverage measures to reduce burden on authors, reviewers, and editors as much as possible.
- **Have a clear scope**. Spell out to yourselves and potential contributors what your project will accept, and why. This will save a lot of confusion and effort in the future.
- **Build a community** through incentives of networking, opportunities to learn, and kindness.

## Other high-level guidelines might include:

- Pay attention to upstream and downstream dependencies
- Define and enforce guidelines for productive, inclusive communication about the review process (for both reviewers and reviewees)
  - Ensure that a Code of Conduct is linked in the guidelines document and that review communications adhere to the CoC
  - Provide guidance and training in healthy communication to those who will be conducting reviews
  - Make CoC violation reporting mechanisms transparent to those having their contributions reviewed
- Communicate when reviews lead to acceptance or rejection, and be thoughtful and clear when explaining rejection–contributors are more likely to “try again” when they have a positive experience and understand why changes are not accepted

## Decide Who is Responsible for Reviewing

Peer review is an extremely productive process, but it is also a labor-intensive one. Project contributors and maintainers are often already busy and adding additional tasks can create a burdensome and tiring environment. How can your team share the work of reviewing while ensuring the review process produces desired results? Your project might consider:

- Discussing who has the skills to participate in reviewing software
- Deciding how to upskill those who are interested in reviewing
- Setting a reasonable cadence for review (e.g., ongoing or in batches)
- Engaging the broader community in the review process

## Incentivize and Recognize Reviewers

In both scientific publishing and software development, providing good reviews can feel like a thankless job. It is therefore important to consider how to incentivize and recognize reviewers. For example:

- Featuring reviewers and their work in project blog posts or newsletters
- Creating badges or other public-facing signifiers for reviewers
- Implementing an open review process, where reviewers and their reviews are shared publicly
- Automating where possible, such as implementing CI tools, to reduce reviewer burden and incentivize participation
- Use review as an on-ramp to other leadership roles in your project (e.g., maintainer, core team member)
- Offer avenues to authorship or other formal recognition of effort in outputs
  - Your team could start with the CRediT Model to help define when reviewing contributions rise to the level of authorship
- Examples:
  - Bioconductor’s Package Reviewers Recognition page


The full article and list with all the authors can be access on the [article webpage](https://eoss-om-communitycalls.github.io/2025-01-29-software-peer-review/).  
