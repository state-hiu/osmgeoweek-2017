---
layout: default
title: About
published: true
twitter-description: Sign up for an event near you or plan your own mapathon. You can contribute to mapping projects around the world and explore the power of maps! Get in touch, we're happy to help!
---

<!--counts of events and projects-->
{% assign event_counter = 0 %}
{% for event in site.categories.event %}
    {% assign event_counter = event_counter | plus: 1 %}
{% endfor %}

{% assign project_counter = 0 %}
{% for project in site.categories.project %}
    {% unless project.tags contains 'notfeatured' %}
        {% assign project_counter = project_counter | plus: 1 %}
    {% endunless %}
{% endfor %}

<div class='fill-blue'>
  <div class='liner clearfix center fill-darken3 dark col12'>
    <h2 class='pad2'>About OSMGeoWeek</h2>
  </div>
</div>


<div class='limiter pad4y clearfix'>
<h3>A global coalition of partners are hosting mapping events at colleges, community centers and other institutions to map places around the globe, following this year’s Geography Awareness Week theme, “Explore! The Power of Maps”</h3>
<p/><br/>

OSM Institutions will host the flagship OpenStreetMap mapping party on Thursday, Nov. 19, from 6:30 p.m. to 9 p.m. EST at Peace Corps headquarters in Washington, D.C., with the goal of actively contributing to OpenStreetMap. Admission is free, but interested individuals should <a href="https://www.eventbrite.com/e/access-for-all-osm-geoweek-2015-tickets-19153645068">RSVP online</a>.
<p/>

On the local level, grassroots organizers around the world are holding <a href="{{site.baseurl}}/events/">over {{event_counter}} events</a> at local schools and community centers during OSMGeoWeek. If you are organizing an event, or even thinking about it, get in touch at <a href='mailto:mapgive@state.gov'>mapgive@state.gov</a>.
<p/>

There are a collection of <a href="{{site.baseurl}}/projects/"> {{project_counter}} featured Mapping Projects</a> to work on during the week. Organizers and participants can choose projects that strike their interest, most all on the theme ,"Explore! The Power of Maps". As the week progresses, we'll add animations and stats to visualize progress.
<p/>

The <a href="{{site.baseurl}}/plan/">Guides</a> are a collection of resources for planning and hosting a local event, and for participants at the event to learn and contribute to OSM. We are also supporting <a href="http://teachosm.org/">TeachOSM</a>, a resource for educators to bring OSM into the classroom.
<p/>

For more details about Geography Awareness Week, its history, and more information about this year’s theme, <strong>“Explore! The Power of Maps”</strong> take a look at National Geographic’s <a href="http://education.nationalgeographic.com/programs/geographyawarenessweek/">Geography Awareness Week homepage</a>. Follow <a href="https://twitter.com/search?q=%23osmgeoweek&src=typd">#osmgeoweek</a> for updates during the week, and share your experiences using the #osmgeoweek hashtag.
</div>

