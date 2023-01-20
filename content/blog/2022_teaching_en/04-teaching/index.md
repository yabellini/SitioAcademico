---
title: "Ten quick tips for teaching with (participatory) live coding (on-line)"
weight: 4
subtitle: ""
excerpt: " "
date: 2023-01-20
draft: false
tag:
  - Education
  - Community
  - English
---

Live coding and participatory live coding are effective strategies for teaching programming, as they allow students to see the instructor's thought process and problem-solving techniques in real time while programming. Moreover, it enables active teaching by allowing teachers to follow their learners’ interests, questions, and feedback. However, with the shift to virtual classrooms, we need to adapt these teaching practices to the online context. I try to  achieve this adaptation in this blog post base on my four years of experience teaching coding online at both the undergraduate and graduate levels, using live coding.


## What is (Participatory) live coding ?

The most effective way to teach programming is **live coding**. Instead of presenting pre-written material, the teacher writes code in front of the class while the learners follow along, typing it in and running it as they go. 

## The existing tips for live coding

I use three sources:


* [Top Ten Tips for Participatory Live Coding in a Workshop by The Carpentries](https://carpentries.github.io/instructor-training/17-live/#top-ten-tips-for-participatory-live-coding-in-a-workshop)
* [Ten quick tips for teaching with participatory live-coding paper in Plos Computational Biology](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008090)
* [The live coding session of the book Teaching Tech Together (T3)](https://educarencomunidad.tech/en/index.html#s:performance-live)

This table shows the tips of each text side by side, matching similar tips. The number on each recommendation is the place this tip has on the list. 


| The Carpentries | Plos      | T3               | 
|-----------------|-----------|------------------|
| 1. Stand up and move around the room if possible.| 3.Be seen and heard. | 4.Be Seen and Heard. 11. Face the Screen—Occasionally  |
| 2.Go slowly | 1.Go slowly |3.Take It Slow |
| 3.Mirror your learner’s environment. | 2.Mirror your learner’s environment.| 5.Mirror Your Learner’s Environment|
| 4.Use your screen wisely.| 4.Use the screen(s) wisely| 6.Use the Screen Wisely | 7.Double Devices |
| 5.Use illustrations | 6.Use illustrations—Even better, draw them | 8.Draw Early, Draw Often |
| 6.Turn off notifications | 5.Avoid distractions | 9.Avoid distractions |
| 7.Stick to the lesson material. | 7.Stick to the lesson material | 10. Improvise—After You Know the Material |
| 8.Leave no learner behind. | 9.Get real-time feedback and provide immediate help, 10.Turn learners into co-instructors | 2.Ask For Predictions |
| 9.Embrace mistakes. | 8.Embrace your mistakes | 1.Embrace Your Mistakes |
| 10.Have fun! | | |

We can see that there are many tips that are either repeated in all the sources or are very similar to each other and the order in which they are presented changes.

I took 10 of these tips and added considerations for teaching online.

## The tips for online live coding

### 1. Be seen and heard

As learners are coding along, it is important they clearly see and hear what you are doing. In online setting accomplish this may require more resources in terms of technology and infrastructure, such as stable internet connection a wide screen or a second screen for you and your students. 

* **Before start:** explain to your students how to accommodate their screen. In case they have only one screen (it is the caso of most of my students) demonstrate how they can divide the screen in two vertically or horizontally.  In case they have two screens, how to split the windows, one with the teacher's screens and the other with their programming environment.  You can have some pictures or videos to show how to accomplish this.  If you are teaching a long course (more than 3 clases) you can show case this on the first classes and then only do it time to tima as a reminder.  You can also share this videos or picture so your students can check how to order they screens.

* **Live Coding:** 

  * share your screen and ask before starting coding if they see it and if the size of the font is adequate. Change it if your students request it. 
  
  * Enlarge your mouse pointer and consider using a pointer highlight ([something like this](https://www.gnome-look.org/p/999801/)). 
  
  * Use a program that shows your screen presses, like[ Screenkey](https://gitlab.com/screenkey/screenkey).  If you forget to say the shortcut you use aloud, the soft will show this on the screen for your students.

  * The white background seems better for synchronous classes. The night theme looks better for recorded videos because some students watch them at night and use small devices.

  * If you can, share your code live as you write it. Antonio Vazquez Brust [explain how to do this using `ngrok` and RStudio for teaching R](https://bitsandbricks.github.io/post/code-live-from-rstudio-and-share-it-with-the-world-in-real-time/) and Elio Campitelli explain how he [teach R with frictionless live coding in this video](https://youtu.be/idFpvvH1JyI). There are other tools for other languages, Naomi Alterman show us [how to live streaming your live coding to static webpages for audience in this talk](https://youtu.be/a3uJj7Eqwzg) for CarpentryCon. 
  
* **After live coding**: share your code, you can copy and paste on the chat of the platform, copy and paste on the shared notes or upload to the course webpage or virtual campus. This will help your students to validate their code and to catch-up if they can't copy or write some part of the code.


### 2. Go slowly and don’t teach alone

When you do participatory live coding, you need to teach and program at a pace that allows learners to follow along and not get left behind. This is especially important in online setting if people are switching between windows (the teacher demostration and their own coding) or between screen if they have more than one.

* Start with a blank script or notebook, this ensure you will explain everything they need for the code to work. 

* Before starting, coding said aloud and write in the notebook or as comment in the script, the goal of the code we are going to develop.  This helps to focus on what we want to accomplish and the reasoning behind to code for that goal.

* Explain every step you made. Say out loud what you are doing while you do it for every command you type, every word of code you write, and every menu item or website button you click. Then, point to the command and its output on the screen and go through it a second time.  This allow students to check what they did.

* If the output of your command or code makes what you just typed disappear from view, scroll back up so learners can see it again.

* Don’t use many keyboard shortcuts, especially at the beginning. If you use a keyboard shortcut say it out loud the first times you do. Explain an alternative to the shortcut (for example using menus).

* Your helper should be watching the chat, helping to troubleshooting and solving problems of students, copying links or piece of code if need it, and letting you know when something needs to be clarified or re-explain or shown one more time. If you are alone, let students know when you are going to watch the chat to help them.
Be clear about how they can participate and make questions (using the chat, unmuted them, using non verbal expresión, using shared notes, etc.) and how are you going to answer.


### 3. Use your screen ...  
 Some people now use two devices when teaching: a laptop plugged into the projector for learners to see and a tablet so that they can view their own notes and the notes that the learners are taking  
  