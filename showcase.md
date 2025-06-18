---
layout: page
title: 📺 Final Project Showcase
description: Showcase of student final projects from Spring 2025.
nav_order: 1
# nav_exclude: true
---

# Final Project Showcase

This page lists all projects submitted by the 182 students in Spring 2025's
offering of DSC 106. Projects are listed with the permission of the
student teams.

There were three kinds of awards given to student submissions. The Best Project
Award was given to the top 8% of submissions based on visualization
effectiveness and creativity. The Honorable Mention Award was given to the top
16% of submissions based on effectiveness and creativity. The People's Choice
Award was given to the top 8% of submissions based on votes cast during the
in-person showcase event.

{% for project in site.data.projects %}
{% include project-showcase-card.html project=project %}
{% endfor %}
