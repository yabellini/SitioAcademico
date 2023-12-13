---
title: Multilingual Data Science. Part 1.
author: Yanina Bellini Saibene, Natalia Morandeira
summary: "This is part 1 of a 2 parts blog post originally posted on Data Science by Design (DSxD) and cross posted by the Software Sustainability Institute"
date: '2023-08-30'
tags:
  - English
  - Localization
  - Community
---


Language is a cognitive instrument; it is our vehicle for learning and building our world, and thus it can become a source of exclusion.

> “Approximately 64% of Internet content is in English, although only 4.8% of the world's population speaks English as a first language. If we consider Internet users, almost 3 in 4 cannot understand more than 60% of all web content.”¹

Data science affects many people’s lives globally. This practice uses technological tools developed under global open science, software, and education, but most resources are built and published exclusively in English.

> “The predominant language of open source is English—in code, content, and community interactions—and English proficiency is a metric by which performance and personality can be judged.”²

English is the lingua franca for data science, creating a significant barrier for non-English speakers wanting to join the field: We are not allowed to participate if we can’t understand the language.³ The authors have experienced this barrier firsthand, as we both were born in a South American country where the official language is Spanish. Being able to access and use technology and data science is a necessity to adequately teach and research in our careers.

> “The use of the English language [. . .] represents a significant trend in the history of programming language design.”⁴

So, what actions can we take when faced with such a situation? We can use our privileges to change it, and that is where community-driven translations come into play.
Community Path

Translations function as substitutes for original texts. You use them in place of a work written in a language you cannot read5 or that you have difficulties reading; even if you have proficiency in a second language, learning in a foreign language increases your cognitive load. Translations are one of the efforts we can undertake to create a more diverse field of data science. We know that voluntary and collaborative content creation is possible. Open-source software and Wikipedia are great examples of how each person can do their bit. The primary advantage of working collaboratively is distributing the work (hopefully) among a diverse set of people.

In 2017, R-Ladies’ Code of Conduct was translated into Spanish and Portuguese. In 2018, the Latin America R Community collectively translated the R for Data Science (R4DS) book into Spanish, including the packages datos (Spanish) and dados (Portuguese).6 Then, the community translated Teaching Tech Together (T3) and contributed to collectively translating Cheatsheets, The Carpentries’ lessons, and The Programming Historian lessons. The active and growing Spanish-speaking community drives rOpenSci (ropensci.org) to do its first Spanish-language code peer review and translate into Spanish the rOpenSci’s book on best practices for software development, code review, and contribution to open-source projects.⁷ The following ten tips summarise what we have learned in these community-driven translations from being coordinators, translators, reviewers, and editors of books and materials used by tens of thousands of people.

## 1. Motivation

Translating technical material of living documents is a long process with two well-defined stages involving different resources. The first is to achieve a full version of the translated material; the second is to keep the material updated and synchronised between the languages. The project’s type, goals, stage, motivation, and expectations should be clear from the start to have the best chance at success. Different motivation levels appear in collaborative translations:

* Community Motivations: For example, making the material accessible to Latin American people and striving to use it in specific workshops.

* Personal Motivations: The motivations of the specific people involved in the project, such as learning and discussing the content with other participants while translating it. Before people can decide to participate, we must detail the kinds of benefits they might gain, such as: learning technical skills useful beyond this project, giving back to their community, gaining experience working collaboratively in open-source and international teams, connecting with people with similar interests, increasing their network, and mentoring other people during the project.

## 2. Consent of the Text’s Author(s)

Most materials have a license, and for translations, the license should allow derivative work. The authors and/or the editor may have rights to the material. Seek the authors’ consent, and involve them in the process for questions and opinions. In a technical text, the author may define novel terms, and being able to correspond with that person is essential to be as faithful to the original text as possible. From the authors’ point of view, this exchange also invariably improves the original text, from error corrections to finding more diverse examples, gaps in the content, and more. Authors can promote translations by considering this in advance when creating their content. For example, they might publish the text in a markup language, publish in a public repository, or create the text with a structure that lends itself to multi-language translation. If an organization publishes such material, it can assign funding to community translation initiatives.

## 3. Share and Document Your Process and Agreements

Having clear written guidelines for contributing and decision-making makes the entire translation process easier. In this section, we focus on the technical aspect of a project. See section 10 for details about constructing a governance document to formalise the decision-making process and describe how project participants interact. You will need to discuss, use, and regularly update several instruments such as: Roles and responsibilities like translator, reviewer, editor, project lead, graphic designer, etc. This helps to assign responsibilities and credit for contributions (see sections 6 and 10). A tentative agenda with deadlines, tasks assigned, and progress tracking. This helps to keep the project on track (see section 6).

A guide detailing the standardised use of language, including:

  *  Voice usage (e.g., conversational, scientific, formal)
  *  Dialectal variety (see sections 7 and 8)
  *  Grammar, orthography, and punctuation rules
  *  Inclusive and nonsexist language guide
  *  Translating figures and alt text (accessibility, see section 5)
  *  Bilingual technical glossary (see section 9)
  *  Nontechnical words to be translated, such as people’s names, sports or cities in the examples (see Localization in section 4)

These project products are just as important and useful as the main translated text. Share them with an open license.

## 4. Translation in the Spotlight

Internationalisation refers to the technology and design that allows software to adapt to several regions without engineering changes to the source code. The technical solution allows us to localise our content.⁸

Localisation makes content more accessible and suitable within the context of another region, country, or audience.⁸ This includes language, date formats, currency, measure units, and compatibility with different characters.

There are many solutions for internationalising and localising content, and translation is typically the most time-consuming component.⁸

Many projects focus their efforts on internationalisation, trying to choose the right tool for the job. For example, trying to decide if they should use translation management systems (Crowdin, Transifex, Weblate), automatic translators (Google Translate, DeepL), version control systems (GitHub, GitLab), markup languages (LaTeX, Markdown), and tools for writing these languages (Overleaf, RStudio).

Whatever translation tools and markup languages you choose, they should not be a barrier for the team. Choose the tools that best suit your team and the material. For instance, how important is it to prioritise version control? Updates? Preview? Output format? How high is the entry-level knowledge needed to contribute?

Additionally, create processes to help team members who cannot use a particular tool due to accessibility or their own skills. Train the team on the project’s infrastructure, develop instructions (videos, how-to guides, etc.) on using the tools, create peer translation opportunities, and organise onboarding and coworking translation meetings.

## 5. Inclusive and Nonsexist Language

Many languages utilise feminine and masculine gender indicators. Using nonsexist language or gender-equal language in translation means avoiding lexical choices that are biased, discriminatory, or exclusionary in nature. In tech and data science communities, using nonsexist language helps to fight stereotypes about gender roles and promote female and nonbinary representation.

> “The type of language we use is not innocent. If we use a language that takes as the norm and measure of humanity only a part of it (the masculine), we help to persist in the collective imagination the perception that everything that is not masculine is subsidiary, secondary and dispensable. We call this sexist use of language.”⁹

Study nonsexist language recommendations in the language you want to translate, seek advice from experts, discuss options with the team, and document the decision to be consistent through the chapters (and projects). The Carpentries, for example, decided to always use feminine terms in their Spanish translations. In T3 and rOpenSci, we adjusted the wording to avoid having to assign a gender at all. When we couldn’t prevent gender marking, we used feminine/masculine or masculine/feminine splits. For consistency throughout the text and to show that there is no particular hierarchy, we alternated the use of these splits between chapters, with the use of each one being consistent throughout each chapter. Another possibility is to use nonbinary nouns, pronouns, and adjectives (e.g., in Spanish, using -e or -x is the most common option). Which is the best option for the readers of your community?

## References

1. Richter, F. English is the internet’s universal language. Statista https://www.statista.com/chart/26884/languages-on-the-internet/ (2022).

2. Carter, H and J. Groopman, “Diversity, Equity, and Inclusion in Open Source: Exploring the Challenges and Opportunities to Create Equity and Agency Across Open Source Ecosystems,” foreword by Jim Zemlin, The Linux Foundation, December 2021.

3. Odilli Uchidiuno, J. , Ogan, A., Yarzebinski, E. & Hammer, J. Going Global: Understanding English Language Learners’ Student Motivation in English-Language MOOCs. International Journal of Artificial Intelligence in Education vol. 28 528–552 Preprint at https://doi.org/10.1007/s40593-017-0159-7 (2018).

4. Pigott, D.. HOPL, the history of Programming Languages. Wikipedia, The Free Encyclopedia https://en.wikipedia.org/w/index.php?title=Non-English-based_programming_languages&oldid=1130348995 (2006).

5. Bellos, D. Is That a Fish in Your Ear?: Translation and the Meaning of Everything. (Macmillan, 2011).

6. Quiroga, R. ‘The development of {datos} package for the R4DS Spanish translation’. https://rivaquiroga.cl/es/charlas/2020-rstudio-conf.html (2020).

7. Multilingual Publishing. https://ropensci.org/multilingual-publishing/.

8. Wikipedia contributors. Internationalization and localization. Wikipedia, The Free Encyclopedia https://en.wikipedia.org/w/index.php?title=Internationalization_and_localization&oldid=1125663076 (2022).

9. Guía para el uso de un lenguaje no sexista e igualitario en la Honorable Cámara de Diputados de la Nación Argentina. https://www4.hcdn.gob.ar/dependencias/dprensa/guia_lenguaje_igualitario.pdf

> Crosspost: https://www.software.ac.uk/blog/multilingual-data-science-part-1
