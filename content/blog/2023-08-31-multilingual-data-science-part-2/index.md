---
title: Multilingual Data Science. Part 2.
author: Yanina Bellini Saibene, Natalia Morandeira
summary: "This is part 2 of a 2 parts blog post originally posted on Data Science by Design (DSxD) and cross posted by the Software Sustainability Institute"
date: '2023-08-30'
tags:
  - English
  - Localization
  - Community
---

## 6. Baby Steps and Tracking Progress and Contributions

Dividing the entirety of the work into smaller activities and milestones allows for better task assignment and tracking. For book translations, a chapter is often a good unit of division. But other items must also be translated, like figures, alt texts, code examples, and datasets. There are also extra activities: ensuring the correct use of nonsexist or inclusive language, checking spelling/grammar, and looking for alternative external references available in the language of the translation, among others.

Keeping a record of these activities allows you to intervene, assist, discuss a process, seek replacements or more participants, look for an alternative tool, and do periodic progress reports (even if no progress has been made!). For T3, we reported progress weekly in the translation Slack channel, detailing the completed tasks and thanking those who had participated. For the translation of R4DS, we updated task completion in the GitHub repository.

Tracking and reporting allow all contributions to be recognized adequately—not only the most common roles (translators, reviewers, and editors) but also those who advise on specific topics, solve technical problems, or perform graphic design work.

The tool you select to record this information will be related to the tool you choose for the translations. For example, you can use GitHub projects and issues, as we did for R4DS and rOpenSci, or you can use a shared spreadsheet and GitHub issues, as we did for T3. Some translation management systems record the progress, but not who contributes. Whichever set of tools you select, keep your progress updated, record the necessary information to give credit where it is due, and make sure you know how long each task takes. That information will be invaluable for this and other projects.

##  7. Flexibility: Don’t Be Literal, and Bring the Message Closer to Your Audience

This point is directly related to localisation. Examine the examples, source codes, data, idiomatic expressions, poems, songs, metaphors, and analogies included in your source material. These items cannot be translated literally (and are usually mistranslated by artificial intelligence apps). Instead, propose a translation that makes it possible to understand the expression’s meaning while remaining as faithful as possible to the original text’s meaning for the target audience. You can ask a bilingual person or the author themselves for insight into the phrase’s meaning, and you may also adapt the examples using regional data and local artists and cultures.

T3 has an example using Canadian geography wherein we replaced it with a Latin American example:

* Original text: “Factual errors like believing that Vancouver is the capital of British Columbia (it’s Victoria).”

* Spanish example: “Factual errors like believing that Rio de Janeiro is the capital of Brazil (it’s Brasilia).”

On an R4DS code snippet to teach loops, we replaced the song “Ten Green Bottles” with “Five Little Green Frogs,” the Spanish version of the song. We also translated all the data in the exercises themselves, including the variables’ names, currency, date format, and measure units. In T3, we used a poem by María Elena Walsh on a code for teaching functions.

## 8. Linguistic Diversity

A diverse language needs a diverse translating team. Some languages have dialects or regional variations. For example, “green beans” have almost ten different names across Spanish-speaking countries. In some countries, technical texts use more anglicisms than others. With people from different countries translating and reviewing one source text, these idiomatic differences will arise during the process, and by working together you can make a decision that works best for the intended audience.

Part of the agreements you will have to make is deciding which dialect or regional variation of the language is being used (R4DS, T3, and rOpenSci use Latin American conventions for the Spanish translation) and which word you will use when a concept has more than one option. Holding a team and/or community vote on these matters is one helpful idea. You also have to decide on specific details, such as what grammatical gender to use with technical concepts that don’t have a translation (or that you decide not to translate). For example, is the R-operator la pipe (she) or el pipe (he)?

The agreements must be properly documented (see section 3) to build a translation and localisation community memory that can be reused and improved upon.

## 9. Create a Bilingual Glossary

A bilingual glossary contributes to the localisation memory of the community. It can be as simple as a CSV file with the list of terms in the source language and their equivalent in the target language, or it can also contain the definitions in one or more languages. There are several initiatives: for T3, we built an English-Spanish dictionary of educational technology terms¹⁰; for rOpenSci, we are creating an English-Spanish glossary of research software development terms; and The Carpentries has the glosario project, a dictionary of data science terms in more than twenty languages.

## 10. Build a Community Around the Translation

The governance document mentioned in section 3 describes the roles, structure, organization of the work, and all the documents needed to accomplish the translations. For example, in T3, we organised the team with one leading person, two editors, one translator per chapter, and two reviewers per chapter. We also decided to discuss translation issues on Slack. If we didn’t get a consensus, we asked the community through social media and GitHub issues. Alongside participant roles, you will need to agree on and document:

   * A Space for Community Interactions: This can be a Slack/Discord channel or workspace or the GitHub/Gitlab repository of the project. You can also have synchronous meetings for working and sharing the achievements of the project and the members.
   * Accessibility/Diversity Statements: For example, ensuring alt text for images, using colour palettes that address colour blindness, allowing open access, and using an open format compatible with assistive technology such as screen readers.
   * A Code of Conduct: Ensure there is a clear way to reinforce it.
   * Citation, Attributions, and License: Translators have authorship of the translated contents. In T3, we mentioned the translators and reviewers below each chapter title, and we added an “About the Translation” chapter¹¹ with a short description of the project and all the participants. We also published our Translation Guidelines¹² with all the contributors as authors¹². Finally, we added a suggested citation of the Spanish version of the book according to the relative contributions along the translation process¹¹.

Last, but not least, building a community also means prioritising the group’s well-being and having the people involved in lateral projects derived from the translation. Some methods of building community might be: besides discussing governance, working on the translation itself, having social meetings, naming the group and creating a logo for it, sharing concerns and supporting others, disseminating the translation process via social media, and receiving and sharing feedback. Without forgetting the previous tips on motivation and making sure the translation is in the spotlight, ideally the group can enjoy and learn during the process, have fun working on it, celebrate everyone’s achievements, and—why not?—make new collaborations and friends!

## Concluding Remarks

Working toward multilingual data science through translations and localisations is a crucial step in removing language barriers and ensuring that the knowledge and innovations in data science are not limited to a select group of individuals who speak a certain language. This information should be accessible to everyone! Multilingual materials and the community translation process serve to advance the field and allow for a greater, more global collaboration and exchange of ideas among data scientists from different backgrounds and regions, improving the discipline as a whole. Now, think of your favourite data science book or material. Are you aware of the importance of other people being able to access that content? How can you help make it available to them? By working together, we can create a more inclusive and diverse community of data scientists and foster a greater sense of community and collaboration within the discipline. 

## References

10. Bellini Saibene, Y. English-Spanish dictionary of educational technology terms. https://yabellini.shinyapps.io/T3Glossary/.

11. Wilson, G. 2021. “Enseñar tecnología en comunidad. Cómo crear y dar lecciones que funcionen y construir una comunidad docente a su alrededor” [Teaching Tech Together. How to create and deliver lessons that work and build a teaching community around them] (Spanish translation: Y. Bellini Saibene, N.S. Morandeira, P. Corrales, L. Acion, M. Dermit, Y. Sosa, J. Benitez Saldivar, Z. Bazurto, S. Canelón, L. Canaviri Maydana, M. Alonso, A. Bellini, P. Minotti, R. Chirinos, P. Rojas, N. Stroud, R.N. Villafañe, P. Loto, A.L. Diedrichs, Y. Terrazas-Carafa & L. Rodríguez Planes). https://teachtogether.tech/es/ (Original English work published in 2019).

12. Bellini Saibene, Y, N.S. Morandeira; P. Corrales; L. Acion; M. Dermit; Y. Sosa; J. Benitez Saldivar; Z. Bazurto; S. Canelón; L. Canaviri Maydana; M. Alonso; A. Bellini; P. Minotti; R. Chirinos; P. Rojas Saunero; N. Stroud; R.N. Villafañe; P. Loto; A.L. Diedrichs; Y. Terrazas-Carafa; L. Rodríguez Planes. 2022. “Orientaciones para la traducción al español de Enseñar Tecnología en Comunidad”. doi:10.5281/zenodo.7261895


> Crosspost: https://www.software.ac.uk/blog/multilingual-data-science-part-2